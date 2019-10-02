import sys
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

STEPS_PER_REVOLUTION = 64 * 64
SEQUENCE = [[1,0,0,0],
            [1,1,0,0],
            [0,1,0,0],
            [0,1,1,0],
            [0,0,1,0],
            [0,0,1,1],
            [0,0,0,1],
            [1,0,0,1]]
		
STEPPER_PINS = [6,13,19,26]
for pin in STEPPER_PINS:
  GPIO.setup(pin,GPIO.OUT)
  GPIO.output(pin, GPIO.LOW)

SEQUENCE_COUNT = len(SEQUENCE) # 定義每一個循環由多少的步驟 (順序) 組成。
PINS_COUNT = len(STEPPER_PINS) # 定義總共有幾個控制用的腳位。

sequence_index = 0 # 記錄目前進行到哪個步驟的變數 – sequence_index
direction = 1 # 記錄轉動方向的變數 – direction。當 direction 為 1 時表示正向轉動，而 direction 為 -1 時表示反向轉動。
steps = 0 # 記錄目前已移動步數的變數。

if len(sys.argv)>1: # 用來控制每一個步驟中間的暫停時間。
  wait_time = int(sys.argv[1])/float(1000)
else: # 程式透過這個方式來改變馬達的轉動速度。此參數預設值為 100，表示暫停 100 毫秒，也就是 0.1 秒。
  wait_time = 1/float(1000)

try:
    print('按下 Ctrl-C 可停止程式')
    while steps < STEPS_PER_REVOLUTION:
		
		# 利用迴圈將四個控制腳位設定為合適的電位，
		# 電位的設定值可由兩層串列中直接取得，也就是 SEQUENCE[sequence_index][pin]。
		# 第一層表示第幾個順序步驟，所以使用代表步驟的變數 sequnece_index。
		# 第二層則為該步驟中各腳位的電位狀態，所以使用代表腳位的變數 pin。
		
        for pin in range(0, PINS_COUNT):
            GPIO.output(STEPPER_PINS[pin], SEQUENCE[sequence_index][pin])

        steps += direction

        sequence_index += direction # 計算下一個應該執行的順序。當正向轉動時， sequence_index 加 1，而反向轉動時則減 1
        sequence_index %= SEQUENCE_COUNT # 使用取餘數的方式 (%=)，以避免 sequence_index 的數值因為不斷增加或減少而超過 0~7 的範圍

        if steps % (64*64) == 0:
          time.sleep(2)
          direction = direction* -1
          steps = 0

        print('index={}, direction={}'.format(sequence_index, direction))
        time.sleep(wait_time)
except KeyboardInterrupt:
    print('關閉程式')
finally:
    GPIO.cleanup() # 程式結束後程式中所使用的腳位會回到預設狀態