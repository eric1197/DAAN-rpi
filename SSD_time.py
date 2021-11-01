import time, RPi.GPIO as GPIO
import _thread

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
times = 0
colon = 0

for x in seg7:
    GPIO.setup(x, GPIO.OUT)
for x in scan:
    GPIO.setup(x, GPIO.OUT)
GPIO.setup(37, GPIO.IN)

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

def ThreadScan(sleeptime):
    global y
    while True:
        GPIO.output(scan[y], 0)
        y = y+1
        if y>3:
            y=0
        #print(Data[y])
        if y>=2:
            out(font[Data[y]]+128*colon)
        else:
            out(font[Data[y]])
        GPIO.output(scan[y], 1)
        time.sleep(sleeptime)

_thread.start_new_thread(ThreadScan, (0.00001,))

def pressed(a):
    global times
    times+=1
    times%=3
    print("mode = %d" % times)

GPIO.add_event_detect(37, GPIO.FALLING, callback = pressed, bouncetime = 200)
old = 0

while True:
    t = int(time.strftime("%S")) + int(time.strftime("%M")) * 100
    if times == 1:
        t = int(time.strftime("%Y"))
    elif times == 2:
        t = int(time.strftime("%d")) + int(time.strftime("%m")) * 100
    if t != old:
        colon = 1
        saveData(t)
        time.sleep(0.5)
        colon = 0
        old = t
