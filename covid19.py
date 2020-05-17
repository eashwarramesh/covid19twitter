import json
import requests
from datetime import datetime

#Time Information to embed on Tweet to avoid Duplicate Tweet Issue

now = datetime.now()
current_time = now.strftime("%H:%M:%S")

#Requesting information from API Website

request = requests.get("https://api.covid19api.com/summary")

#Converting API Information into Text format

request_text = request.text

#Converting JSON Information into Python Dict Format

data = json.loads(request_text)

for value in data['Countries']:
    NewConfirmed = (value['NewConfirmed'])
    TotalConfirmed = (value['TotalConfirmed'])
    NewDeaths = (value['NewDeaths'])
    TotalDeaths = (value['TotalDeaths'])
    TotalRecovered = (value['TotalRecovered'])
    CountryName = (value['Country'])
    
    if(CountryName == "India"):
        message1 = "The Total Number of Cases is",TotalConfirmed
        message2 = "Total Deaths is",TotalDeaths
        message3 = "New cases from Today is",NewConfirmed
        message4 = "Information as of",current_time
        
#Converting Tuple to String        
        
        m1=str(message1)
        m11="\n"
        m2=str(message2)
        m12="\n"
        m3=str(message3)
        m13="\n"
        m4=str(message4)
        m14="\n"
        m15="\n"
        m5="Powered by a #RaspberryPi and covid19api.com"
        
        m6=m1+m11+m2+m12+m3+m13+m4+m14+m15+m5
        print(m6)
        
#Twitter Module Import
        
        from twython import Twython
        from auth import(consumer_key, consumer_secret, access_token, access_token_secret)
        twitter = Twython(consumer_key, consumer_secret, access_token, access_token_secret)
        
#Twitter Status Function        
        
        twitter.update_status(status=m6)
        print("Tweeted")
