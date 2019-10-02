import time  # 引入time模块
import datetime
from random import *
import requests
from bs4 import BeautifulSoup
import os
import sys
from place_to_longlat import *

# ----------------------------------- #
'''
輸入地點 string
進去跟中央氣象局爬到的各縣市名稱經緯度去比較
算出最接近的縣市的天氣
return 天氣 string

使用方式：
call main('要查詢的地點') 即可
'''
# ----------------------------------- #



thePlace = []
theWeather = []

def get_articles(dom):
	soup = BeautifulSoup(dom, 'html.parser')
	returndict = {}

	cc = 0
	#地名 22個城市
	d1 = soup.find_all('tr')
	for d in d1:
		if d.find('th'):
			place = d.find('th').text
			if place!='':
				thePlace.append(place)
				cc+=1

	'''
	#白天晚上 氣溫
	d2 = soup.find_all('td','num')
	for dd2 in d2:
		articles.append({'temperature' : dd2.text.strip()})
    '''

	#下雨程度
	d3 = soup.find_all('td','num')
	cf = 0
	a=0
	for dd3 in d3:
		if dd3.find('img'):
			k = dd3.find('img')['title']
			if cf%14 == 0:
				theWeather.append(k)
			cf+=1

	returndict['place'] = thePlace
	returndict['weather'] = theWeather
	return returndict

def get_web_page(url):
	resp = requests.get(url)
	resp.encoding = 'utf-8'
	
	#success open website
	if resp.status_code != 200:#server的回覆馬 404error 200ok
		print('Invalis url:', resp.url)
		return None
	#falied to open website
	else:
		return resp.text
	
def travel(userGowhere):
	#  -----------------------  #
	'''
	info 是一個 dict
	紀錄著中央氣象局資訊
	裡面有兩個項目一個是地點list 一個是天氣list
	'''
	# ------------------------  #
	page = get_web_page('http://www.cwb.gov.tw/V7/forecast/week/week.htm')
	info = get_articles(page)
	print(info)
	
	placelist = info['place']
	weatherlist = info['weather']
	placelist.remove(placelist[20]) # 金門縣 google 找不到
	weatherlist.remove(weatherlist[20])

	city_longlat = [] # city_longlat 紀錄所有city的經緯度 是一個nested list
	for i in placelist:
		city_longlat.append(placeToLonglat(i))
	#print(city_longlat)
	
	userlatlong = placeToLonglat(userGowhere)

	userlat = userlatlong[0]
	userlong = userlatlong[1]
	
	distance = []
	for i in city_longlat:
		la = i[0]
		lo = i[1]
		distance.append( (la-userlat)*(la-userlat) + (lo-userlong)*(lo-userlong) )
	#print(distance)
	#print(min((distance)))
	#print(distance.index(min(distance)))
	print(userGowhere + '  的天氣是-> ')
	print(weatherlist[distance.index(min(distance))])
	return userGowhere + '  的天氣是' + weatherlist[distance.index(min(distance))]


if __name__ == '__main__':
	travel('台大')