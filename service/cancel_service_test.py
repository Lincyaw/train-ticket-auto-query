import unittest
from service.cancel_service import *
from service.auth_service import DtoLoginUser, users_login
from service.test_utils import BASE_URL, headers
from faker import Faker

fake = Faker()


class TestCancelService(unittest.TestCase):
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

    def test_calculate_refund(self):
        order_id = fake.uuid4()
        response = calculate_refund(self.client, order_id, self.host, self.headers)
        self.assertIsInstance(response, dict)

    def test_cancel_ticket(self):
        order_id = fake.uuid4()
        login_id = fake.uuid4()
        response = cancel_ticket(self.client, order_id, login_id, self.host, self.headers)
        self.assertIsInstance(response, dict)


if __name__ == '__main__':
    unittest.main()
