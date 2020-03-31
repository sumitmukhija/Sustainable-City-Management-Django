import os
from dotenv import load_dotenv
from SCMBackend.singleton import singleton

@singleton
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
            Bike related environ vars
    '''
    def get_dublin_bikes_api_key(self):
        return self.get_var_with_key('DUBLIN_BIKES_KEY')

    def get_dublin_bikes_base_url(self):
        return self.get_var_with_key('DUBLIN_BIKES_URL')

    def get_base_bus_stop_tt_url(self):
        return self.get_var_with_key("BUS_TT_URL")

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

    def get_base_luas_stop_url(self):
        return self.get_var_with_key('BASE_MONGO_LUAS_STOP_URL')

    def get_base_irish_rail_stop_url(self):
        return self.get_var_with_key('BASE_MONGO_IRISH_RAIL_STOP_URL')

    def get_base_bus_internal_tt_url(self):
        return self.get_var_with_key('BASE_INTERNAL_BUS_TT_URL')

    """
        Pusher related vars
    """
    def get_pusher_app_id(self):
        return self.get_var_with_key('PUSHER_APP_ID')

    def get_pusher_key(self):
        return self.get_var_with_key('PUSHER_APP_KEY')
    
    def get_pusher_secret(self):
        return self.get_var_with_key('PUSHER_APP_SECRET')


    def get_var_with_key(self, key):
        if os.getenv(key) is None:
            raise ValueError(str(key) + ' not found')
        else:
            return os.getenv(key)

    def get_test_creds(self, cred_type, validity):
        if validity:
            if cred_type.lower() == 'user':
                return self.get_var_with_key('TEST_VALID_USER')
            elif cred_type.lower() == 'password':
                return self.get_var_with_key('TEST_VALID_PASS')
        else:
            if cred_type.lower() == 'user':
                return self.get_var_with_key('TEST_INVALID_USER')
            elif cred_type.lower() == 'password':
                return self.get_var_with_key('TEST_INVALID_PASS')
