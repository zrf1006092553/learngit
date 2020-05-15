#!/usr/bin/python
# -*- coding: utf-8 -*-

def calsum(*args):
    ax = 0
    for n in args:
        ax = ax + n 
    return ax
    
def lazysum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n 
        return ax
    return sum 
#我们在函数lazy_sum中又定义了函数sum，并且，内部函数sum可以引用外部函数
#lazy_sum的参数和局部变量，当lazy_sum返回函数sum时，相关参数和变量都保存在返
#回的函数中，这种称为“闭包（Closure）”的程序结构拥有极大的威力
L = [1, 2, 3, 6, 4, 5]
f = lazysum(L)
print(f)
#当我们调用lazy_sum()时，每次调用都会返回一个新的函数，即使传入相同的参数：
   
f1 = lazysum(1, 2)
f2 = lazysum(1, 2)
print(f1 == f2) #每次返回的不一样 可理解为返回一个新的函数
 
#闭包 
def count():
    fa = []
    for i in range(1, 4):
        def f():
            return i * i    #这里引用了变量i
        fa.append(f)    #等到三个函数全返回时i=3 结果同时为9
    return fa
    
f1, f2, f3 = count()    
print(f1(), f2(), f3())
#####返回函数不要引用任何循环变量，或者后续会发生变化的变量。
#！！！！！#改进方法，在创建一个函数，参数绑定循环变量当前的值
def count1():
    def f(j):
        def g():    #这里用g（）函数的返回参数解决了变量j*j的问题 
            return j * j 
        return g 
        
    fs = []
    for i in range(1, 4):
        fs.append(f(i))
    return fs
    
f4, f5, f6 = count1()
print(f4(), f5(), f6())


#####利用闭包返回一个计数器函数，每次调用它返回递增整数：

# -*- coding: utf-8 -*-

def createCounter():
    j = 0
    def counter():
        nonlocal j  #当内部作用域想修改外部作用域的变量时，
        #就要用到global和nonlocal关键字了。
        j += 1
        return j
    return counter

# 测试:
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')


   
   
   
    