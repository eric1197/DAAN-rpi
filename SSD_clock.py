import time, RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
seg7 = [5, 33, 19, 15, 13, 7, 21, 11]
scan = [23, 31, 29, 3]
font = [0x3F, 0x06, 0x5B, 0x4F, 0x66, 0x6D, 0x7D, 0x27, 0x7F, 0x6F, 0x00]
cnt = 0
delaytime = 0.001
starttime = 0
Data = [0, 0, 0, 0]
y = 0
for x in seg7:
    GPIO.setup(x, GPIO.OUT)
for x in scan:
    GPIO.setup(x, GPIO.OUT)

def out(n):
    for x in range(8):
        if n % 2 == 1:
            GPIO.output(seg7[x], 0)
        else:
            GPIO.output(seg7[x], 1)
        n = n // 2

def saveData(cnt):
    temp = cnt
    for x in range(4):
        Data[x] = temp % 10
        temp = temp // 10

while True:
    if cnt > 9999:
        cnt = 0
    if time.time() - starttime >= 0.01:
        starttime = time.time()
        cnt = cnt + 1
    saveData(cnt)
    out(font[Data[y]])
    GPIO.output(scan[y], 1)
    time.sleep(delaytime)
    GPIO.output(scan[y], 0)
    y = y+1
    y = y % 4

