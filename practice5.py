"""
创建列表
"""
items1 = [35, 12, 99, 68, 55, 35, 87]
items2 = ['Python', 'Java', 'Go', 'Kotlin']
items3 = [100, 12.3, 'Python', True]
items4 = list(range(7))
items5 = list('hello')
print(items1)
print(items4)
print(items5)
print(type(items1))

"""
列表的运算
"""
items6 = [29,48,98,55,76]
items7 = [33,11,44]
print(items6 + items7)
items8 = ['Python', 'Java', 'JavaScript']
items8 += items7
print(items8)

print(items8 * 2)
print(29 in items6 )
"""
索引运算
"""
items9 = ['apple', 'waxberry', 'pitaya', 'peach', 'watermelon']
print(items9[0])
print(items9[-1])

# 切片
print(items9[0:5])
print(items9[0:5:2])
print(items9[-4:-1])
print(items9[::2])
print(items9[-2::-1])

# 切片的方式改变元素
items9[1:3] = ['banana','orange']
print(items9)

"""
元素的遍历
"""
# 索引的方式遍历
languages = ['Python', 'Java', 'C++', 'Kotlin']
for index in range(len(languages)):
    print(languages[index])

#  直接遍历列表
languages = ['Python', 'Java', 'C++', 'Kotlin']
for language in languages:
    print(language)

"""
将一颗色子掷6000次，统计每种点数出现的次数(不熟练)
"""
import random
counter = [0] * 6
for _ in range(6000):
    face = random.randint(1,6)
    counter[face - 1] += 1
for face in range(1,7):
    print(f'{face}点出现了{counter[face - 1]}次')


"""
列表的方法：
添加和删除元素、元素位置和频次、元素排序和反转、列表生成式
"""
# 添加和删除元素
languages = ['Python', 'Java', 'C++']
languages.append('JavaScript')
print(languages)
languages.insert(1,'SQL')
print(languages)

if 'Java' in languages:
    languages.remove('Java')
print(languages)
if 'Justin'in languages:
    languages.remove('Justin')
print(languages)
temp = languages.pop(0)
print(temp)
languages.append(temp)
print(languages)
languages.clear()
print(languages)

item = ['Python', 'Java', 'C++']
del item[2]
print(item)
# 元素位置和频次
items = ['Python', 'Java', 'Java', 'C++', 'Kotlin', 'Python']
print(items.index('Python'))
print(items.index('Python',1))
print(items.count('Python'))
print(items.count('Java'))
print(items.count('Kotlin'))

# 元素排序和反转
items10 = ['Python', 'Java', 'C++', 'Kotlin', 'Swift']
items10.sort()
print(items10)
items10.reverse()
print(items10)

# 列表生成式
"""
创建一个取值范围在1到99且能被3或者5整除的数字构成的列表。
"""
item11 = [i for i in range(1,100) if i % 3 == 0 and i % 5 == 0]
print(item11)

"""
有一个整数列表nums1，创建一个新的列表nums2，nums2中的元素是nums1中对应元素的平方。
"""
nums1 = [35, 12, 97, 64, 55]
nums2 = [num ** 2 for num in nums1]
print(nums2)

"""
有一个整数列表nums3，创建一个新的列表nums4，将nums3中大于50的元素放到nums4中。
"""
nums3 = [33, 83, 66, 47, 55]
nums4 = [num for num in nums3 if num > 50]
nums4.sort()
print(nums4)

# 嵌套列表
"""
通过键盘输入的方式来录入5个学生3门课程的成绩并保存在列表中
"""
scores = []
for _ in range(5):
    temp = []
    for _ in range(3):
        score = int(input('请输入学生成绩：'))
        temp.append(score)
    scores.append(temp)
print(scores)
"""
产生随机数的方式来生成5个学生3门课程的成绩并保存在列表中(不熟练)
"""
scores = [[random.randint(60,100) for _ in range(3)] for _ in range(5)]
print(scores)
