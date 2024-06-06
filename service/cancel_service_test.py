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
        self.assertIsInstance(response, cancelResponse)

    def test_cancel_ticket(self):
        order_id = fake.uuid4()
        login_id = fake.uuid4()
        response = cancel_ticket(self.client, order_id, login_id, self.host, self.headers)
        self.assertIsInstance(response, cancelResponse)

    def test_cancel_service_workflow(self):
        # Test welcome
        welcome_response = welcome(self.client, self.host, self.headers)
        self.assertIsInstance(welcome_response, str)

        # Create a new order (you need to implement the create_order function)
        order_id = fake.uuid4()

        # Calculate refund for the order
        refund_response = calculate_refund(self.client, order_id, self.host, self.headers)
        self.assertIsInstance(refund_response, cancelResponse)

        # Cancel the ticket
        login_id = fake.uuid4()
        cancel_response = cancel_ticket(self.client, order_id, login_id, self.host, self.headers)
        self.assertIsInstance(cancel_response, cancelResponse)

        # # Verify that the order is cancelled (you need to implement the is_order_cancelled function)
        # self.assertTrue(is_order_cancelled(self.client, order_id, self.host, self.headers))

if __name__ == '__main__':
    unittest.main()
