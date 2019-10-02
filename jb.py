import jieba
import time  # 引入time模块
import datetime
from random import *
import requests
from bs4 import BeautifulSoup
from time_file import *
from weather_scrapy import *
import time
import threading
import socket
import struct
import re
import os
import sys
from subprocess import call
from enum import Enum, unique
from traceback import print_exc
from gtts import gTTS
from aiy.board import Board
from aiy.voice.audio import AudioFormat, play_wav, record_file, Recorder
from dance import *
from finalRobot import *

# ------ robot --------- #
import RPi.GPIO as GPIO
import time
from playsound import playsound
# ------ robot --------- #

#------- thread ---------#
import threading
import time
#------- thread ---------#

def sport():
	print('運動 跳舞 func')
	robotssport()
	os.system('mpg321 dance_ok.mp3')
	return '跳舞運動完成'

def clock():
	print('時間 吃藥 旋轉布近馬達 func')
	#tts = gTTS(text='我來看看現在時間', lang='zh-tw')
	#tts.save('ip.mp3')
	os.system('mpg321 look_what_time_is_it.mp3')
	# 建立一個子執行緒
	t = threading.Thread(target = excited_medicine)
	# 執行該子執行緒
	t.start()
	t.join()
    #excited_medicine()
	return tt()


def outside():
	print('出門景點 查天氣 oled顯示器 第一次對話func')
	#tts = gTTS(text='我幫你查看看天氣', lang='zh-tw')
	#tts.save('ip.mp3')
	os.system('mpg321 hows_the_weather.mp3')
	# 建立一個子執行緒
	t = threading.Thread(target = wherePlayAsk)
	# 執行該子執行緒
	t.start()
	t.join()
	#tts = gTTS(text='你想去哪裡玩', lang='zh-tw')
	#tts.save('ip.mp3')
	os.system('mpg321 go_where_play.mp3')
	return '出去玩'

def outside2(playingspot):
	print('出門景點 查天氣 oled顯示器 第二次對話func')
	#tts = gTTS(text='定位查詢天氣中 請稍後', lang='zh-tw')
	#tts.save('ip.mp3')
	os.system('mpg321 wait_for_weather.mp3')
	weather_return = travel(playingspot)
	if '晴' in weather_return or '日' in weather_return:
		 # 建立一個子執行緒
		os.system('mpg321 sun_weather.mp3')
		t = threading.Thread(target = sunrobot)
		# 執行該子執行緒
		t.start()
		t.join()
	else:
		# 建立一個子執行緒
		os.system('mpg321 bad_weather.mp3')
		t = threading.Thread(target = otherrobot)
		# 執行該子執行緒
		t.start()
		t.join()
	return weather_return


def Rni(inputt, conversation):
	if conversation ==0:
		# do the NLP
		seg_list = jieba.cut_for_search(inputt)

		print(inputt.split())
		haha = inputt.split()

		count = 0
		# judge the jieba NLP
		for i in haha:
			print('字串loop切割狀態')
			print(i)
			print('-------------')
			count+=1
			if '跳舞'in i or '運動'in i or '霧'in i:
				return sport()
				break
			elif '幾點'in i  or '時間'in i  or '食藥仔'in i  or '食藥仔'in i or '藥仔'in i:
				return clock()
				break
			elif '天氣'in i  or '出門'in i  or '玩'in i  or '出去玩'in i or '去' in i:
				return outside()
				break
			else:
				if count==len(haha):
					print('我不知道你在說什麼')
					fuck()
					return '我不知道你在說什麼'
					#return outside()
	elif conversation==1:
		seg_list = jieba.cut_for_search(inputt)
		haha = inputt.split()
		playingplace = haha[0][2:]
		print('要去玩的景點是' + playingplace)
		return outside2(playingplace)



if __name__ == '__main__':
	Rni('我想 天氣')
