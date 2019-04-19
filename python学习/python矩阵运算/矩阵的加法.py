import numpy as np

#矩阵的加
a = np.arange(16).reshape(4,4)
print(a)
b = np.ones([4,4],dtype = int)
print(b)
c = a + b           #方法1
print(c)
d = np.add(a,b)     #方法2
print(d)