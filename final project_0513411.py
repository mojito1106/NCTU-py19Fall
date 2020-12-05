# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 12:25:15 2019

@author: LOVESS
"""

#聊天機器人->字串處理
#1205pic
#交談指令玩遊戲
import telegram_send
import requests

from telegram.ext import Updater, CommandHandler

from selenium import webdriver
#driver = webdriver.Chrome()
import random

def nctu(bot, update):
    driver = webdriver.Chrome()
    driver.get("http://www.nctu.edu.tw/")
    assert "NCTU 國立交通大學" in driver.title
    title = driver.find_element_by_xpath("/html/body/div[2]/nav/div[1]/div[3]/div/div/div[1]/h4")
    news = driver.find_element_by_xpath("/html/body/div[2]/nav/div[1]/div[3]/div/div/div[2]")
    ref = driver.find_element_by_xpath("/html/body/div[2]/nav/div[1]/div[3]/div/div/div[3]/a")
    r = ref.get_property('href')
    #/html/body/div[2]/nav/div[1]/div[3]/div/div/div[1]/h4 標題
    #/html/body/div[2]/nav/div[1]/div[3]/div/div/div[2] 最新消息內容
    #/html/body/div[2]/nav/div[1]/div[3]/div/div/div[3]/a 連結
    t=title.text
    n=news.text
    #rt=r.text
    #sleep(5)
    update.message.reply_text(
        '交大首頁最新內容：「{}」\n {}\n {}'.format(t,n,r))
        
def weather(bot,update):
    driver = webdriver.Chrome()
    driver.get("https://weather.com/weather/tenday/l/f41314da689d72f081fa70aeb4835781cd2f6c9cacad8b744a9bc972fde5b1f6")
    
    one_high_temp = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[11]/div/main/region/div[3]/div/section/div/table/tbody/tr[1]/td[4]/div/span[1]")
    one_low_temp = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[11]/div/main/region/div[3]/div/section/div/table/tbody/tr[1]/td[4]/div/span[3]")
    one_rain_per =driver.find_element_by_xpath("/html/body/div[1]/div/div/div[11]/div/main/region/div[3]/div/section/div/table/tbody/tr[1]/td[5]/div/span[2]/span")
    one_humidity =driver.find_element_by_xpath("/html/body/div[1]/div/div/div[11]/div/main/region/div[3]/div/section/div/table/tbody/tr[1]/td[7]/span/span")
    #one_high_t=one_high_temp.text
    #one_low_t=one_low_temp.text
    one_high_tf = int((one_high_temp.text.split('°'))[0])
    one_low_tf = int((one_low_temp.text.split('°'))[0]) #['61', '']矩陣的型態,取出華氏的職
    one_high_t = int((one_high_tf-32)*5/9) #華氏轉攝氏
    one_low_t = int((one_low_tf-32)*5/9) #華氏轉攝氏
    #print (one_low_t,one_high_t)
    one_rain=one_rain_per.text
    one_h=one_humidity.text
    
    two_high_temp = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[11]/div/main/region/div[3]/div/section/div/table/tbody/tr[2]/td[4]/div/span[1]")
    two_low_temp = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[11]/div/main/region/div[3]/div/section/div/table/tbody/tr[2]/td[4]/div/span[3]")
    two_rain_per =driver.find_element_by_xpath("/html/body/div[1]/div/div/div[11]/div/main/region/div[3]/div/section/div/table/tbody/tr[2]/td[5]/div/span[2]/span")
    two_humidity =driver.find_element_by_xpath("/html/body/div[1]/div/div/div[11]/div/main/region/div[3]/div/section/div/table/tbody/tr[2]/td[7]/span/span")
    #two_high_t=two_high_temp.text
    #two_low_t=two_low_temp.text
    two_high_tf = int((two_high_temp.text.split('°'))[0])
    two_low_tf = int((two_low_temp.text.split('°'))[0]) #['61', '']矩陣的型態,取出華氏的職
    two_high_t = int((two_high_tf-32)*5/9) #華氏轉攝氏
    two_low_t = int((two_low_tf-32)*5/9) #華氏轉攝氏
    two_rain=two_rain_per.text
    two_h=two_humidity.text                       
                                               
    three_high_temp = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[11]/div/main/region/div[3]/div/section/div/table/tbody/tr[3]/td[4]/div/span[1]")
    three_low_temp = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[11]/div/main/region/div[3]/div/section/div/table/tbody/tr[3]/td[4]/div/span[3]")
    three_rain_per =driver.find_element_by_xpath("/html/body/div[1]/div/div/div[11]/div/main/region/div[3]/div/section/div/table/tbody/tr[3]/td[5]/div/span[2]/span")
    three_humidity =driver.find_element_by_xpath("/html/body/div[1]/div/div/div[11]/div/main/region/div[3]/div/section/div/table/tbody/tr[3]/td[7]/span/span")
    #three_high_t=three_high_temp.text
    #three_low_t=three_low_temp.text
    three_high_tf = int((three_high_temp.text.split('°'))[0])
    three_low_tf = int((three_low_temp.text.split('°'))[0]) #['61', '']矩陣的型態,取出華氏的職
    three_high_t = int((three_high_tf-32)*5/9) #華氏轉攝氏
    three_low_t = int((three_low_tf-32)*5/9) #華氏轉攝氏
    three_rain=three_rain_per.text
    three_h=three_humidity.text 
    
   
    
    
    update.message.reply_text(
        '新竹今天氣溫 最高：{}°C 最低：{}°C 降雨機率：{} 濕度：{}'.format(one_high_t,one_low_t,one_rain,one_h))
    update.message.reply_text(
        '新竹明天氣溫 最高：{}°C 最低：{}°C 降雨機率：{} 濕度：{}'.format(two_high_t,two_low_t,two_rain,two_h))
    update.message.reply_text(
        '新竹後天氣溫 最高：{}°C 最低：{}°C 降雨機率：{} 濕度：{}'.format(three_high_t,three_low_t,three_rain,three_h))
    
def news(bot, update):
    driver = webdriver.Chrome()
    driver.get("https://www.chinatimes.com/realtimenews/?page=3&chdtv")
    title = driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/section/ul/li[1]/div/div/div/h3/a")
    news = driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/section/ul/li[1]/div/div/div/p")
    ref = driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/section/ul/li[1]/div/div/div/h3/a")
    r = ref.get_property('href')
    t=title.text
    n=news.text
    #rt=r.text
    #sleep(5)
    update.message.reply_text(
        '即時新聞：「{}」\n {}\n {}'.format(t,n,r))

def search(bot,update):
    queryStr=update.message.text
    new_queryStr=queryStr.replace("/search "," ")
    driver = webdriver.Chrome()
    url = 'https://www.google.com.tw/search?hl=zh&q=%s' % new_queryStr
    driver.get(url)
    title = driver.find_element_by_xpath('//*[@id="rso"]/div/div/div[1]/div/div/div[1]/a/h3')
    ref = driver.find_element_by_xpath('//*[@id="rso"]/div/div/div[1]/div/div/div[1]/a')
    #title = driver.find_element_by_xpath('/html/body/div[7]/div[3]/div[10]/div[1]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div/div[1]/a/h3')
    #ref = driver.find_element_by_xpath('/html/body/div[7]/div[3]/div[10]/div[1]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div/div[1]')
    t=title.text
    r = ref.get_property('href')
    
    update.message.reply_text('標題：{}\n連結：{}'.format(t,r))


def custom(bot,update):
    driver = webdriver.Chrome()
    driver.get("https://zh.wikipedia.org/zh-tw/%E9%98%B2%E5%BD%88%E5%B0%91%E5%B9%B4%E5%9C%98")
    cond = driver.find_elements_by_tag_name('img')
    cond[0].get_attribute('src')
    
    def url_to_file(url,filename):
            result = requests.get(url)
            result.raise_for_status()
            with open (filename,'wb') as FILE:
                for chunk in result.iter_content(102400):
                    FILE.write(chunk)
    temp = [] #建制空陣列
    for i ,img in enumerate(cond):   #找出全部
        subname = img.get_attribute('src').split('.')[-1]
        if (subname=='jpg'):
            url_to_file(img.get_attribute('src'),'C:/Users/LOVESS/Desktop/bts/{}.{}'.format(i+1,subname))
            temp.append(i+1)
    print(temp)
    num = random.choice(temp)
    print(num)
    with open ("C:/Users/LOVESS/Desktop/bts/{}.jpg".format(num),"rb")as f: #要讓他有隨機的
        telegram_send.send(images=[f])
    

updater = Updater('894035266:AAHADlXGLPrBEa28Ruz5KlZz-cEtpP2N5pc')

updater.dispatcher.add_handler(CommandHandler('nctu', nctu))#若收到一個nctu指令,就執行nctu f.
updater.dispatcher.add_handler(CommandHandler('weather', weather))
updater.dispatcher.add_handler(CommandHandler('news', news))
updater.dispatcher.add_handler(CommandHandler('search', search))
updater.dispatcher.add_handler(CommandHandler('custom', custom))

updater.start_polling()
updater.idle() #idle發呆

#去除頭尾的空白strip(講義有))
#切割字串split