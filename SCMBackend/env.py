import os
from dotenv import load_dotenv

class Environ():

    def __init__(self):
        load_dotenv()

    '''
            Breezometer related environ vars
    '''
    def get_breezometer_api_key(self):
        return self.get_var_with_key('BREEZOMETER_KEY')

    def get_breezometer_base_url(self):
        return self.get_var_with_key('BREEZOMETER_BASE_URL')

    '''
            Mongo related environ vars
    '''
    def get_mongo_host(self):
        return self.get_var_with_key('MONGO_HOST')

    '''
            Host related environ vars
    '''
    def get_localhost(self):
        return self.get_var_with_key('LOCALHOST')
    
    def get_base_pollution_url(self):
        return self.get_var_with_key('BASE_MONGO_POLLUTION_URL')

    def get_base_bike_url(self):
        return self.get_var_with_key('BASE_MONGO_BIKE_URL')

    def get_base_traffic_url(self):
        return self.get_var_with_key('BASE_MONGO_TRAFFIC_URL')

    def get_base_bus_stop_url(self):
        return self.get_var_with_key('BASE_MONGO_BUS_STOP_URL')

    def get_var_with_key(self, key):
        if os.getenv(key) is None:
            raise ValueError(str(key) + ' not found')
        else:
            return os.getenv(key)
