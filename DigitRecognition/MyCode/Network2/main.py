#### Libraries
### Third-party Libraries
import sys
sys.path.insert(0, './DigitRecognition/MyCode/Data_Loader')

# My libraries
import hand_drawing
import mnist_loader
import network2
import os

if __name__ == "__main__":
    training_data, validation_data, test_data = \
        mnist_loader.load_data_wrapper()
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

    if os.path.isfile(os.path.join(__location__, "trained_model.txt")):
        net = network2.load(os.path.join(__location__, "trained_model.txt"))
    else:
        net = network2.Network([784, 30, 10], cost=network2.CrossEntropyCost)
        net.SGD(training_data, 30, 10, 0.5,
            lmbda=5.0,
            evaluation_data=validation_data,
            monitor_evaluation_accuracy=True,
            monitor_training_cost=True,
            early_stopping_n=10)
        net.save("trained_model.txt")
    hand_drawing.check_drawing(net)
