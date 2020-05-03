#!/usr/bin/python
# -*- coding: utf-8 -*-
import math

def power(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
    
print(power(int(input()), int(input())))