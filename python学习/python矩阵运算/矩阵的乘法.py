import numpy as np

#矩阵的乘法
a = np.arange(6).reshape(1,6)     #这是一个1*6的行矩阵
print(a)
b = np.transpose(a)               #这是一个6*1的列矩阵
print(b)
c = a * b                         #这个并不是矩阵的乘法
print(c)
d = np.dot(a,b)                   #要实现矩阵乘法，必须使用numpy.dot()函数
print(d)
e = np.dot(b,a)
print(e)

