import numpy as np
import matplotlib.pyplot as plt

#读取数据
data = np.loadtxt('../ex2data.txt',delimiter=',')  #'../ex2data.txt'是测试数据文档的目录
#print(data)    测试读取是否正确
X = np.c_[data[:,0]]
y = np.c_[data[:,1]]
theta = [0,0]
#print(theta[0])    #测试
#print(theta[1])    #测试
#print(X)   #测试
#print(y)   #测试
#print(np.dot(X,theta[0]))    #测试

def cost_function(X,y,theta):    #代价函数
    m = y.size
    h = np.dot(X,theta[0])+theta[1]
    j = 1.0/(2*m)*(np.sum(np.square(h-y)))
    return j

#print(cost_function(X,y,theta))    #测试

def gradient_descent(X,y,theta,alpha=0.01,times=1000):         #梯度下降，学习率初始值为0.001，循环次数为1000
    m = y.size
    C = np.zeros(times)
    for i in np.arange(times):
        C[i] = cost_function(X,y,theta)
        h = np.dot(X,theta[0])+theta[1]
        theta0 = theta[0]-(alpha/m)*(np.dot(X.T,(h-y))[0][0])   #同步下降
        theta1 = theta[1]-(alpha/m)*(np.sum(h-y))
        theta[0] = theta0
        theta[1] = theta1
        #print(theta)
    return(theta,C)
theta,C = gradient_descent(X,y,theta)

print(theta)
#print(C)


#显示数据,使用matplotlib库画出二维图形
'''
plt.scatter(X,y,s=30,c='r',marker='x',linewidths=1)
plt.show()
'''

#代价函数的变换曲线
plt.plot(C)    
plt.show()

#原数据和拟合函数
xx = np.arange(5,23)
yy = theta[0]*xx+theta[1]
plt.scatter(X,y,s=30,c='r',marker='x',linewidths=1)    
plt.plot(xx,yy)
plt.show()


    

