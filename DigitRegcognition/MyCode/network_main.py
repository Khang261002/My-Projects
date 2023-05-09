#### Libraries
# My libraries
import hand_drawing
import mnist_loader
import network
import os

### Third-party Libraries
import numpy as np

if __name__ == "__main__":
    training_data, validation_data, test_data = \
        mnist_loader.load_data_wrapper()
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    
    if (os.path.isfile(os.path.join(__location__, "network_weights.npy")) and 
        os.path.isfile(os.path.join(__location__, "network_biases.npy"))):
        weights = np.load(os.path.join(__location__, "network_weights.npy"), allow_pickle=True)
        biases = np.load(os.path.join(__location__, "network_biases.npy"), allow_pickle=True)
        net = network.Network([784, 30, 10], trained_weights=weights, trained_biases=biases)
    else:
        net = network.Network([784, 30, 10])
        net.SGD(training_data, 30, 10, 3.0, test_data=test_data)
    hand_drawing.check_drawing(net)
