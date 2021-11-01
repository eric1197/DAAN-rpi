import time, RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
seg7 = [5, 33, 19, 15, 13, 7, 21, 11]
scan = [23, 31, 29, 3]
for x in seg7:
    GPIO.setup(x, GPIO.OUT)
for x in scan:
    GPIO.setup(x, GPIO.OUT)

while True:
    for x in range(8):
        GPIO.output(seg7[x], 1)
    for x in range(4):
        GPIO.output(scan[x], 0)
    GPIO.output(3, 1)
    GPIO.output(29, 1)
    GPIO.output(31, 1)
    GPIO.output(23, 1)
    for x in range(8):
        GPIO.output(seg7[x], 0)
        time.sleep(0.5)
