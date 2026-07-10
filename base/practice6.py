import timeit
"""
元组的定义和运算
"""
#定义一个三元组和四元组
t1 = (12,45,39)
t2 = ('hi',38,True,'长沙')

# 查看变量类型
print(type(t1))
print(type(t2))

# 查看元组中元素的数量
print(len(t1))
print(len(t2))

#索引运算
print(t1[0])
print(t2[3])

#切片运算
print(t1[::2])
print(t2[:2])

#遍历元组
for index in range(len(t1)):
    print(t1[index])
for elm in t2:
    print(elm)

#成员运算
print(12 in t1)
print(44 not in t1)
print('深圳' in t2)

#拼接运算：
t3 = t1 + t2
print(t3)

#比较运算
print(t1 == t3)
print(t1 <= t3)

#一元组
t4 = (12,)
print(type(t4))
t5 = (123)
print(type(t5))

"""
打包和解包操作
"""
#打包
a = 1,10,100
print(a)
#解包
i,j,k = a
print(i,j,k)

#星号表达式
a = 1,10,100,1000
i,j,*k = a
print(i,j,k)
i,*j,k = a
print(i,j,k)
*i,j = a
print(i,j)
i,j,k,*l = a
print(i,j,k,l)
i,j,k,l,*m = a
print(i,j,k,l,m)

"""
元组 VS 列表
"""
print('%.3f秒' % timeit.timeit('(1,2,3,4,5,6)',number=10000))
print('%.3f秒' % timeit.timeit('[1,2,3,4,5,6]',number=10000))