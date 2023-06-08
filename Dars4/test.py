import requests
s="Urgench"

api_url = f'https://api.weatherapi.com/v1/current.json?key=9e070c3df80441ffb0b113050232703&q={s}&aqi=no'

data=requests.get(api_url)

data=data.json()

name=data['location']['name']
region=data['location']['region']
country=data['location']['country']
temp=data['current']['temp_c']
time=data['current']['last_updated']
timelocal=data['location']['localtime']

image=data['current']["condition"]['icon']
status=data['current']["condition"]['text']


print(daname,region,country,temp,time,timelocal,status,image,sep="\n")
