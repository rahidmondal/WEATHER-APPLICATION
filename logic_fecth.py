import requests,json,os
from dotenv import load_dotenv
load_dotenv() #loads env folder into the program 

def get_weather(city:str): #weather Fetching Logic
    api_key = os.getenv('API_KEY')
    base_url = 'https://api.weatherapi.com/v1/current.json?key='
    request_url = (base_url+api_key+'&q='+city+'&aqi=no')
    response = requests.request('GET',request_url)
    parsed = response.json()
    global time,location,temp_C,feelsLikeTemp_C,condition,humidity,cloud
    time = (parsed['location']['localtime'])
    location = (parsed['location']['name'])
    temp_C = (parsed['current']['temp_c'])
    feelsLikeTemp_C = (parsed['current']['feelslike_c'])
    condition = (parsed['current']['condition']['text'])
    humidity = (parsed['current']['humidity'])
    cloud = (parsed['current']['cloud'])
    return time,location,temp_C,feelsLikeTemp_C,condition,humidity,cloud

if __name__ == '__main__': #Solo console build- wont execute in foreing file 
    print("=----------------------------------------------=")
    print("| 날씨[WeatherApplication]-Console Build v-0.1 |")
    print("=----------------------------------------------=")
    while True : 
        print('{Note : Enter X to exit!!!}')
        city = input("Enter City Name : ")
        city = city.capitalize() 
        if city == 'X': 
            break
        else :
            get_weather(city)
            print('Current Time : ',time)
            print('Location : ',location)
            print('Temperature : ',temp_C)
            print("Real Feel :",feelsLikeTemp_C)
            print('Condition : ',condition)
            print('Humidity : ',humidity)
            print('Clouds : ', cloud)
            print("------------------------------------------------")
    print("=----------------------------------------------=")
    print("      | Build By: Rahid Mondal ©2022 |          ")
    print("=----------------------------------------------=")

