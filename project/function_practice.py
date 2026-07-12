import random,string
"""
例子1：随机验证码
"""
#生成所有的数字和字母
ALL_CHARS = string.digits + string.ascii_letters

def generate_code(*,code_len=4):
    """
    生成随机验证码
    :param code_len: 默认长度为4
    """
    print(''.join(random.choices(ALL_CHARS,k=code_len)))

n = int(input('需要几行验证码：'))
for _ in range(n):
    generate_code()

"""
例子2：判断素数
"""
def is_prime(num:int) -> bool:
    for i in range(1,int(num ** 0.5)+1):
        if num % i ==0:
            return  False
    return True
print(is_prime(8))

"""
例子3：最大公约数和最小公倍数
"""
def gcd(x:int,y:int) -> int:
    """ 求最大公约数"""
    while y % x !=0:
        x,y = y % x,x
    return x
def lcm(x:int,y:int) -> int:
    """ 求最小公倍数 """
    return x * y // gcd(x,y)

"""
例子4：数据统计
"""
def ptp(data):
    """ 极差 """
    return max(data) - min(data)

def mean(data):
    """ 算术平均 """
    return sum(data)/len(data)

def median(data):
    temp,size = sorted(data),len(data)
    if size % 2 == 0:
        return mean(temp[size // 2 -1:size //2 +1])
    else:
        return temp[size // 2]

def var(data, ddof=1):
    """方差"""
    x_bar = mean(data)
    temp = [(num - x_bar) ** 2 for num in data]
    return sum(temp) / (len(temp) - ddof)

def std(data, ddof=1):
    """标准差"""
    return var(data, ddof) ** 0.5

def cv(data, ddof=1):
    """变异系数"""
    return std(data, ddof) / mean(data)

def describe(data):
    """输出描述性统计信息"""
    print(f'均值: {mean(data)}')
    print(f'中位数: {median(data)}')
    print(f'极差: {ptp(data)}')
    print(f'方差: {var(data)}')
    print(f'标准差: {std(data)}')
    print(f'变异系数: {cv(data)}')