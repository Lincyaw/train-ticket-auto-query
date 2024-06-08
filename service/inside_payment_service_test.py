import unittest
from service.inside_payment_service import *
from service.auth_service import DtoLoginUser, users_login
from service.test_utils import BASE_URL, headers
from faker import Faker

fake = Faker()


class TestInsidePaymentService(unittest.TestCase):
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

    def test_pay(self):
        info = PaymentInfo(orderId=fake.uuid4())
        response = pay(self.client, info, self.host, self.headers)
        self.assertIsInstance(response, dict)

    def test_create_account(self):
        info = AccountInfo()
        response = create_account(self.client, info, self.host, self.headers)
        self.assertIsInstance(response, dict)

    def test_add_money(self):
        user_id = fake.uuid4()
        money = str(fake.random_int(min=1, max=1000))
        response = add_money(self.client, user_id, money, self.host, self.headers)
        self.assertIsInstance(response, dict)

    def test_query_payment(self):
        response = query_payment(self.client, self.host, self.headers)
        self.assertIsInstance(response, dict)

    def test_query_account(self):
        response = query_account(self.client, self.host, self.headers)
        self.assertIsInstance(response, dict)

    def test_draw_back(self):
        user_id = fake.uuid4()
        money = str(fake.random_int(min=1, max=1000))
        response = draw_back(self.client, user_id, money, self.host, self.headers)
        self.assertIsInstance(response, dict)

    def test_pay_difference(self):
        info = PaymentInfo(orderId=fake.uuid4())
        response = pay_difference(self.client, info, self.host, self.headers)
        self.assertIsInstance(response, dict)

    def test_query_add_money(self):
        response = query_add_money(self.client, self.host, self.headers)
        self.assertIsInstance(response, dict)


if __name__ == '__main__':
    unittest.main()