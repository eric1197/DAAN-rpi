import time, RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
w = [3,5,7,23,11,13,15,29,19,21]
for x in w:
    GPIO.setup(x, GPIO.OUT)

while True:
    for x in range(9):
    	    for y in w:
	        GPIO.output(y, 0)
            GPIO.output(w[x], 1)
            GPIO.output(w[x+1], 1)
            time.sleep(0.1)
    for z in range(8):
    	    for y in w:
	        GPIO.output(y, 0)
            GPIO.output(w[9-z], 1)
            GPIO.output(w[8-z], 1)
	    time.sleep(0.1)
