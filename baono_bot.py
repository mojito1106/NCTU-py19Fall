# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 14:43:23 2019

@author: LOVESS
"""

#聊天機器人->字串處理
#1205pic
#交談指令玩遊戲
from telegram.ext import Updater, CommandHandler
import telegram_send

def hello(bot, update):
    update.message.reply_text(
        'hello, {}'.format(update.message.from_user.first_name))

def bts(bot,update):
    with open ("C:/bts.png","rb")as f:
        telegram_send.send(images=[f])
        
        
def bye(bot,update):
    update.message.reply_text(
        '{} ,bye!'.format(update.message.from_user.first_name))
    
def show_text(bot,update):
    text=update.message.text
    print('We received:')
    print(text)
    update.message.reply_text(
            'Echo:{}'.format(text))
updater = Updater('894035266:AAHADlXGLPrBEa28Ruz5KlZz-cEtpP2N5pc')
'''
with open('C:/Users/LOVESS/Desktop/py/token.txt') as FILE:
    token =FILE.readline()
updater = Updater('token')
updater = Updater('my token')
'''
updater.dispatcher.add_handler(CommandHandler('hello', hello))#若收到一個hello指令,就執行hello f.
updater.dispatcher.add_handler(CommandHandler('bye', bye))
updater.dispatcher.add_handler(CommandHandler('content', show_text))
updater.dispatcher.add_handler(CommandHandler('bts', bts))

updater.start_polling()
updater.idle() #idle發呆

#去除頭尾的空白strip(講義有))
#切割字串split