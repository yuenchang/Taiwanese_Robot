import datetime
import time
from stepMotor2 import *
from finalRobot import *

#------- thread ---------#
import threading
import time
#------- thread ---------#


def tt():
    localtime = time.localtime(time.time())
    hr = localtime.tm_hour
    #motor()

    if (hr>11 and hr<13) or (hr>18 and hr<20):
        print('該吃藥囉')
        return '該吃藥囉'
    else:
        #tts = gTTS(text='阿阿阿阿阿！', lang='zh-tw')
        #tts.save('ip.mp3')
        os.system('mpg321 hahaha.mp3')
        motor()
        os.system('mpg321 no_medicine.mp3')
        print('現在時間'+str(hr)+'點'+str(localtime.tm_min)+'分 不是吃藥時間')
        return '現在時間'+str(hr)+'點'+str(localtime.tm_min)+'分 不是吃藥時間'

if __name__ == '__main__':
	tt()