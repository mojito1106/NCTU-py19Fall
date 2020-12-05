# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 13:33:08 2019

@author: LOVESS
"""

#RANDOM隨機的成分,增加可玩性
#import random
'''
#
random.randint(1,7)
Out[2]: 3
'''
#/////////////////////////////////////////////////////////////////
'''
#
import random
cnt=[0,0,0,0,0,0,0]
for i in range (50000):
    result = random.randint(1,6)
    cnt[result] = cnt[result]+1
    print (cnt)
    
#
#random.shuffle 隨機洗牌
lst=[x+y for x in 'ASHK' for y in '123456789TJQK'] #把x+y交出去

random.shuffle(lst)
print (lst)
'''
#hand手牌)

#sample一次全部拿出來
#手機照片
#//////////////////////////////////////////////////////////////////
'''
# Read an integer which is in {0,...,9}
def read_a_digit():
    ret = -1
    while True:
        try:
            ret = int(input('Input a digit: '))
        except ValueError:
            print('Not an integer')
            continue
        if ret >= 0 and ret <= 9:
            return ret
        print(ret,'is not in {0,...,9}.')

from random import randint #隨機抽一個整數

ans = randint(0,9) #隨機抽0~9

guess = read_a_digit()
while guess != ans:
    print(guess,'is not the answer')
    guess = read_a_digit()

print('Congrats! The answer is',ans)
#Guess a secret number from 0 to 9 with hints
#Sample code
# Read an integer which is in {0,...,9}
def read_a_digit():
    ret = -1
    while True:
        try:
            ret = int(input('Input a digit: '))
        except ValueError:
            print('Not an integer')
            continue
        if ret >= 0 and ret <= 9:
            return ret
        print(ret,'is not in {0,...,9}.')

from random import randint

ans = randint(0,9)

guess = read_a_digit()
while guess != ans:
    if ans < guess:
        print(guess,'is greater than the answer.')
    else:
        print(guess,'is less than the answer.')
    guess = read_a_digit()

print('Congrats! The answer is',ans)
 
'''
#////////////////////////////////////////////////////////////////////
'''
from random import sample
from itertools import combinations

# Check whether a input is valid
def valid(s):
    if len(s)!=4:
        return False
    if any(x not in '0123456789' for x in s):
        return False
    if any(x==y for x, y in combinations(s,2)): #檢查是否兩兩相同(兩個一組x+y兩個一組x+y拿出來檢查)
        return False
    return True

# Read string which has four distinct digits
def read_four_distinct_digits():
    while True:
        ret = input('Input four distinct digits: ')
        if valid(ret):          #檢查輸入是否合法
            return ret
        print(ret,'is not valid.')

ans = ''.join(sample('0123456789',4))

guess = read_four_distinct_digits()
while guess != ans:
    A = sum(1 for x,y in zip(guess,ans) if x==y) #zip從guess和ans一個一個拿出來比對 x==y?,是的話就交出去
    B = sum(1 for x in guess if x in ans)-A #沒出現在正確位置上,但有猜到(加總起來,但是要扣掉在對的位置上的那些)
    print(guess,'is {}A{}B.'.format(A,B))
    guess = read_four_distinct_digits()

print('Congrats! The answer is',ans)



'''


#//////////////////////////////////////////////////////////////////////
'''
from itertools import permutations
import random
cand=[''.join(x) for x in permutations('0123456789',4)]

def nAnB(guess,ans):
    A = sum(1 for x,y in zip(guess,ans) if x==y)
    B = sum(1 for x in guess if x in ans)-A
    return '{}A{}B.'.format(A,B)
    
#nAnB('2345','2749')
#Out[41]: '2A0B.'
#手機cmd
def nextcnd(cand,guess,result):
    ret=[ans for ans in cand if result==nAnB(guess,ans)]
    return ret

while len(cand)>0:
    print('size of' ,cand,'is',len(cand))
    print('suggestion:',random.choice(cand))
    guess=input('guess:')
    result=input('result:')
    cand =nextcnd(cand,guess,result)
'''
#////////////////////////////////////////////////////////////////////////////
'''
tuple=(12,3,4,None,'string',print) 
tuple[-1]=5566 不能直接修改標籤
list=[...] list就可以直接修改標籤

5*[55,66]
Out[42]: [55, 66, 55, 66, 55, 66, 55, 66, 55, 66]

a=[0,1,2,3,4]

a.pop(2)
Out[44]: 2

a
Out[45]: [0, 1, 3, 4]

a.remove(0)

a
Out[47]: [1, 3, 4]

a.reverse()

a
Out[53]: [4, 3, 1]

 a.append(2)

a
Out[55]: [4, 3, 1, 2]

b=[7,6,5]
b.sort()

b
Out[51]: [5, 6, 7]
'''

#a,b mutable 把他們貼到ilist,

#c=cpoy.deepcopy(a) 深層拷貝








