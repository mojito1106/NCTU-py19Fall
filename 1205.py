# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 13:33:32 2019

@author: LOVESS
"""

a=[0]*10**7
a[9899]='今天好冷又下雨'
a[9944]='x8 x8 x8 '
for item in a:
    if item!=0:
        print(item)
    
a={} #沒放東西

temp={'台北市':'15-16','高雄市':'16-17'}
print(temp['台北市'])

square_to_cubic={x**2:x**3 for x in range(0,21)} #only 0~20
print(square_to_cubic)

#dict 可以移除標籤(沒有順序的概念) del
#list 也可以移除標籤(但是後面的標籤會往前補)

del square_to_cubic[400]
print(square_to_cubic)

i={'name':'mz','heigh':189,'weight':112,'age':21} #只會印key,不會印value
for j in i :
    print(j)
for j in i.values() :
    print(j)
for k in i.items() :
    print(k)

'''    
#console
print(i.get('married'))
None   
'''

some_list = [0,3,5,7,1,2,1,2,1]
counter = {}
for x in some_list:
    if x not in counter.keys():
        counter[x] = 0
    else:
        counter[x] =counter[x]+ 1
print(counter)    
    
#輸出:{0: 0, 3: 0, 5: 0, 7: 0, 1: 2, 2: 1} #怪怪的!!!數字應該要和下面的一樣

some_list = [0,3,5,7,1,2,1,2,1]
counter = {}
for x in some_list:
    counter.setdefault(x,0)
    counter[x] += 1
print(counter)    
#輸出:{0: 1, 3: 1, 5: 1, 7: 1, 1: 3, 2: 2}

    
    
    
    
    
    
    
    
    
    
    
    