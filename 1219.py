# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 13:42:30 2019

@author: LOVESS
"""

from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("http://www.nctu.edu.tw/")
assert "NCTU 國立交通大學" in driver.title
student =driver.find_element_by_id("/html/body/div[2]/nav/div[1]/div[1]/ul/li[1]/a")
student.click()
sleep(5)
#driver.close()


'''
driver = webdriver.Chrome()
driver.get("http://www.nctu.edu.tw/")
assert "NCTU 國立交通大學" in driver.title
student =driver.find_element_by_id("#groupNav > div > ul:nth-child(1) > li.item-511 > a")
student.click()
sleep(5)
'''
#a=driver.find_element_by_css_selector('//*[@id="divMaskFrame"] ')
#右鍵->copy->copy xpath
#F12開發人員工具
#要去找瀏覽器的driver,所以drive.
#iphone mw 5:57


#**小提醒：在跑之前要先關掉開發人員
#截圖
#text = driver.find_element_by_css_selector("#modRandomArticle138 > div > div.title > h4")
#text.screenshot_as_png
#text.screenshot("C:\Users\LOVESS/tmp.png")
#Out[30]: True
