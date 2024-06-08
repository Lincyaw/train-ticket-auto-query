import unittest
from service.execute_service import *
from service.auth_service import DtoLoginUser, users_login
from service.test_utils import BASE_URL, headers
from faker import Faker

fake = Faker()


class TestExecuteService(unittest.TestCase):
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

    def test_execute_ticket(self):
        order_id = fake.uuid4()
        response = execute_ticket(self.client, order_id, self.host, self.headers)
        self.assertIsInstance(response, ExecuteServiceResult)

    def test_collect_ticket(self):
        order_id = fake.uuid4()
        response = collect_ticket(self.client, order_id, self.host, self.headers)
        self.assertIsInstance(response, ExecuteServiceResult)


if __name__ == '__main__':
    unittest.main()