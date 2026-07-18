import re
"""
正则表达式
校验用户名和 QQ 号
"""
username = input('请输入用户名: ')
qq = input('请输入QQ号: ')

m1 = re.match(r'^[0-9a-zA-Z_]{6,20}$')
if not m1:
    print('请输入有效的用户名.')

m2 = re.fullmatch(r'[1-9]\d{4,11}', qq)
if not m2:
    print('请输入有效的QQ号.')

if m1 and m2:
    print('你输入的信息是有效的!')

"""
正则表达式
查询手机号
"""
# 用前瞻、后顾，保证手机号前后不再是数字
pattern = re.compile(r'(?<=\D)1[34578]\d{9}(?=\D)')
sentence = '''重要的事情说8130123456789遍，我的手机号是13512346789这个靓号，
不是15600998765，也不是110或119，王大锤的手机号才是15600998765。'''
# 方法一：findall → 得到字符串列表
tel_list = re.findall(pattern,sentence)
for tel in tel_list:
    print(tel)
print('--------华丽的分隔线--------')
# 方法二：finditer → 迭代匹配对象，用 .group() 取内容
for temp in pattern.finditer(sentence):
    print(temp.group())
print('--------华丽的分隔线--------')
# 方法三: 反复search，每次从上次结束位置找
m = pattern.search(sentence)
while m:
    print(m.group())
    m = pattern.search(sentence,m.end())
print('--------华丽的分隔线--------')

"""
正则表达式
替换字符串中的不良内容
"""
sentence = 'Oh, shit! 你是傻逼吗? Fuck you.'
purified = re.sub('fuck|shit|[傻沙煞刹]|[逼必笔比]',
                  '*', sentence, flags=re.IGNORECASE)
print(purified)  # Oh, *! 你是*吗? * you.

"""
正则表达式
拆分长字符串
"""
poem = '窗前明月光，疑是地上霜。举头望明月，低头思故乡。'
sentences_list = re.split(r'[，。]', poem)
sentences_list = [sentence for sentence in sentences_list if sentence]
for sentence in sentences_list:
    print(sentence)