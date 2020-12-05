# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 15:53:00 2019

@author: LOVESS
"""
import pyautogui, time

color =None

def report():
    #global color #改法一:加這一行，因為要修改全域變數，但盡量避免在f裡面改全域變數
    loc= pyautogui.position()
    local_color=pyautogui.screenshot().getpixel(loc)
    print("position is :",loc,"color is",local_color)
    return local_color,loc #改法二,直接回傳

while True:
    color,_=report()
    time.sleep(0.5)
    if color ==(139,0,0):
        break


def squares(n):
    for i in range(n+1):
        yield i**2
        yield 'poo'
    yield 123
    yield 'poop'
    pyautogui.moveTo(500,500,10)#移到500,500花10秒
    yield 'done'

print('squares is',type(squares))
print('squares() is',type(squares(5)))
for i in squares(5):
    print(i)