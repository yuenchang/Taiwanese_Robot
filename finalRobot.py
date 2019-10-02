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

import os

# ------------- 各種初始設定 ---------------- #
# pin
outputPin1 = 17
outputPin2 = 27
outputPin3 = 22
outputPin4 = 5

def robot_action_set():
	print('In robot func')
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

# 動作 is what (也是初始設定)#
def action(pin1, pin2, pin3, pin4):
	GPIO.output(outputPin1, pin1)
	GPIO.output(outputPin2, pin2)
	GPIO.output(outputPin3, pin3)
	GPIO.output(outputPin4, pin4)





# ------------- 動作細部設計 ---------------- #
def sport():
	time.sleep(3.5)
	action(0, 1, 1, 1)
	time.sleep(1)
	action(1, 0, 1, 1)
	time.sleep(1)
	action(0, 1, 1, 1)
	time.sleep(1.3)
	action(1, 0, 1, 1)
	time.sleep(3)
	action(1, 1, 0, 1)
	time.sleep(1.8)
	action(1, 1, 1, 0)

def excited():
	for i in range(0, 7):
		action(1, 1, 0, 1)
		time.sleep(0.5)
		action(1, 1, 1, 0)
		time.sleep(0.5)

def where():
	action(0, 1, 1, 1)
	time.sleep(0.7)
	action(1, 1, 0, 1)
	action(0, 1, 1, 1)
	time.sleep(0.7)
	action(1, 1, 0, 1)

def sun():
	for i in range(0, 2):
		action(0, 1, 1, 1)
		time.sleep(1)
		action(1, 0, 1, 1)
		time.sleep(1)

def other():
	for i in range(0, 2):
		action(1, 1, 0, 1)
		time.sleep(1)
		action(1, 1, 1, 0)
		time.sleep(1)

def fuckyou():
	action(1, 1, 0, 1)

# --------------- 動作主call func ------------------ #
def robotssport():
		# ---------------------------- #
		# 改成語音辨識去操控動作
		# 0: make the action ; 1: no action

	robot_action_set()

	# 建立一個子執行緒
	t = threading.Thread(target = sport)
	#sport()
	# 執行該子執行緒
	t.start()

		# ---------------------------- #
	os.system('mpg321 dance.mp3')
	print('播音結束')
	t.join()
	return 'robot dance OK !'

def excited_medicine():
	robot_action_set()
	excited()
	return 'excited medcine OK !'


def wherePlayAsk():
	robot_action_set()
	where()
	return 'where play ok!'

def sunrobot():
	robot_action_set()
	sun()
	return 'sun ok!'

def otherrobot():
	robot_action_set()
	other()
	return 'other except sun ok!'

def fuck():
	robot_action_set()
	fuckyou()
	return 'ffffffffffffffffffuck'

if __name__ == '__main__':
	robotssport()