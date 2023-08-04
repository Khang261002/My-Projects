from tensorflow.keras.datasets import mnist
from scipy.ndimage import rotate
import matplotlib.pyplot as plt
from expand_mnist import rotation

train, (X_test, Y_test) = mnist.load_data()
num = 5
train = rotation(train)
X_train, Y_train = train
images = X_train[:(num*5)]
labels = Y_train[:(num*5)]
num_row = 5
num_col = 5
# plot images
# print('BEFORE:')
# fig1, axes1 = plt.subplots(num_row, num_col, figsize=(1.5*num_col,2*num_row))
# for i in range(num):
#     ax = axes1[i//num_col, i%num_col]
#     ax.imshow(images[i], cmap='gray')
#     ax.set_title('Label: {}'.format(labels[i]))
# plt.tight_layout()
# plt.show()

print('AFTER:')
fig2, axes2 = plt.subplots(num_row, num_col, figsize=(1.5*num_col,2*num_row))
for i in range(num):
    ax = axes2[i//num_col, i%num_col]
    ax.imshow(images[i].reshape(28,28), cmap='gray')
    ax.set_title('Label: {}'.format(labels[i]))
plt.tight_layout()
plt.show()
print("Complete!")
