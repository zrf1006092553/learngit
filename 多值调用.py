#!/usr/bin/python
# -*- coding: utf-8 -*-

def person(name, age, *args, **kw):
    print('name', name, 'age', age, 'other', kw)
    
def pet(name, age, *, city = 'Beijing', job, **kw):
    print('name = ', name, 'age = ', age, 'city = ', city, 'job = ', job)

person('Chow', 30, city = 'Hefei', job = 'trainer')
pet('Peter', 24, job = 'Engineer')

args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
person(*args, **kw)

#multi-numbers 
def product(*x):
    y = 1
    if len(x) == 0:
        raise TypeError
    else:
        for n in x:
            y = y * n
    return y

#test
# 测试
print('product(5) =', product(5))
print('product(5, 6) =', product(5, 6))
print('product(5, 6, 7) =', product(5, 6, 7))
print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
if product(5) != 5:
    print('测试失败!')
elif product(5, 6) != 30:
    print('测试失败!')
elif product(5, 6, 7) != 210:
    print('测试失败!')
elif product(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    try:
        product()
        print('测试失败!')
    except TypeError:
        print('测试成功!')