import time, requests, _thread, RPi.GPIO as GPIO
# init of SSD
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
seg7 = [5, 33, 19, 15, 13, 7, 21, 11]
scan = [23, 31, 29, 3]
font = [0x3F, 0x06, 0x5B, 0x4F, 0x66, 0x6D, 0x7D, 0x27, 0x7F, 0x6F, 0x00]
y = 0
AQI = 0
Data = [0, 0, 0, 0]  
mode = 0
val = [0,0]
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
def saveData(AQI):
    temp = AQI
    for x in range(4):
        Data[x] = temp % 10
        temp = temp // 10
    for i in range(3, 0, -1):
        if Data[i] == 0:
            Data[i] = 10
        else:
          break
def ThreadScan(sleeptime):
    global y
    while True:
        GPIO.output(scan[y], 0)
        y = y+1
        if y>3:
            y=0
        #print(Data[y])
        out(font[Data[y]])
        GPIO.output(scan[y], 1)
        time.sleep(sleeptime)
def pressed(a):
    global mode,d
    mode+=1
    mode%=2
    #print(mode, end='\n')
    saveData(val[mode])

_thread.start_new_thread(ThreadScan, (0.00001,))
GPIO.add_event_detect(37, GPIO.FALLING, callback = pressed, bouncetime = 200)

# init of Data

# main
while True:
  date = input("Input date: ")
  aqi_url = "https://www.twse.com.tw/exchangeReport/STOCK_DAY?date=" + date + "&stockNo=2330"
  response = requests.get(aqi_url)
  aqi = response.json()
  print(response.status_code)
  items=("County","SiteName","PM2.5","AQI")
  if response.status_code==200:
      for i in range(len(aqi["data"])):
          if((aqi["data"][i][0][7:9]) == date[6:8]):
              print(date + " 收盤價: " + aqi["data"][i][6].split('.')[0])
              saveData(int(aqi["data"][10][6].split('.')[0]))
              print()
  else:
    print("ERROR!!")
