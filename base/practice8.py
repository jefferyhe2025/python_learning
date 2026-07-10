"""
创建集合
"""
set1 = {1,1,2,2,3,3}
print(set1)
set2 = {'banana','coconut','apple','apple','banana'}
print(set2)
set3 = set('hello')
print(set3)
set4 = set([1,1,3,4,5,3,3])
print(set4)
set5 = {num for num in range(1,20) if num % 3 == 0 or num % 5 == 0}
print(set5)

"""
元素遍历
"""
set6 = {'Python', 'C++', 'Java', 'Kotlin', 'Swift'}
for elm in set6:
    print(elm)

"""
集合的运算：成员运算、交集运算、并集运算、差集运算、比较运算
"""
#成员运算
set1 = {11, 12, 13, 14, 15}
print(10 in set1)      # False
print(15 in set1)      # True
set2 = {'Python', 'Java', 'C++', 'Swift'}
print('Ruby' in set2)  # False
print('Java' in set2)  # True

set1 = {1, 2, 3, 4, 5, 6, 7}
set2 = {2, 4, 6, 8, 10}
#交集运算
print(set1 & set2)
print(set1.intersection(set2))
#并集运算
print(set1 | set2)
print(set1.union(set2))
#差集运算
print(set1 - set2)
print(set1.difference(set2))
#对称差运算
print(set1 ^ set2)
print(set1.symmetric_difference(set2))

#复合运算
set1 = {1, 3, 5, 7}
set2 = {2, 4, 6}
set1 |= set2
print(set1) # set1.update(set2) -> print(set1)
set3 = {3,6,9}
set1 -= set3
print(set1) #set1.intersection_update(set3)
set1 ^= set3
print(set1) #set1.symmetric_difference(set3)

#比较运算
set1 = {1, 3, 5}
set2 = {1, 2, 3, 4, 5}
set3 = {5, 4, 3, 2, 1}

print(set1 < set2)   # True
print(set1 <= set2)  # True
print(set2 < set3)   # False
print(set2 <= set3)  # True
print(set2 > set1)   # True
print(set2 == set3)  # True

print(set1.issubset(set2))    # True
print(set2.issuperset(set1))  # True

"""
集合的方法
"""
set1 = {1, 10, 100}

#添加元素
set1.add(1000)
set1.add(10000)
print(set1)

#删除元素
set1.discard(100)
if 10 in set1:
    set1.remove(10)
print(set1)

#清空集合
set1.clear()
print(set1)

#判断有没有相同的元素
set1 = {'Java', 'Python', 'C++', 'Kotlin'}
set2 = {'Kotlin', 'Swift', 'Java', 'Dart'}
set3 = {'HTML', 'CSS', 'JavaScript'}
print(set1.isdisjoint(set2))
print(set1.isdisjoint(set3))

"""
不可变集合：类比列表和元组
"""
fset1 = frozenset({1, 3, 5, 7})
fset2 = frozenset(range(1, 6))
print(fset1)          # frozenset({1, 3, 5, 7})
print(fset2)          # frozenset({1, 2, 3, 4, 5})
print(fset1 & fset2)  # frozenset({1, 3, 5})
print(fset1 | fset2)  # frozenset({1, 2, 3, 4, 5, 7})
print(fset1 - fset2)  # frozenset({7})
print(fset1 < fset2)  # False