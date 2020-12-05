# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 00:29:56 2019

@author: LOVESS
"""

import pyautogui #鍵盤滑鼠的操作
import snp
import time
pyautogui.FAILSAFE = True

pyautogui.PAUSE = 1  #太快無法執行
pyautogui.hotkey('win','r')
pyautogui.press('shift') #如果會卡中文輸入法的
pyautogui.typewrite('chrome',0.1)
pyautogui.press('enter')

pyautogui.PAUSE = 1  #太快無法執行
loc = snp.locateOnScreen('ENGLISH.png',region=(1184,732,19,31),threshold=0.9) 
if loc == None:
    pyautogui.press('shift') #如果會卡中文輸入法的
    
pyautogui.typewrite('https://gamekuo.com/html5/3963_math-genius-games',0.1)

loc = snp.locateOnScreen('winup.png',region=(1278,6,36,18)) 
if loc == None:
    pyautogui.click(1335,67)
#pyautogui.hotkey('win','up') #視窗最大化
    
pyautogui.press('enter')
pyautogui.PAUSE = 1  #太快無法執行


pyautogui.moveTo(739,462) #滑鼠移到適當位置進行滾動
pyautogui.scroll(-200) #正:向上滾動,負:向下滾動

times=3
for i in range(times):
    print(i)
    pyautogui.moveTo(739,462) #滑鼠移到適當位置
    loc_i = snp.locateOnScreen('skip_ad.PNG',region=(760,577,105,48))       # 偵測螢幕上是否有與 skip_ad.PNG 相同的圖片，若有 loc 將會被指派相同於圖片的地方的位置，若沒有 loc 會被指派為 None
    
    start=time.time()
    
    while loc_i == None:                              # 如果 loc 是 None (剛剛螢幕上沒找到相同的圖片) / 如果有找到，會直接跳過這個迴圈
        time.sleep(0.1)                             # 停 0.1 秒
        loc_i =snp.locateOnScreen('skip_ad.PNG',region=(760,577,105,48))   # 再找一次
        '''duration=time.time()-start
        if duration >5:
            break'''   
    
    center = pyautogui.center(loc_i)
    pyautogui.PAUSE = 1 
    pyautogui.click(center)
    
    
    
    loc_play_i =snp.locateOnScreen('Play.PNG')#,region=(435,404,260,85))       # 偵測螢幕上是否有與 Play.PNG 相同的圖片，若有 loc 將會被指派相同於圖片的地方的位置，若沒有 loc 會被指派為 None
    
    while loc_play_i == None:                              # 如果 loc 是 None (剛剛螢幕上沒找到相同的圖片) / 如果有找到，會直接跳過這個迴圈
        time.sleep(0.1)                             # 停 0.1 秒
        loc_play_i = snp.locateOnScreen('Play.PNG')#,region=(435,404,260,85))   # 再找一次
    
    center = pyautogui.center(loc_play_i)
    pyautogui.PAUSE = 1 
    pyautogui.click(center)
    
    
    def identify_pic(region=None):
        
        
        loc = snp.locateOnScreen('0.png',region=region,threshold=0.9) 
        num=0
        if loc ==None:
            loc = snp.locateOnScreen('1.png',region=region,threshold=0.5)
            num=1
        if loc ==None:
            loc = snp.locateOnScreen('2.png',region=region,threshold=0.8)
            num=2
        if loc ==None:
            loc = snp.locateOnScreen('8.png',region=region,threshold=0.8)
            num=8
        if loc ==None:
            loc = snp.locateOnScreen('3.png',region=region,threshold=0.7)
            num=3
        if loc ==None:
            loc = snp.locateOnScreen('4.png',region=region,threshold=0.5)
            num=4
        if loc ==None:
            loc = snp.locateOnScreen('5.png',region=region,threshold=0.8)
            num=5
        if loc ==None:
            loc = snp.locateOnScreen('6.png',region=region,threshold=0.8)
            num=6
        if loc ==None:
            loc = snp.locateOnScreen('7.png',region=region,threshold=0.7)
            num=7
        
        if loc ==None:
            loc = snp.locateOnScreen('9.png',region=region,threshold=0.8)
            num=9
        if loc == None:
            num=0   #沒有數字
                
        return loc,num
    
    
    while(True): #開始作答
        loc_gg=snp.locateOnScreen('gg.png',region=(476,247,79,34),threshold=0.9) #結果出來就停止作答
        if loc_gg != None:
            break
    
    
        #第一組數字
        loc_11= identify_pic(region=(354,265,25,47))  #1.1左上 (354,265)右下  (x=379, y=312)
        #print(loc_11)
        if loc_11[0]!=None:
                num_11=loc_11[1]*10 #十位數
                #print(num_11)
        else:
            num_11=0
                
        loc_12= identify_pic(region=(390,265,25,47))  #1.2左上(x=390, y=265)右下 (x=425, y=311)
        #print(loc_12)
        num_12=loc_12[1]
        #print(num_12)
        num_1=num_11+num_12
        
        #第二組數字
        loc_2= identify_pic(region=(577,265,25,47))  #2左上(x=577, y=265)右下 (x=613, y=315)


        #print(loc_2)
        num_2=loc_2[1]
              
        #第三組數字 
        loc_32 = identify_pic(region=(758,265,25,47))    #3.2左上(x=758, y=265)右下 (x=795, y=314)
        #print(loc_32)
        if loc_32[0]!=None:
            num_32=loc_32[1]
            #print(num_32)
        else:
            num_32=0
        
        loc_31= identify_pic(region=(722,266,25,47))   #3.1左上(x=722, y=266)右下 (x=751, y=315)
        #print(loc_31)
        if loc_32[0] !=None:
            num_31=loc_31[1]*10 #十位數
            #print(num_31)
        else:
            num_31=loc_31[1]
        
        num_3=num_31+num_32
        
        print(num_1,num_2,num_3) #第一組數字+ #第二組數字+  #第三組數字
        
          
        #加減乘除
        if num_1==2:        #特殊情況
            if num_2==2:
                loc = snp.locateOnScreen('Plus.PNG',region=(288,400,200,100))      
        
                while loc == None:                             
                    time.sleep(0.1)                            
                    loc = snp.locateOnScreen('Plus.PNG')   
        
                center = pyautogui.center(loc)
                pyautogui.PAUSE = 1 
                pyautogui.click(center)
                
        if num_1<num_3:          #被除數<等號右邊的數字 (+ *)
            plus=num_1+num_2
            multiple=num_1*num_2
            if plus==num_3:
                
                loc = snp.locateOnScreen('Plus.PNG',region=(288,400,200,100))      
        
                while loc == None:                             
                    time.sleep(0.1)                            
                    loc = snp.locateOnScreen('Plus.PNG')   
        
                center = pyautogui.center(loc)
                pyautogui.PAUSE = 1 
                pyautogui.click(center)
            
            if multiple==num_3:
                loc = loc = snp.locateOnScreen('Multiple.PNG',region=(509,401,200,100))     
        
                while loc == None:                             
                    time.sleep(0.1)                            
                    loc = snp.locateOnScreen('Multiple.PNG')   
        
                center = pyautogui.center(loc)
                pyautogui.PAUSE = 1 
                pyautogui.click(center)
          
        if num_1==num_3:    #被除數=等號右邊的數字
             loc = loc = snp.locateOnScreen('Multiple.PNG',region=(509,401,199,95))
             
             while loc == None:                             
                    time.sleep(0.1)                            
                    loc = snp.locateOnScreen('Multiple.PNG') 
             
             center = pyautogui.center(loc)
             pyautogui.PAUSE = 1 
             pyautogui.click(center)
        
      
        if num_1>num_3:    #被除數>等號右邊的數字
            minus=num_1-num_2
            if num_2 != 0:
                ratio=num_1/num_2 #排除除數是0
           
            if minus==num_3:
                loc = snp.locateOnScreen('Minus.PNG',region=(399,402,199,95))    
        
                while loc == None:                             
                    time.sleep(0.1)                            
                    loc = snp.locateOnScreen('Minus.PNG')   
        
                center = pyautogui.center(loc)
                pyautogui.PAUSE = 1 
                pyautogui.click(center)
            
            if ratio==num_3:
                loc = snp.locateOnScreen('Ratio.PNG',region=(617,402,199,95))     
        
                while loc == None:                             
                    time.sleep(0.1)                            
                    loc = snp.locateOnScreen('Ratio.PNG')   
        
                center = pyautogui.center(loc)
                pyautogui.PAUSE = 1 
                pyautogui.click(center)
            
            if num_2 ==0:
                loc = loc = snp.locateOnScreen('Multiple.PNG',region=(509,401,199,95))
             
                while loc == None:                             
                        time.sleep(0.1)                            
                        loc = snp.locateOnScreen('Multiple.PNG') 
                 
                center = pyautogui.center(loc)
                pyautogui.PAUSE = 1 
                pyautogui.click(center)
    
    if i < 2:
        pyautogui.click(82,53) #f4重新載入




