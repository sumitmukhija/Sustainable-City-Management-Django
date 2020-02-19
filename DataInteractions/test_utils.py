from SCMBackend.env import Environ
import requests
import os


class TestUtils:
    def get_valid_auth(self):
        """
        Function to login using a dummy account with all permissions set true
        :return: jwt for user with all permissions
        """
        user = Environ().get_test_creds('user', True)
        pwd = Environ().get_test_creds('password', True)
        token = self.mock_login(user, pwd)
        if token:
            return token
        else:
            raise Exception('Wrong credentials for valid test')

    def get_invalid_auth(self):
        """
        Function to login using a dummy account with all permissions set false
        :return: jwt for user with no permissions
        """
        user = Environ().get_test_creds('user', False)
        pwd = Environ().get_test_creds('password', False)
        token = self.mock_login(user, pwd)
        if token:
            return token
        else:
            raise Exception('Wrong credentials for invalid test')

    def mock_login(self, user, pwd):
        url = Environ().get_localhost()
        url += '/mongo_auth/login/'
        response = requests.post(url=url, data={"username": user, "password": pwd})
        resp = response.json()
        token = ''
        if 'data' in resp and 'token' in resp['data']:
            token = resp['data']['token']

        return token


if __name__ == '__main__':
    TestUtils().get_valid_auth()
    TestUtils().get_invalid_auth()



