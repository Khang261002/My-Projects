import os
import new_network3
import hand_drawing
# softmax plus log-likelihood cost is more common in modern image classification networks.
from new_network3 import Network, ConvPoolLayer, FullyConnectedLayer, SoftmaxLayer, ReLU

if __name__ == '__main__':
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

    # mini-batch size:
    mini_batch_size = 10

    if os.path.isfile(os.path.join(__location__, "Model/best_model.pkl")):
        net = Network.load_network()
    else:
        # read data:
        training_data, validation_data, test_data = new_network3.load_data_shared("mnist_expanded.pkl.gz")
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
        net.SGD(training_data, 60, mini_batch_size, 0.03, validation_data, test_data,
                lmbda=0.1, early_stopping_n=20, constant_eta=False)
    hand_drawing.check_drawing(net)

# run with python 3.5: py -3.5 -u "./MyCode/Network3/main.py"
# model_0:      test 10 epochs
# model_1:      mnist.pkl.gz, 60 epochs, early_stopping_n = 10 --> 99.13%
# model_2:      mnist_displacement_expanded.pkl.gz, 60 epochs, early_stopping_n = 10 --> 99.43%
# model_3:      mnist_expanded.pkl.gz, 60 epochs, early_stopping_n = 20 --> 99.41%
# model_4:      mnist_expanded.pkl.gz, 60 epochs, early_stopping_n = 20 --> 99.46%
# model_5:      mnist_expanded.pkl.gz, 60 epochs, early_stopping_n = 20 --> 99.45%
# best_model:      mnist_expanded.pkl.gz, 60 epochs, early_stopping_n = 20 --> 99.60%
# model_7:      mnist_expanded.pkl.gz, 60 epochs, early_stopping_n = 20 --> 99.48%
# model_8:      new_network3, mnist_expanded.pkl.gz, 60 epochs,
#               early_stopping_n = 20, constant_eta = False, new_eta = eta/2 --> 99.55%
# model_9:      new_network3, mnist_expanded.pkl.gz, 60 epochs,
#               early_stopping_n = 20, constant_eta = False, new_eta = eta/2 --> 99.46%
# model_10:     new_network3, mnist_expanded.pkl.gz, 60 epochs,
#               early_stopping_n = 20, constant_eta = False,
#               new_eta = eta/(1.0 + eta_decrease_factor*(epoch + 1)) --> 99.49%
# model_11:   new_network3, mnist_expanded.pkl.gz, 60 epochs,
#               early_stopping_n = 20, constant_eta = False,
#               new_eta = eta/(1.0 + eta_decrease_factor*(epoch + 1)) --> 99.52%
