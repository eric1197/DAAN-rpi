import requests

aqi_url = "http://opendata2.epa.gov.tw/AQI.json"

response = requests.get(aqi_url)
aqi = response.json()
site = input("Input site name: ")

print(response.status_code)
items=("County","SiteName","PM2.5","AQI")
if response.status_code==200:
  for i in items:
    print(i, end='\t')
  print()

  for d in aqi:
    if(d["SiteName"])==site:
      for i in items:
        print(d[i], end='\t')
      print()
else:
  print("ERROR!!")
