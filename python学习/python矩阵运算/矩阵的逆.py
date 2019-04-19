import numpy as np


#矩阵的逆
a = np.arange(1,5).reshape(2,2)
print(a)
b = np.linalg.inv(a)            #取逆
print(b)
c = np.dot(a,b)                 #c为单位矩阵
print(c)

a = np.eye(4)
print(a)
b = np.eye(4)
print(b)
c = np.dot(a,b)
print(c)