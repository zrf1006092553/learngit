#!/usr/bin/python
# -*- coding: utf-8 -*-


#()   []变成generator
L = (x * x for x in range(10))

print(L)
print(next(L))
print(next(L))

#一般不用next调用

for n in L:
    print(n)
    
    
#斐波拉契数列 print is easy
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'
    
print(fib(5))


#这就是定义generator的另一种方法。
#如果一个函数定义中包含yield关键字，
#那么这个函数就不再是一个普通函数，而是一个generator：
def fib2(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

print(fib2(max))

#这里，最难理解的就是generator和函数的执行流程不一样。
#函数是顺序执行，遇到return语句或者最后一行函数语句就返回。
#而变成generator的函数，在每次调用next()的时候执行，
#遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。

def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield (2)
    print('step 3')
    yield (5)
#调用该generator时，首先要生成一个generator对象，
#然后用next()函数不断获得下一个返回值：yiels处执行
o = odd()
print(next(o))
print(next(o))
print(next(o))

#执行3次yield后，
#已经没有yield可以执行了，所以，第4次调用next(o)就报错。
#把函数改成generator后，我们基本上从来不会用next()来获取下一个返回值，
#而是直接使用for循环来迭代：
for n in fib(6):
    print(n)
#但是用for循环调用generator时，
#发现拿不到generator的return语句的返回值。
#如果想要拿到返回值，必须捕获StopIteration错误，
#返回值包含在StopIteration的value中：

    
# -*- coding: utf-8 -*-杨辉三角
#  source:https://blog.csdn.net/qq_37701443/article/details/82707526?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromBaidu-1&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromBaidu-1
def triangles():
    p = [1]
    while True:
        yield p
        p = [1] + [p[i] + p[i + 1] for i in range(len(p) - 1)] + [1]



# 期待输出:
# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
# [1, 5, 10, 10, 5, 1]
# [1, 6, 15, 20, 15, 6, 1]
# [1, 7, 21, 35, 35, 21, 7, 1]
# [1, 8, 28, 56, 70, 56, 28, 8, 1]
# [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
n = 0
results = []
for t in triangles():
    results.append(t)
    n = n + 1
    if n == 10:
        break

for t in results:
    print(t)

if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')    
    

#Python的for循环本质上就是通过不断调用next()函数实现的，例如：

for x in [1, 2, 3, 4, 5]:
    pass
#实际上完全等价于：

# 首先获得Iterator对象:
it = iter([1, 2, 3, 4, 5])
# 循环:
while True:
    try:
        # 获得下一个值:
        x = next(it)
    except StopIteration:
        # 遇到StopIteration就退出循环
        break



