"""
字符串的定义
"""
#字符串的定义
s1 = 'hello, world!'
s2 = "你好，世界！❤️"
s3 = '''hello,
wonderful
world!'''
print(s1,s2,s3)

#转义字符
s1 = '\'hello, world!\''
s2 = '\\hello,world!\\'
print(s1)
print(s2)

#原始字符串
s1 = '\it \is \time \to \read \now'
s2 = r'\it \is \time \to \read \now'
print(s1)
print(s2)

#字符的特殊表示
s1 = '\141\142\143\x61\x62\x63'
s2 = '\u4f55\u51a0\u81fb'  # "何冠臻"

"""
字符串的运算
"""
#拼接和重复
s1 = 'hello' + ', ' + 'world'
s2 = '!' * 3
print(s1)
print(s2)

#比较运算
s1 = 'a whole new world'
s2 = 'hello world'
s3 = '冠臻'
s4 = '王大锤'
print(s1 == s2)
print(s1 < s2)
print('hello world'== s1)
print('hello world'== s2)
print(ord('冠'))
print(ord('臻'))
print(s3 > s4)

#成员运算
s1 = 'hello, world'
s2 = 'goodbye, world'
print('bye' in s1)
print('bye' in s2)

#获取字符串长度
s = 'hello, world'
print(len(s))

#索引和切片
s = 'abc123456'
print(s[0])
print(s[-6:-3])
print(s[::2])
print(s[::3])

"""
字符的遍历
"""
#字符的遍历
s = 'hello'
for index in range(len(s)):
    print(s[index])

for elm in s:
    print(elm)

"""
字符串的方法
"""
#大小写相关操作
s1 = 'hello, world!'
s2 = 'GOODBYE'
print(s1.capitalize()) #首字母大写
print(s1.title())
print(s1.upper())
print(s2.lower())

#查找操作
s = 'hello, world!'
print(s.find('lo'))
print(s.find('ld',5))
print(s.index('lo'))
print(s.find('o'))
print(s.rfind('o'))

#性质判断
s1 = 'hello, world!'
s2 = 'abc123456'
print(s1.startswith('He'))
print(s1.startswith('he'))
print(s2.isdigit())
print(s2.isalpha())
print(s2.isalnum())

#格式化
s = 'hello, world'
print(s.center(20,'-'))
print(s.ljust(20,))
print(s.rjust(20,'~'))
print('32'.zfill(6)) #补零
print('44'.zfill(4))
a = 321
b = 123
# 三种格式化输出
print('%d + %d = %d'%(a,b,a+b))
print('{0} + {1} = {2}'.format(a,b,a+b))
print(f'{a} + {b} = {a+b}')

#修剪操作
s1 = '   jackfrued@126.com  '
s2 = '~你好，世界~'
print(s1.strip()) #默认修建空格
print(s2.lstrip('~'))
print(s2.rstrip('~'))

#替换操作
s = 'hello, good world'
print(s.replace('o','@'))
print(s.replace('o','@',1))

#拆分与合并
s = 'I love you'
s1 = 'I#love#you#so#much'
word1 = s.split()
print(word1)
print('~'.join(word1)) #合并
print(s1.split('#'))
print(s1.split('#',2))

#编码和解码
a = '冠臻'
b = a.encode('utf-8')
c = a.encode('gbk')
print(b,c)
print(b.decode('utf-8'))
print(c.decode('gbk'))