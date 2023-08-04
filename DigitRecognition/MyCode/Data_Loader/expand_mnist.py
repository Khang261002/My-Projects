"""expand_mnist.py
~~~~~~~~~~~~~~~~~~

Take the 50,000 MNIST training images, and create an expanded set of
250,000 images, by displacing each training image up, down, left and
right, by one pixel.  Save the resulting file to
../data/mnist_displacement_expanded.pkl.gz.

I have also developed a rotation function capable of rotating images
by 10 degrees in both clockwise and counterclockwise directions. The
primary objective behind this implementation is to avoid excessive
rotation, which could result in unnatural angles. By employing this
technique, we can effectively generate three times the amount of
training data. Consequently, by combining both approaches, our
dataset will encompass a total of 750,000 images.

Note that this program is memory intensive, and may not run on small
systems.

"""

from __future__ import print_function

#### Libraries

# Standard library
import pickle
import gzip
import os.path
import random

# Third-party libraries
import numpy as np
from scipy.ndimage import rotate

def displacement(training_data):
    expanded_training_pairs = []
    j = 0 # counter
    for x, y in zip(training_data[0], training_data[1]):
        expanded_training_pairs.append((x, y))
        image = np.reshape(x, (-1, 28))
        j += 1
        if j % 1000 == 0: print("Displacing-Expanding image number", j)
        # iterate over data telling us the details of how to
        # do the displacement
        for d, axis, index_position, index in [
                (1,  0, "first", 0),
                (-1, 0, "first", 27),
                (1,  1, "last",  0),
                (-1, 1, "last",  27)]:
            new_img = np.roll(image, d, axis)
            if index_position == "first": 
                new_img[index, :] = np.zeros(28)
            else: 
                new_img[:, index] = np.zeros(28)
            expanded_training_pairs.append((np.reshape(new_img, 784), y))
    random.shuffle(expanded_training_pairs)
    expanded_training_data = [list(d) for d in zip(*expanded_training_pairs)]
    return expanded_training_data

def rotation(training_data):
    expanded_training_pairs = []
    j = 0 # counter
    for x, y in zip(training_data[0], training_data[1]):
        expanded_training_pairs.append((x, y))
        image = np.reshape(x, (-1, 28))
        j += 1
        if j % 1000 == 0: print("Rotating-Expanding image number", j)
        # iterate over data telling us the details of how to
        # do the rotation
        for alpha in [-10, 10]:
            new_img = rotate(image, angle=alpha, reshape=False)
            expanded_training_pairs.append((np.reshape(new_img, 784), y))
    random.shuffle(expanded_training_pairs)
    expanded_training_data = [list(d) for d in zip(*expanded_training_pairs)]
    return expanded_training_data

if __name__ == '__main__':
    print("Expanding the MNIST training set")
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

    if os.path.exists(os.path.join(__location__, "mnist_expanded.pkl.gz")):
        print("The expanded training set already exists. Exiting.")
    else:
        f = gzip.open(os.path.join(__location__, 'mnist.pkl.gz'), 'rb')
        training_data, validation_data, test_data = pickle.load(f, encoding="latin1")
        f.close()

        expanded_training_data = rotation(training_data)
        expanded_training_data = displacement(expanded_training_data)
        
        print("Saving expanded data. This may take a few minutes.")
        f = gzip.open(os.path.join(__location__, "mnist_expanded.pkl.gz"), "w")
        pickle.dump((expanded_training_data, validation_data, test_data), f)
        f.close()
    print("Completed!")
