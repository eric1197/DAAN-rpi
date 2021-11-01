import time, RPi.GPIO as GPIO

GPIO.setwarnings(False)
w = [3,5,7,23,11,13,15,29,19,21]
GPIO.setmode(GPIO.BOARD)
for x in w:
    GPIO.setup(x, GPIO.OUT)
    #p1 = GPIO.PWM(3, 1000)

while True:
    for x in w:
        for dc in range (5, 101, 5):
            GPIO.PWM(x, 1000).start(dc)
            time.sleep(0.2)
