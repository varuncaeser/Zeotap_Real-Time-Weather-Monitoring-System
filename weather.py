import requests
from dotenv import load_dotenv
import os
from dataclasses import dataclass

load_dotenv()
api_key = os.getenv('284494b43222342cf380627a03bb7b29')

@dataclass
class Weather_Data:
    main:str
    description:str
    icon:str
    temperature:float

def get_all_altitude(city_name,state_code,country_code,API_key):
    responce = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&appid={API_key}').json()
    data = responce[0]
    lat , lon = data.get('lat'),data.get('lon')

    return lat,lon
    
def get_current_weather(lat,lon,API_key):
    responce = requests.get(f'http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}&units=metric').json()
    data = Weather_Data(
    main = responce.get('weather')[0].get('main'),
    description =  responce.get('weather')[0].get('description'),
    icon =  responce.get('weather')[0].get('icon'),
    temperature=responce.get('main').get('temp')
    )
    return data

    
def main(city_name, state_name , Country_name):
    lat , lon = get_all_altitude(city_name,state_name,Country_name,api_key)
    final_weather_data = get_current_weather(lat,lon,api_key)
    return final_weather_data







if __name__ == "__main__":
    lat , lon = get_all_altitude('kolkata','WB','INDIA',api_key)
    print(get_current_weather(lat,lon,api_key))

