import jieba
import time  # 引入time模块
import datetime
from random import *
import requests
from bs4 import BeautifulSoup
import os

# ------ robot --------- #
import RPi.GPIO as GPIO
import time
from playsound import playsound
# ------ robot --------- #

#------- thread ---------#
import threading
import time
#------- thread ---------#

def get_web_page(url):
	resp = requests.get(url=url)
	resp.encoding = 'big-5'
	return resp.text

def weather():
	print('天氣 func')
	page = get_web_page('https://www.cwb.gov.tw/V7/forecast/taiwan/Tainan_City.htm')
	soup = BeautifulSoup(page, 'html.parser')
	infoAll = soup.find('table', 'FcstBoxTable01').find_all('td') 
	temperature = infoAll.pop(0).string
	#print(len(infoAll))
	print(infoAll)
	print(str(infoAll[1].string))
	return str(infoAll[1].string) + ' 氣溫是'+str(temperature)

def clock():
	print('時間 func')
	cur=datetime.datetime.now()
	hr = cur.hour
	Min = cur.minute
	year = cur.year
	date = cur.day
	month = cur.month	
	print (str(year) + '年'+ str(month)+ '月' + str(date) +'日' + str(hr) + '點' + str(Min) + '分')
	return str(year) + '年'+ str(month)+ '月' + str(date) +'日' + str(hr) + '點' + str(Min) + '分'

def math():
	print('數學 func')

def game():
	print('遊戲 func')
	ans = randint(1, 2)
	if ans==1:
		print('什麼水可以放口袋?')
		return '什麼水可以放口袋? 快點想 三秒後公佈答案 阿阿阿阿阿阿阿阿阿阿阿 答案是 薪水'
	elif ans==2:
		print('什麼樣的雨可以淋死人? 快點想 三秒後公佈答案 阿阿阿阿阿阿阿阿阿阿阿 答案是 槍林彈雨')
		return '什麼樣的雨可以淋死人? 快點想 三秒後公佈答案 阿阿阿阿阿阿阿阿阿阿阿 答案是 槍林彈雨'
	elif ans==3:
		print('59487你會想到甚麼? 快點想 三秒後公佈答案 阿阿阿阿阿阿阿阿阿阿阿 答案是 哈哈哈哈 我會想到你')
		return '59487你會想到甚麼? 快點想 三秒後公佈答案 阿阿阿阿阿阿阿阿阿阿阿 答案是 哈哈哈哈 我會想到你'

def job():
	action(0, 1, 1, 1)
	time.sleep(2)
	action(1, 0, 1, 1)
	time.sleep(2)
	action(1, 1, 0, 1)
	time.sleep(2)
	action(1, 1, 1, 0)
	
# pin
outputPin1 = 10
outputPin2 = 9
outputPin3 = 11
outputPin4 = 5
def action(pin1, pin2, pin3, pin4):
	GPIO.output(outputPin1, pin1)
	GPIO.output(outputPin2, pin2)
	GPIO.output(outputPin3, pin3)
	GPIO.output(outputPin3, pin4)

def robot():
	print('In robot func')
	#os.system('MusicForRobot.mp3')

	
	# GPIO Setting
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(outputPin1, GPIO.OUT)
	GPIO.setup(outputPin2, GPIO.OUT)
	GPIO.setup(outputPin3, GPIO.OUT)
	GPIO.setup(outputPin4, GPIO.OUT)


	GPIO.output(outputPin1, 1)
	GPIO.output(outputPin2, 1)
	GPIO.output(outputPin3, 1)
	GPIO.output(outputPin4, 1)
	print('設定完成')
		# ---------------------------- #
		# 改成語音辨識去操控動作
		# 0: make the action ; 1: no action
	'''
	action(0, 1, 1, 1)
	time.sleep(2)
	action(1, 0, 1, 1)
	time.sleep(2)
	action(1, 1, 0, 1)
	time.sleep(2)
	action(1, 1, 1, 0)
	'''
	# 建立一個子執行緒
	t = threading.Thread(target = job)

	# 執行該子執行緒
	t.start()
	print('播音樂開始')
		# ---------------------------- #
	os.system('mpg321 MusicForRobot.mp3')
	t.join()
	return 'robot dance OK !'



def Rni(inputt):
	# do the NLP
	seg_list = jieba.cut_for_search(inputt)

	print(inputt.split())
	haha = inputt.split()

	count = 0
	# judge the jieba NLP
	for i in inputt.split():
		print('字串loop切割狀態')
		print(i)
		print('-------------')
		if "你好" in i or i=='好' or i=='機器人' or i=='機器':
			return robot()

		if i=='天氣' or i=='氣溫' or i=='溫度' or i=='氣象':
			return weather()
			break
		elif i=='幾點' or i=='時間' or i=='報時':
			return clock()
			break
		elif i=='猜謎' or i=='遊戲' or i=='謎語' or i=='謎語' or i=='謎' or i=='遊戲' or i=='玩遊戲' or i=='玩' or i=='耍' or i=='猜':
			return game()
			break
		else:
			for j in seg_list:
				if j == '耍':
					return game()
			count+=1
			if count==len(haha):
				return '我不知道你在說什麼'

if __name__ == '__main__':
	Rni('我想 知道 現在的 時間')
