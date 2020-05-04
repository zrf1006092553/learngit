#!/usr/bin/python
# -*- coding: utf-8 -*-

#快速list
n = list(range(1, 10))
print(n)

#快速n * n的list
L = []
for x in range(1, 10):
    L.append(x * x)
print(L)

#一条语句循环生成上面的n * n list
K = [x * x for x in range(1, 10)]
print(K)

#一句话判断并建立L中的偶数的平方
J = [x * x for x in range(1, 10) if x % 2 == 0]
print(J)

#字符串两层循环，三层以及以上循环很少用到
O = [m + n for m in 'ABCD' for n in 'WXYZ']
print(O)

#列出当前目录下的所有文件和目录名
import os 
P = [d for d in os.listdir('.')]
print(P)
#利用dict和items（）可以同时迭代key和value
A = {'x': 'A', 'y': 'B', 'z': 'C'}
for k, v in A.items():
    print(k, '=', v)

#通过两个变量生成list
P2 = [k + '=' + v for k, v in A.items()]
print(P2)

#把list中变成小写字符串
L2 = ['Hello', 'World', 'IBM', 'Apple']
L3 = [s.lower() for s in L2]
print(L3)

#if else 的用法
#这是因为for前面的部分是一个表达式，
#它必须根据x计算出一个结果。因此，考察表达式：
#x if x % 2 == 0，它无法根据x计算出结果，
#因为缺少else，必须加上else：
P2 = [x if x % 2 == 0 else -x for x in range(1, 10)]
print(P2)

## -*- coding: utf-8 -*-
#使用内建的isinstance函数可以判断一个变量是不是字符串：
L1 = ['Hello', 'World', 18, 'Apple', None]

L2 = [x.lower() for x in L1 if isinstance(x, str)]

# 测试:
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')


