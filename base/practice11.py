"""
把一个函数作为其他函数的参数或返回值的用法，我们通常称之为“高阶函数”。
"""
#引入高级函数
import operator
import functools

"""
累加器
version1.0
"""
def cal(*args,**kwargs):
    """
    设计一个累加器
    :return: 累加结果
    """
    items = list(args) + list(kwargs.values())
    result = 0
    for item in items:
        if type(item) in (int,float):
            result += item
    return result

"""
方便的累加器
version1.1
"""
def calc(init_value, op_func, *args, **kwargs):
    """
    引入一个二元计算器，解耦 result += item，成为一个累计计算器
    :param init_value:初始值
    :param op_func: 二元运算函数
    :return:计算结果
    """
    items = list(args) + list(kwargs.values())
    result = init_value
    for item in items:
        if type(item) in (int, float):
            result = op_func(result, item)
    return result
print(calc(0,operator.add,1,2,3,4,5,6))
print(calc(1,operator.mul,1,2,3,4,5,6))

"""
map函数和filter函数
"""
def even(num):
    """ 判断是否为偶数 """
    return num % 2 == 0
def square(num):
    """ 平方 """
    return num ** 2

old_num = [12,44,33,98,57]
new_num = list(map(square,filter(even,old_num))) #⚠️map函数返回None
print(new_num)
#用列表生成器实现上述功能,非常优雅
old_num = [12,44,33,98,57]
new_num = [num ** 2 for num in old_num if num % 2 == 0]
print(new_num)

"""
sorted函数->返回一个列表
"""
old_strings = ['in', 'apple', 'zoo', 'waxberry', 'pear']
new_strings = sorted(old_strings)
print(new_strings)
#改变排序方式
old_strings = ['in', 'apple', 'zoo', 'waxberry', 'pear']
new_strings = sorted(old_strings,key=len)
print(new_strings)

"""
Lambda函数(匿名函数)：实现只有一行功能的函数（需要加强这方面的理解）
"""
old_nums = [12,44,33,98,57]
new_nums = list(map(lambda x:x ** 2,filter(lambda x:x % 2 == 0,old_nums)))
print(new_nums)

#用lambda函数实现一行阶乘和判断素数
fac = lambda n: functools.reduce(operator.mul,range(2,n + 1),1)
is_prime = lambda x:all(map(lambda f:x % f,range(2,int(x ** 0.5) + 1))) #all()对所有的数值进行布尔判断，非零为True
print(fac(5))
print(is_prime(19))

"""
偏函数
"""
#partial函数的第一个参数和返回值都是函数
int2 = functools.partial(int,base=2)
int3 = functools.partial(int,base=8)
int4 = functools.partial(int,base=16)

print(int(10))
print(int2(10))
print(int3(10))
print(int4(10))

