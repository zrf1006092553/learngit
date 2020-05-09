#!/usr/bin/python
# -*- coding: utf-8 -*-
#map 和 reduce的用法
from functools import reduce
L1 = [1, 2, 3, 6, 8, 9, 6, 5]
L2 = L1[::1]
n1 = list(map(str, L1))
print(n1)

def f1(x, y):
    return x * 10 + y   #变成整数
n2 = reduce(f1, L2)
print(n2)

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
#构造char和int的字典 用于key返回value的对应转换
def char2num(s):
    return DIGITS[s]
def str2int(s): #构造lambda函数，配合map实现字符转整数
    return reduce(lambda x, y: x * 10 + y, map(char2num,s))
print(str2int(n1))


# homework
#利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
# -*- coding: utf-8 -*-

def normalize(name):
    return name.title()
    

# 测试:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)





# -*- coding: utf-8 -*- 请编写一个prod()函数，可以接受一个list并利用reduce()求积：
from functools import reduce

def prod(L):
    def fn(x, y):
        return x * y
    L = reduce(fn, L)
    return L

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')



# -*- coding: utf-8 -*-
#利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
from functools import reduce

def str2float(s):
    n = 0
    while s[n] == '.':
        n = n + 1
    L1 = s[:n]
    L2 = s[n + 1:]
    # 先使用字符串转int 再使用reduce构造多位数
    s1 = reduce(lambda x, y: x * 10 + y, map(char2num, L1))
    s2 = reduce(lambda x, y: x / 10 + y, map(char2num, L2))
    return s1 + s2
#返回值求和即可
print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')


