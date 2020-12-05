# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 14:36:40 2019

@author: LOVESS
"""

import time
import pyautogui
import snp

from pyautogui import screenshot

def report_time():
    t = time.time()
    left, top, width, height = 5, 66, 77, 8
    screenshot(region=(left,top,width,height))
    print(time.time()-t)

for i in range(100):
    report_time()
    
    