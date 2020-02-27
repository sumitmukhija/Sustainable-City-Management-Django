from DataInteractions.test_utils import TestUtils
from SCMBackend.env import Environ

class AuthenticationUtils():
    def __init__(self):
        self.valid_token = TestUtils().get_valid_auth()
        self.headers = {"Authorization": self.valid_token}

    def get_valid_token(self):
        return self.valid_token

    def get_headers(self):
        return self.headers