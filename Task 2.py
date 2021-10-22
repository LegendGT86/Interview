# testing of the weatherapp api
import json
import requests


def weatherapp():
    api_key = 'afca0dc69110a51fa8cc681e4ea6f2ed'
    w_site = "https://openweathermap.org/"
    Cities = ["Cape Town", "London"]


    for x in Cities:
        api_url = (f'{site} + "q" + {Cities} + "" & appid = " + {api_key}')
        api_status = requests.get(api_url)
        if api_status_code == 200:
            data = response.json()
            main = data['main']
            temp = main['temp']
            sunr = main['Sunrise']
            sunst = main['Sunset']
            print(temp)
        else:
            print(f'{x} + api_status_code')



