import numpy as np

#矩阵的转置
a = np.arange(12).reshape(3,4)
print(a)
b = np.transpose(a)  #使用transpose函数
print(b)
c = a.T              #用arrar.T来实现转置
print(c)
