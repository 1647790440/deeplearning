a = [10,9,8,7,6,5,4,3,2,1]
l = len(a)                             #l是数组a的长度
for i in range(0,l-1):  
    for j in range(0,l-1-i):   
        if a[j]>a[j+1]:
            a[j+1],a[j] = a[j],a[j+1]  #同时交换，不需要引入中间变量
print(a)            

    