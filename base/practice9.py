"""
创建和使用字典
"""
xinhua = {
    '麓': '山脚下',
    '路': '道，往来通行的地方；方面，地区：南～货，外～货；种类：他俩是一～人',
    '蕗': '甘草的别名',
    '潞': '潞水，水名，即今山西省的浊漳河；潞江，水名，即云南省的怒江'
}
print(xinhua)
person = {
    'name': '王大锤',
    'age': 55,
    'height': 168,
    'weight': 60,
    'addr': '成都市武侯区科华北路62号1栋101',
    'tel': '13122334455',
    'emergence contact': '13800998877'
}
print(person)

#函数dict或者是字典的生成式语法生成字典
person = dict(name = '王大锤',age = 55,height = 178,weight = 140)
print(person)
#Python内置函数zip压缩两个序列并创建字典
item1 = dict(zip('ABCDE','12345'))
print(item1)
item2 = dict(zip('ABCDE',range(1,8)))
print(item2)
person1 = {x:x ** 2 for x in range(10)}
print(person1)

#对字典的键for循环遍历
person = {
    'name': '王大锤',
    'age': 55,
    'height': 168,
    'weight': 60,
    'addr': '成都市武侯区科华北路62号1栋101'
}
print(len(person))
for key in person:
    print(key)

"""
字典的运算：成员运算和索引运算
"""
#成员运算
person = {'name': '王大锤', 'age': 55, 'height': 168, 'weight': 60, 'addr': '成都市武侯区科华北路62号1栋101'}
print('name'in person)
print('tel' in person)

#索引运算
print(person['weight'])
person['age'] = 21
person['height'] = 180
person['signiture'] = '他是大帅哥'
print(person)

#遍历
for key in person:
    print(f'{key}: {person[key]}')

"""
字典的方法
"""
#获取键值
person = {'name': '王大锤', 'age': 25, 'height': 178, 'addr': '成都市武侯区科华北路62号1栋101'}
print(person.get('name'))
print(person.get('family'))
print(person.get('sex',0))

#获取所有键和值
person = {'name': '王大锤', 'age': 25, 'height': 178}
print(person.keys())
print(person.values())
print(person.items())
for key,value in person.items():
    print(f'{key}:\t{value}')

#合并操作
person1 = {'name': '王大锤', 'age': 55, 'height': 178}
person2 = {'age': 25, 'addr': '成都市武侯区科华北路62号1栋101'}
person1.update(person2)
print(person1)
# person1 |= person2
# print(person1)

#删除操作
person = {'name': '王大锤', 'age': 25, 'height': 178, 'addr': '成都市武侯区科华北路62号1栋101'}
print(person.pop('height'))
print(person)
print(person.popitem())
print(person)

del person['age']
print(person)

"""
字典应用
"""
sentence = input('请输入一段话：')
count = {}

for ch in sentence:
    if 'a' <= ch <= 'z' or 'A' <= ch <= 'Z':
        count[ch] = count.get(ch,0) + 1 #索引添加key
sorted_keys = sorted(count,key=count.get,reverse=True)
for key in sorted_keys:
    print(f'{key}出现的次数：{count[key]}')
