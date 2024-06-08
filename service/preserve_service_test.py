import unittest
from service.preserve_service import *
from service.auth_service import DtoLoginUser, users_login
from service.test_utils import BASE_URL, headers
from faker import Faker

fake = Faker()


class TestPreserveService(unittest.TestCase):
    def setUp(self):
        self.client = requests.Session()
        self.host = BASE_URL
        basic_auth_dto = DtoLoginUser(username='fdse_microservice',
                                      password='111111', verificationCode="123")
        token = users_login(self.client, basic_auth_dto, headers, BASE_URL)
        self.headers = {'Authorization': f'Bearer {token}'}

    def tearDown(self):
        self.client.close()

    def test_home(self):
        response = home(self.client, self.host)
        self.assertIsInstance(response, str)

    def test_preserve(self):
        oti = OrderTicketsInfo(
            from_=fake.city(),
            to=fake.city(),
            date=fake.date()
        )
        response = preserve(self.client, oti, self.host, self.headers)
        self.assertIsInstance(response, dict)

    def test_end_to_end(self):
        pass


if __name__ == '__main__':
    unittest.main()