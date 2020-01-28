import os

class BikeUtil():
    
    def getAPIKey(self):
        return os.getenv('DUBLIN_BIKES_KEY')
