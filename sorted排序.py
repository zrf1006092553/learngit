#!/usr/bin/python
# -*- coding: utf-8 -*-
L1 = [1, 6, 89, 45, 65, 78, 26, -48, -2, -59, -2]

def sort(s):
    return sorted(s)
    
print(sort(L1))

#sorted是高阶函数 可以实现key的绝对值排序
print(sorted(L1, key = abs))

#实现大小写排序
L2 = ['bob', 'about', 'Zoo', 'Credit']

print(sorted(L2, key = str.lower))#正向字母排序
print(sorted(L2, key = str.lower, reverse = True))#反向字母排序

#请用sorted()对上述列表分别按名字排序
L3 = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

# -*- coding: utf-8 -*-
from operator import itemgetter
def by_name(t):
   return t[0]

L4 = sorted(L3, key = by_name)
print(L4)

#再按成绩从高到低排序：

def by_score(t):
    return t[1]

L5 = sorted(L3, key = by_score, reverse = True)
print(L5)
