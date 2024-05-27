import unittest
from service.payment_service import *
from service.auth_service import DtoLoginUser, users_login
from service.test_utils import BASE_URL, headers
from faker import Faker

fake = Faker()


class TestPaymentService(unittest.TestCase):
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
        info = Payment(id=fake.uuid4())
        response = pay(self.client, info, self.host, self.headers)
        self.assertIsInstance(response, dict)

    def test_add_money(self):
        info = Payment(id=fake.uuid4())
        response = add_money(self.client, info, self.host, self.headers)
        self.assertIsInstance(response, dict)

    def test_query(self):
        response = query(self.client, self.host, self.headers)
        self.assertIsInstance(response, list)

    def test_end_to_end(self):
        # Step 1: Query initial payment status
        initial_query_response = query(self.client, self.host, self.headers)
        self.assertIsInstance(initial_query_response, list)

        # Step 2: Add money to the payment
        payment_id = fake.uuid4()
        add_money_info = Payment(id=payment_id)
        add_money_response = add_money(self.client, add_money_info, self.host, self.headers)
        self.assertIsInstance(add_money_response, dict)

        # Step 3: Make a payment
        pay_info = Payment(id=payment_id)
        pay_response = pay(self.client, pay_info, self.host, self.headers)
        self.assertIsInstance(pay_response, dict)

        # Step 4: Query updated payment status
        updated_query_response = query(self.client, self.host, self.headers)
        self.assertIsInstance(updated_query_response, list)

        # Step 5: Verify the payment status has changed
        self.assertNotEqual(initial_query_response, updated_query_response)


if __name__ == '__main__':
    unittest.main()