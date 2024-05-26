import unittest
from service.basic_service import *
from service.auth_service import DtoLoginUser, users_login
from service.test_utils import BASE_URL, headers
from faker import Faker

fake = Faker()


class TestBasicService(unittest.TestCase):
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

    def test_query_for_travel(self):
        travel = Travel(tripId=fake.random_int(),
                        trainTypeId=fake.random_int(),
                        startStationName=fake.city(),
                        startTime=str(fake.date_time()),
                        endStationName=fake.city(),
                        arriveTime=str(fake.date_time()))
        response = query_for_travel(self.client, travel, self.host, self.headers)
        self.assertIsInstance(response, TravelResult)

    def test_query_for_travels(self):
        travels = [Travel(tripId=fake.random_int(),
                          trainTypeId=fake.random_int(),
                          startStationName=fake.city(),
                          startTime=str(fake.date_time()),
                          endStationName=fake.city(),
                          arriveTime=str(fake.date_time())) for _ in range(3)]
        response = query_for_travels(self.client, travels, self.host, self.headers)
        self.assertIsInstance(response, TravelResult)

    def test_query_for_station_id(self):
        station_name = fake.city()
        response = query_for_station_id(self.client, station_name, self.host, self.headers)
        self.assertIsInstance(response, str)


if __name__ == '__main__':
    unittest.main()
