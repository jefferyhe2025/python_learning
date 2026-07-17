"""
读取文本📁
"""
file = open('file/致橡树_副本.txt', 'r', encoding='utf-8')
print(file.read())
file.close()

# for循环逐行遍历 & readlines方法
file = open('file/致橡树_副本.txt', 'r', encoding='utf-8')
for line in file:
    print(line,end='')
file.close()

file = open('file/致橡树_副本.txt', 'r', encoding='utf-8')
lines = file.readlines()
for line in lines:
    print(line,end='')
file.close()

#添加文本内容✏️
with open('base/file/致橡树_副本.txt','a',encoding='utf-8') as file:
    file.write('\n标题：《致橡树》')
    file.write('\n作者：舒婷')
    file.write('\n时间：1977年3月')

"""
异常处理⛔️
"""
#先占位，让finally能够顺利运行。否则，open（）执行失败没有创建file，finally就会报错。
file = None
try:
    file = open('file/致橡树_副本.txt', 'r', encoding='utf-8')
except FileNotFoundError:
    print('无法打开指定的文件!')
except LookupError:
    print('指定了未知的编码!')
except UnicodeDecodeError:
    print('读取文件时解码错误!')
finally:
    if file:
        file.close()

"""
定义异常和抛出异常
"""
class InputError(ValueError):
    """ 定义输入异常 """
    pass


def fac(num):
    if num < 0:
        # 抛出异常
        raise InputError('参数只能为正数')
    if num in (0,1):
        return 1
    return num * fac(num - 1)

flag = True
while flag:
    try:
        num1 = int(input('请输入要计算的数：'))
        print(f'{num1}的阶乘为{fac(num1)}')
        flag = False
    # 捕获错误并处理异常
    except InputError as err:
        print(err)

"""
上下文管理器语法:自动执行文件对象的close方法
"""
try:
    with open('file/致橡树_副本.txt', 'r', encoding='utf-8'):
        print(file.read())
except FileNotFoundError:
    print('无法打开指定的文件!')
except LookupError:
    print('指定了未知的编码!')
except UnicodeDecodeError:
    print('读取文件时解码错误!')

"""
读写二进制文件
"""
try:
    with open('file/beauty.png','rb') as file1:
        data = file1.read()
    with open('file/sea_copy.png','wb') as file2:
        file2.write(data)
except FileNotFoundError:
    print('文件无法获取')
except IOError:
    print('读写文件时解码错误')
print('程序执行结束')#结束提示🔔

# 若文件过大，可采用以为read方法传入size参数来指定每次读取的字节数，
# 通过循环读取和写入的方式来完成上面的操作
try:
    with open('base/file/beauty.png', 'rb') as file1, open('base/file/sea_copy.png', 'wb') as file2:
        while True:
            data = file1.read(512)  # 每次循环都读 512 字节
            if not data:            # 读到空，说明文件结束
                break
            file2.write(data)
except FileNotFoundError:
    print('文件无法获取')
except IOError:
    print('读写文件时出现错误')
print('程序执行结束')


