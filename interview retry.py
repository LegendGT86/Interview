import requests
import json

CT_Lat = -33.9249
CT_Lon = 18.4241
Lnd_Lat = 51.5072
Lnd_Lon = -0.1276
api_key = 'afca0dc69110a51fa8cc681e4ea6f2ed'
ct_endpoint =(f'https://api.openweathermap.org/data/2.5/onecall?lat={CT_Lat}&lon={CT_Lon}&exclude=alerts&appid={api_key}')
ld_endpoint =(f'https://api.openweathermap.org/data/2.5/onecall?lat={Lnd_Lat}&lon={Lnd_Lon}&exclude=alerts&appid={api_key}')
w_site: 'https://openweathermap.org/'

response_ct = requests.get(ct_endpoint)
response_ld = requests.get(ld_endpoint)
primary_ct = response_ct.json()
primary_ld = response_ld.json()
 
# Information Pertaining to CapeTown
if response_ct.status_code == 200:
    print(' ')
    print('City : Cape Town,RSA')
    tz = primary_ct['timezone']
    wtr = primary_ct['current']['weather']
    print('Response code valid - 200')
    print(f'TimeZone is : {tz}')
    print(f'current weather conditions in CapeTown: {wtr}')
    for data in response_ct.json()['current']:
        print(data, response_ct.json()['current'][data])
else:
    print (f'HTTP request error {response_ct.status_code}')

# Information pertaining to London
if response_ld.status_code == 200:
    print('\n')
    print('City : London, UK')
    tz = primary_ld['timezone']
    wtr = primary_ld['current']['weather']
    print('Response code valid - 200')
    print(f'TimeZone is : {tz}')
    print(f'current weather conditions in London: {wtr}')
    for data in response_ld.json()['current']:
        print(data, response_ld.json()['current'][data])
else:
    print (f'HTTP request error {response_ld.status_code}')


# The latitudes and longitudes can be preset in a list or
# extracted from web source to allow reuseability of the code for a variation of locations