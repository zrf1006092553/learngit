#!/usr/bin/python
# -*- coding: utf-8 -*-

def cal(*number):
    sum = 0
    for n in number:
        sum = sum + n * n
    return sum
    
print(cal(int(input()), int(input()), int(input()), int(input())))