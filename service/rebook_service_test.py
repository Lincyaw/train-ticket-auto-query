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
        info = RebookInfo(loginId=str(fake.uuid4()),
                          orderId=str(fake.uuid4()),
                          oldTripId=str(fake.uuid4()),
                          tripId=str(fake.uuid4()),
                          seatType=7,
                          date="2024-06-06 14:16:00")
        response = pay_difference(self.client, info, self.host, self.headers)
        self.assertIsInstance(response, dict)

    def test_rebook(self):
        info = RebookInfo(orderId=fake.uuid4(), oldTripId=fake.uuid4(),
                          tripId=fake.uuid4(),
                          date=fake.date(), seatType=fake.word())
        response = rebook(self.client, info, self.host, self.headers)
        self.assertIsInstance(response, dict)

    def test_end_to_end(self):
        # Step 1: Pay difference
        pay_info = RebookInfo(loginId=str(fake.uuid4()),
                              orderId=str(fake.uuid4()),
                              oldTripId=str(fake.uuid4()),
                              tripId=str(fake.uuid4()),
                              seatType=7,
                              date="2024-06-06 14:16:00")
        pay_response = pay_difference(self.client, pay_info, self.host,
                                      self.headers)
        self.assertIsInstance(pay_response, dict)

        # Step 2: Rebook
        rebook_info = RebookInfo(loginId=str(fake.uuid4()),
                                 orderId=str(fake.uuid4()),
                                 oldTripId=str(fake.uuid4()),
                                 tripId=str(fake.uuid4()),
                                 seatType=7,
                                 date="2024-06-06 14:16:00")
        rebook_response = rebook(self.client, rebook_info, self.host,
                                 self.headers)
        self.assertIsInstance(rebook_response, dict)


if __name__ == '__main__':
    unittest.main()
