"""Works as the Fetching Module to Get weather"""
import requests,json,os
from dotenv import load_dotenv
load_dotenv() #loads env folder into the program 

def get_weather(city:str): 
        """This function Fetch Weather and Return to User """
        api_key = os.getenv('API_KEY')
        base_url = 'https://api.weatherapi.com/v1/current.json?key='
        request_url = (base_url+api_key+'&q='+city+'&aqi=no')
        response = requests.request('GET',request_url)
        parsed = response.json()
        global time,city_name,temp_C,feelsLikeTemp_C,condition,humidity,cloud,icon
        time = (parsed['location']['localtime'])
        city_name = (parsed['location']['name'])
        temp_C = (parsed['current']['temp_c'])
        feelsLikeTemp_C = (parsed['current']['feelslike_c'])
        condition = (parsed['current']['condition']['text'])
        humidity = (parsed['current']['humidity'])
        cloud = (parsed['current']['cloud'])
        icon = (parsed['current']['condition']['icon'])
        return time,city_name,temp_C,feelsLikeTemp_C,condition,humidity,cloud,icon

if __name__ == '__main__': #Solo console build- wont execute in foreing file 
    """Console Based Program for the Weather Application"""
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
            try:
                get_weather(city)
                print('Current Time : ',time)
                print('Location : ',city_name)
                print('Temperature : ',temp_C)
                print("Real Feel :",feelsLikeTemp_C)
                print('Condition : ',condition)
                print('Humidity : ',humidity)
                print('Clouds : ', cloud)
                print("------------------------------------------------")
            except:
                print('City Not Found - Please Try Again !!')
    print("=----------------------------------------------=")
    print("      | Build By: Rahid Mondal ©2022 |          ")
    print("=----------------------------------------------=")

