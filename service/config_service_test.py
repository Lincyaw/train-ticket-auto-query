import unittest
from service.config_service import *
from service.auth_service import DtoLoginUser, users_login
from service.test_utils import BASE_URL, headers
from faker import Faker

fake = Faker()


class TestConfigService(unittest.TestCase):
    def setUp(self):
        self.client = requests.Session()
        self.host = BASE_URL
        basic_auth_dto = DtoLoginUser(username='fdse_microservice',
                                      password='111111', verificationCode="123")
        token = users_login(self.client, basic_auth_dto, headers, BASE_URL)
        self.headers = {'Authorization': f'Bearer {token}'}

    def tearDown(self):
        self.client.close()

    def test_welcome(self):
        response = welcome(self.client, self.host, self.headers)
        self.assertIsInstance(response, str)

    def test_query_all(self):
        response = query_all(self.client, self.host, self.headers)
        self.assertIsInstance(response, dict)

    def test_create_config(self):
        info = Config(name="moumouta", value="777", description="bravo!")
        response = create_config(self.client, info, self.host, self.headers)
        self.assertIsInstance(response, dict)

    def test_update_config(self):
        info = Config(name="moumouta", value="666", description="bravo!")
        response = update_config(self.client, info, self.host, self.headers)
        self.assertIsInstance(response, dict)

    def test_delete_config(self):
        config_name = "moumouta"
        response = delete_config(self.client, config_name, self.host, self.headers)
        self.assertIsInstance(response, dict)

    def test_retrieve_config(self):
        config_name = "moumouta"
        response = retrieve_config(self.client, config_name, self.host, self.headers)
        self.assertIsInstance(response, dict)


if __name__ == '__main__':
    unittest.main()
