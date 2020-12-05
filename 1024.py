# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 13:33:35 2019

@author: LOVESS
"""

import pyautogui, time
##先打開 failsafe 滑鼠到左上角可以直接停
pyautogui.FAILSAFE = True

#等待道出線某圖片為止(method 2)
def wait_until(pic):
    loc=pyautogui.locateOnScreen(pic)
    while loc==None:
        time.sleep(0.1)       # 停 0.1 秒
        t = time.time() 
        loc = pyautogui.locateOnScreen(pic)                     
        #loc = pyautogui.locateOnScreen('box.png')  # 再找一次
        print(time.time()-t) #現在時間-前面時間


##不用加路徑,因為box和spyder一樣位置(找同個目錄下的box.png)(建議套件目錄都放在同黨按下)
loc = pyautogui.locateOnScreen('box.png')       # 偵測螢幕上是否有與 box.png 相同的圖片，若有 loc 將會被指派相同於圖片的地方的位置，若沒有 loc 會被指派為 None

"""while loc == None:                              # 如果 loc 是 None (剛剛螢幕上沒找到相同的圖片) / 如果有找到，會直接跳過這個迴圈
    time.sleep(0.1)                             # 停 0.1 秒
    loc = pyautogui.locateOnScreen('box.png')   # 再找一次

for loc_i in pyautogui.locateAllOnScreen('box.png'):
    print(loc_i)
    center = pyautogui.center(loc_i)
  pyautogui.click(center) """
  
wait_until ('box.png') #method2
for loc_i in pyautogui.locateAllOnScreen('box.png'):
      print(loc_i)
      center = pyautogui.center(loc_i)
      pyautogui.click(center)
    
      
      
      
      
      