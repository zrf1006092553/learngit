#!/usr/bin/python
# -*- coding: utf-8 -*-
#构造奇数列表
L = []
n = 1
while n <= 99:
    L.append(n)
    n = n +2
    
print(L)

#切片操作 简化取值索引范围

print(L[0:10])
print(L[-9:-1])

#前十个数 步长为2
print(L[:10:2])

#所有数 步长为5
print(L[::5])
print('qwertyuiopasdfghjkl' [:8])
print('asdfghjklzxcvbnm' [::2])

print((0, 3, 5, 8, 6, 7)[:3])
#利用切片操作，实现一个trim()函数，去除字符串首尾的空格
#，注意不要调用str的strip()方法：


def trim(s):
    while len(s) > 0 and s[0] == '':
        return s == s[1:]
    while len(s) > 0 and s[-1] == '':
        return s == s[:-1]
    return s
            
# 测试:
if trim('hello  ') != 'hello':
    print('测试失败1!')
    print(trim('hello  '))
elif trim('  hello') != 'hello':
    print('测试失败2!')
elif trim('  hello  ') != 'hello':
    print('测试失败3!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败4!')
elif trim('') != '':
    print('测试失败5!')
elif trim('    ') != '':
    print('测试失败6!')
else:
    print('测试成功7!')