#!/usr/bin/python
# -*- coding: utf-8 -*-

#tao wa diaoyong 
def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)
    
print(fact(5))

def f1(n):
    return f2(n, 1)

def f2(n, y):
    if n == 1:
        return y
    return f2(n - 1, n * y)
    
print(f1(5))

#Hanoi tower
def move(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
    else:
        move(n - 1, a, c, b)
        print(a, '-->', c)
        move(n - 1, b, a, c)

move(3, 'A', 'B', 'C')
        