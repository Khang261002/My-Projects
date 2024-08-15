import numpy as np
import os

def func(a):
    # if a:
    #     print(a, " have value")
    # elif a == []:
    #     print(a, " is an empty list")
    # else:
    #     print(a, " have no value")
    if type(a) == np.ndarray:
        if a.size != 0:
            print(True)
        else:
            print(False)
    else:
        print(type(a))

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
w = np.load(os.path.join(__location__, "network_weights.npy"), allow_pickle=True)
b = np.load(os.path.join(__location__, "network_biases.npy"), allow_pickle=True)
a = []
c = np.array([[], []])
func(w)     # True
func(b)     # True
func(a)     # type(a)
func(c)     # False