#!/usr/bin/python
# -*- coding: utf-8 -*-

#函数名就是指向函数的变量
g = abs
print(g(-825))


#高阶函数调用
def add(x, y, f):
    return f(x) + f(y)

print(add(-5, 6, abs))