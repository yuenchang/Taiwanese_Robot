"""
copyright WMMKSLab Gbanyan

modified by wwolfyTC 2019/1/24
"""
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

# import func from Rni
from jb import *

from aiy.board import Board
from aiy.voice.audio import AudioFormat, play_wav, record_file, Recorder

Lab = AudioFormat(sample_rate_hz=16000, num_channels=1, bytes_per_sample=2)
token = "eyJhbGciOiJSUzUxMiIsInR5cCI6IkpXVCJ9.eyJzY29wZXMiOiIwIiwic3ViIjoiIiwiZXhwIjoxNTY5ODk4MjE5LCJhdWQiOiJ3bW1rcy5jc2llLmVkdS50dyIsImlhdCI6MTUzODM2MjIxOSwic2VydmljZV9pZCI6IjMiLCJpZCI6NDksImlzcyI6IkpXVCIsIm5iZiI6MTUzODM2MjIxOSwidmVyIjowLjEsInVzZXJfaWQiOiIwIn0.BZw0abkTwDbl494J_RAlpGRGJKfOgzRjvLzTF3aR0l66xgpfj7L_DOeab1dmaiCXdWvQR2QgvVmuHg-CihLrM99ssbgXGpBc_agxCNMIWVh5Uw6gUjA3_mndyNrKIG9cKTHB402LhsotNtPanriWoEmg7pNPxq69U7hLFIdiML4"

def record():
    with Board() as board:
        print('press to record.')
        board.button.wait_for_press()
        done = threading.Event()
        board.button.when_pressed = done.set

        def wait():
            start = time.monotonic()
            while not done.is_set():
                duration = time.monotonic() - start
                print('recording: %.02f s[press to stop recording]' % duration)
                time.sleep(0.5)

        record_file(Lab, filename='r.wav', wait=wait, filetype='wav')

def askForService(token, data):
    HOST = "140.116.245.149"
    PORT = 2802
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    model = "main"
    try:
        sock.connect((HOST, PORT))
        msg = bytes(token+"@@@", "utf-8")+struct.pack("8s", bytes(model, encoding="utf8"))+b"R"+data
        msg = struct.pack(">I", len(msg)) + msg
        sock.sendall(msg)
        received = str(sock.recv(1024), "utf-8")
    finally:
        sock.close()
    return received

def main():
    outside = 0

    while True:
        with Board():
            print("\n\npress to start")

        record()
        play_wav("r.wav")
        record_file = open('./r.wav','rb').read()
        text = askForService(token, record_file)
        print('+++++++++++++++++++')
        print(text)
        print('+++++++++++++++++++')
        textlist = text.split(':', 1)
        textlist = textlist[1].split('r', 1)
        print(textlist)
        print(type(textlist))
        print('---------------------')
        print(textlist[0])
        print('-----------------------')
        RniReply = Rni(textlist[0], outside)
        #RniReply = Rni('時間', outside)
        # --------因為出去玩的有對話系統 ---------- #
        if str(RniReply) != '出去玩':
            outside = 0
        if str(RniReply) == '出去玩':
            outside = 1
        # --------因為出去玩的有對話系統 ---------- #



        # --------非對話系統中 的行為 ------------ #
        if outside == 0:
            #tts = gTTS(text=RniReply, lang='zh-tw')
            #tts.save('ip.mp3')
            #os.system('mpg321 ip.mp3')
            print('刪除掉了 rni reply QQQQQ')
        # --------非對話系統中 的行為 ------------ #
            '''
            person = "TW_LIT_AKoan"  # 人物(語言)
            vol = "100"  # 音量 0~100
            speed = "-2"  # 速度 -10~10
            subprocess.call(["/usr/bin/php", "tts.php", str(RniReply), person, vol, speed])
            play_wav("word.wav")
        '''
        #return c_text[1]
        


if __name__ == '__main__':
    main()
