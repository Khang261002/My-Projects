import os
import network3
import hand_drawing
# softmax plus log-likelihood cost is more common in modern image classification networks.
from network3 import Network, ConvPoolLayer, FullyConnectedLayer, SoftmaxLayer, ReLU

if __name__ == '__main__':
    # read data:
    training_data, validation_data, test_data = network3.load_data_shared("mnist_expanded.pkl.gz")
    # mini-batch size:
    mini_batch_size = 10
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

    if os.path.isfile(os.path.join(__location__, "Model/best_model.pkl")):
        net = Network.load_network()
    else:
        net = Network([
            ConvPoolLayer(image_shape=(mini_batch_size, 1, 28, 28),
                        filter_shape=(20, 1, 5, 5),
                        poolsize=(2, 2),
                        activation_fn=ReLU),
            ConvPoolLayer(image_shape=(mini_batch_size, 20, 12, 12),
                        filter_shape=(40, 20, 5, 5),
                        poolsize=(2, 2),
                        activation_fn=ReLU),
            FullyConnectedLayer(n_in=40*4*4, n_out=100, activation_fn=ReLU),
            SoftmaxLayer(n_in=100, n_out=10)], mini_batch_size)
        net.SGD(training_data, 60, mini_batch_size, 0.03,
                validation_data, test_data, lmbda=0.1, early_stopping_n=10)
    hand_drawing.check_drawing(net)

# run with python 3.5: py -3.5 -u "./DigitRecognition/MyCode/Network3/main.py"