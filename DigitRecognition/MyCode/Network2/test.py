sizes = [784, 30, 10]
for x, y in zip(sizes[:-1], sizes[1:]):
    print("x: {}, y: {}".format(x, y))