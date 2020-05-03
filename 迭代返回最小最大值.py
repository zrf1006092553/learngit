#!/usr/bin/python
# -*- coding: utf-8 -*-


for n in 'ABCD':
     print(n)

for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)

def findMinAndMax(L):
    
    if len(L) == 0:
        print(None, None)
        return (None, None)
    elif len(L) == 1:
        print(L[0], L[0])
        return (L[0], L[0])
    elif len(L) > 1:
        maxL = L[0]
        minL = L[0]
        for x in L:
            if x >= maxL:
                maxL = x
            if x <= minL:
                minL = x
        print(minL, maxL)
        return (minL, maxL)
    else:
        print('INPUT ERROR')
        

    
# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!' )
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!' )
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!' )
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!' )
else:
    print('测试成功!')