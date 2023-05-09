import numpy as np

_A = [[1,2,3],
      [4,5,6],
      [7,8,9]]
_B = [[10,11],
      [12,13],
      [14,15]]
_C = [[1,2,3],
      [0,1,4],
      [5,6,0]]

I3 = np.eye(3)
A = np.array(_A) # This is a vector
AT = np.transpose(A)
B = np.array(_B)
C = np.array(_C)
C_1 = np.linalg.pinv(C)

print('A^T = \n', AT)
print('A*B = \n', A.dot(B))
print('A*B = \n', A@B)
print('A*I3 = \n', A*I3)
print('Number of row of B = ', np.size(B,0))           # 0 is row and 1 is column
print('Number of column of B = ', np.size(B,1))
print('Shape of B is ', B.shape)
print('Size of B = ', np.size(B))
print('C^-1 = \n', C_1)
print('C*C^-1 = \n', C@C_1)
