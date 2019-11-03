# You don't have to use these classes, but we recommend them as a good place to start!
from dotenv import load_dotenv
import os
load_dotenv()
import requests

class WeatherGetter:
    def __init__(self):
        # Let's set our secrets and keys from the .env file
        # as environment variables.
        self.BASE_URL = 'https://api.darksky.net'
        self.token = os.getenv('DARKSKYKEY')
        if len(self.token) == 0:
            raise ValueError('Missing API key!')
        print(self.token)
        
#     def getweather(latitude, longitude, date):
#         for d in dates:

#             time=f'{d}T15:00:00'
#             key = self.token

#             url=https://api.darksky.net/forecast/key/[latitude],[longitude],[time]
            

    def checkup(self):
        return self.token


class MongoHandler():
    pass