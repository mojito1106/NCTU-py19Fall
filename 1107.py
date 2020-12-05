# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 13:41:50 2019

@author: LOVESS
"""


'''
#1

def squares(n):
    for i in range(n+1):
        yield i**2

print('squares is',type(squares))
print('squares(5) is',type(squares(5)))
for i in squares(5):
    print(i)
    
#有for要來generator拿東西，執行到yield就會把東西拿出去(有yield就是generator) 

#2
def f():      #定義但卻沒有執行
    print('1st time')
    yield 1
    print('2nd time') #從上次yield過的地方往下執行
    yield 2
    print('3rd time')
    yield 3
    print('4th time')
    return 5    #結束程式碼，表示拿不到東西

for i in f(): #開始執行
    print(i) #拿不到東西可以貼，迴圈就會結束 
    

#3
def primes(n):
    print("primes(" ,n, ")")
    if n < 2:
        return
    n_is_prime = True
    for i in primes(n-1):
        yield i
        if n % i == 0:
            n_is_prime = False
    if n_is_prime:
        yield n

for i in primes(5): #把小於5的質數印出來
    print(i)
'''



#4
def merge(a, b):
    it_a, it_b = iter(a), iter(b)
    item_a = next(it_a,None)
    item_b = next(it_b,None)
    while item_a != None and item_b != None:
        if item_a <= item_b:
            yield item_a
            item_a = next(it_a,None)
        else:
            yield item_b
            item_b = next(it_b,None)
    if item_a != None: yield item_a
    if item_b != None: yield item_b
    for item in it_a: yield item
    for item in it_b: yield item

def mergesort(a):
    L = len(a)
    if L<=1:
        for x in a:
            yield x
        return
    for x in merge(mergesort(a[:L//2]),mergesort(a[L//2:])):
        yield x

print('merge',[1,3,5,6],'and',[2,4,7,8])
for item in merge([1,3,5,6],[2,4,7,8]):
    print(item)

print()
print('mergesort',[1,5,2,4,3,8,7,6])
for item in mergesort([1,5,2,4,3,8,7,6]):
    print(item)





