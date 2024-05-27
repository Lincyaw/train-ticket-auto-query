import unittest
from service.rebook_service import *
from service.auth_service import DtoLoginUser, users_login
from service.test_utils import BASE_URL, headers
from faker import Faker

fake = Faker()


class TestRebookService(unittest.TestCase):
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

    def test_pay_difference(self):
        info = RebookInfo(orderId=fake.uuid4())
        response = pay_difference(self.client, info, self.host, self.headers)
        self.assertIsInstance(response, dict)

    def test_rebook(self):
        info = RebookInfo(orderId=fake.uuid4(), oldTripId=fake.uuid4(), tripId=fake.uuid4(),
                          date=fake.date(), seatType=fake.word())
        response = rebook(self.client, info, self.host, self.headers)
        self.assertIsInstance(response, dict)

    def test_end_to_end(self):
        # Step 1: Pay difference
        pay_info = RebookInfo(orderId=fake.uuid4())
        pay_response = pay_difference(self.client, pay_info, self.host, self.headers)
        self.assertIsInstance(pay_response, dict)

        # Step 2: Rebook
        rebook_info = RebookInfo(orderId=pay_info.orderId, oldTripId=fake.uuid4(), tripId=fake.uuid4(),
                                 date=fake.date(), seatType=fake.word())
        rebook_response = rebook(self.client, rebook_info, self.host, self.headers)
        self.assertIsInstance(rebook_response, dict)

        # Step 3: Verify the rebook information
        self.assertEqual(rebook_response['orderId'], rebook_info.orderId)
        self.assertEqual(rebook_response['oldTripId'], rebook_info.oldTripId)
        self.assertEqual(rebook_response['tripId'], rebook_info.tripId)
        self.assertEqual(rebook_response['date'], rebook_info.date)
        self.assertEqual(rebook_response['seatType'], rebook_info.seatType)


if __name__ == '__main__':
    unittest.main()