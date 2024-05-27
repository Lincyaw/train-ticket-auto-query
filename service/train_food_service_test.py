import unittest
from service.train_food_service import *
from service.auth_service import DtoLoginUser, users_login
from service.test_utils import BASE_URL, headers
from faker import Faker

fake = Faker()


class TestTrainFoodService(unittest.TestCase):
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

    def test_list_train_food(self):
        response = list_train_food(self.client, self.host, self.headers)
        self.assertIsInstance(response, list)
        if len(response) > 0:
            self.assertIsInstance(response[0], dict)
            self.assertIn('id', response[0])
            self.assertIn('tripId', response[0])
            self.assertIn('foodName', response[0])
            self.assertIn('price', response[0])

    def test_list_train_food_by_trip_id(self):
        trip_id = fake.uuid4()
        response = list_train_food_by_trip_id(self.client, trip_id, self.host, self.headers)
        self.assertIsInstance(response, list)
        if len(response) > 0:
            self.assertIsInstance(response[0], dict)
            self.assertIn('id', response[0])
            self.assertIn('tripId', response[0])
            self.assertIn('foodName', response[0])
            self.assertIn('price', response[0])


if __name__ == '__main__':
    unittest.main()