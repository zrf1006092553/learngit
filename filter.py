#!/usr/bin/python
# -*- coding: utf-8 -*-

#filter()把传入的函数依次作用于每个元素，
#然后根据返回值是True还是False决定保留还是丢弃该元素。

def isodd(n):
    return n % 2 == 1
def iseven(n):
    return n % 2 == 0
    
L1 = [1, 5, 6, 9, 7, 89, 12]
print(list(filter(isodd, L1)))
print(list(filter(iseven, L1)))


L2 = ['A', 'B', '', None, 'C', '   ']
###!!!!!把序列中的空字符串删除！！！
def notempty(s):
    return s and s.strip()
    
#str = "00000003210Runoob01230000000"; 
#print str.strip( '0' );  # 去除首尾字符 0
#str2 = "   Runoob      ";   # 去除首尾空格
#print str2.strip();
  #注意到filter()函数返回的是一个Iterator，也就是一个惰性序列，所以要强迫filter()
  #完成计算结果，需要用list()函数获得所有结果并返回list。 
print(list(filter(notempty, L2)))
    
#example 生成素数
def odditer():
    n = 1
    while True:
        n = n + 1
        yield n 
        

def notdivisible(n):
    return lambda x: x % n > 0 

def primes():
    yield 2 
    it = odditer()  #初始序列
    while True:
        n = next(it)    #返回序列第一个数
        yield n 
        it = filter(notdivisible(n), it)    #构造新序列

for n in primes():
    if n < 50:
        print(n)
    else:
        break
    
 ## -*- coding: utf-8 -*-
##回数是指从左向右读和从右向左读都是一样的数，
#例如12321，909。请利用filter()筛选出回数：
def is_palindrome(n):
        return str(n) == str(n)[::-1]
#确定是回数 则直接返回强转str（n）
# 测试:
output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')  
    

    
