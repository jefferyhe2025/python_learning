"""
下载和上传函数 + 记录时间的装饰器
"""
import random
import time
from functools import wraps,lru_cache

def record_time(func):
    """ 记录时间的装饰器 """
    @wraps(func) #可以取消对原函数的装饰
    def wrapper(*args,**kwargs):
        print('开始计时')
        start = time.time()
        #执行被装饰的函数
        result = func(*args,**kwargs)
        end = time.time()
        #计算函数运行的时间
        print(f'{func.__name__}花费时间:{end - start:.2f}秒')
        return result
    return wrapper # 返回wrapper函数，替换原函数

@record_time # 💻用语法糖的方式调用装饰器函数
def download(filename):
    print(f'开始下载文件{filename}')
    # 模拟下载时间（最多6秒）
    time.sleep(random.random() * 6)
    print(f'{filename}下载完成')

@record_time
def upload(filename):
    print(f'开始上传文件{filename}')
    #模拟上传时间（最多8秒）
    time.sleep(random.random() * 8)
    print(f'{filename}上传完成')

# 调用装饰器:🔊1.先替换（wrapper->download/upload）2.再执行wrapper()
# download = record_time(download)
# upload = record_time(upload)
download('MySQL从删库到跑路.avi')
upload('Python从入门到住院.pdf')
# 取消装饰器
download.__wrapped__("MySQL从删库到跑路.avi")
upload.__wrapped__('Python从入门到住院.pdf')

"""
函数的递归调用：函数自己调用自己
收敛条件：函数什么时候结束递归
栈与栈帧：
"""
#递归实现阶乘
def fac(num):
    """ 递归实现阶乘 """
    if num in (0,1): #函数的收敛条件
        return 1
    return num * fac(num -1 )

#递归打印斐波那契数列
#装饰器解决fib1重复调用
@lru_cache() #装饰器有参数需要()
def fib1(n):
    """ 递归打印斐波那契数列 """
    if n in (1,2):
        return 1
    return fib1(n-1) + fib1(n-2)

for i in range(1,40):
    print(fib1(i))



