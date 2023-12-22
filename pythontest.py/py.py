import requests

apikey = "bfc177c11d7f08513174f8e2a22c7749"
url = "https://api.openweathermap.org/data/2.5/weather"


params = {'q': "Delhi",
        'appid' : apikey,
        'units':'metric'}

data = requests.get(url,params=params)

data.json()