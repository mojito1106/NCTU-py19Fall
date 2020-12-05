# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 13:57:21 2019

@author: LOVESS
"""

#1212pic德州poker

'''
from iterpool ...
cnt=0 #計數器歸零
cnt=cnt+1
print(cnt)

'''

'''
import telegram_send
telegram_send.configure("c:/test.conf") #創一個可以放token和文字的檔
#放完token之後就可以可以拿到一組數字,然後就可以透過python開始傳送訊息(當聊天機器人)
'''
import webbrowser, json
with open('C:/Users/LOVESS/Downloads/animal.json',encoding='utf8') as a_json:
    content = json.load(a_json)
cnt = 0
for data in content:
    if not data.get('animal_colour'): continue
    if not data.get('animal_kind'): continue
    if not data.get('album_file'): continue
    if data['animal_colour'] == '黑色' and data['animal_kind'] == '狗':
        webbrowser.open(data['album_file'])
        cnt += 1
    if cnt >= 5: break #開出最多五個圖檔之後就會解鎖












