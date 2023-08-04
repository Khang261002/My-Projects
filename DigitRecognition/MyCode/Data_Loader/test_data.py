import pickle
import gzip
import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = gzip.open(os.path.join(__location__, 'mnist.pkl.gz'), 'rb')
training_data, validation_data, test_data = pickle.load(f, encoding="latin1")
f.close()
print(len(validation_data[1]))