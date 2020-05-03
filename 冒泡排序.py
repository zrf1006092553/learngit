#!/usr/bin/python
# -*- coding: utf-8 -*-

lis1 = [56,32,59,78,5,15,79,17,56,2,-9,478,65,651,-2684,6541,89,48]

def sortport(lis):
    for i in range(len(lis)-1):
        for j in range(len(lis)-1-i):
            if lis[j] > lis[j+1]:
                lis[j],lis[j+1] = lis[j+1],lis[j]
                
    return lis


print(sortport(lis1))