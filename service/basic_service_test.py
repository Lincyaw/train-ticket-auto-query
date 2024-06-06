import unittest
from random import random
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
        TRIPID = TripId(type=int,
                        number="7777")

        TRIP = Trip(id=str(fake.uuid4()),
                    tripId=TRIPID,
                    trainTypeName="QianNianSunHao",
                    routeId=str(fake.uuid4()),
                    startStationName="shanghai",
                    stationsName="suzhou",
                    terminalStationName="taiyuan",
                    startTime="2024-06-02 09:00:00",
                    endTime="2014-06-02 15:51:52")

        info = Travel(trip=TRIP,
                      startPlace="shanghai",
                      endPlace="shenzhen",
                      departureTime="2024-06-02 16:21:00")
        response = query_for_travel(self.client, info, self.host, self.headers)
        self.assertIsInstance(response, TravelResult)

    def test_query_for_travels(self):
        TRIPID = TripId(type=int,
                        number="7777")

        TRIP = Trip(id=str(fake.uuid4()),
                    tripId=TRIPID,
                    trainTypeName="QianNianSunHao",
                    routeId=str(fake.uuid4()),
                    startStationName="shanghai",
                    stationsName="suzhou",
                    terminalStationName="taiyuan",
                    startTime="2024-06-02 09:00:00",
                    endTime="2014-06-02 15:51:52")

        travels = [Travel(trip=TRIP,
                          startPlace="shanghai",
                          endPlace="shenzhen",
                          departureTime="2024-06-02 16:21:00") for _ in range(3)]
        response = query_for_travels(self.client, travels, self.host, self.headers)
        self.assertIsInstance(response, TravelResult)

    def test_query_for_station_id(self):
        station_name = "shanghai"
        response = query_for_station_id(self.client, station_name, self.host, self.headers)
        self.assertIsInstance(response, dict)

    def test_end_to_end(self):
        # Test welcome
        welcome_response = welcome(self.client, self.host, self.headers)
        self.assertIsInstance(welcome_response, str)

        # Test query for station ID
        station_name = "shanghai"
        station_id_response = query_for_station_id(self.client, station_name, self.host, self.headers)
        self.assertIsInstance(station_id_response, dict)

        # Test query for travel
        TRIPID = TripId(type=int,
                        number="7777")

        TRIP = Trip(id=str(fake.uuid4()),
                    tripId=TRIPID,
                    trainTypeName="QianNianSunHao",
                    routeId=str(fake.uuid4()),
                    startStationName="shanghai",
                    stationsName="suzhou",
                    terminalStationName="taiyuan",
                    startTime="2024-06-02 09:00:00",
                    endTime="2014-06-02 15:51:52")

        info = Travel(trip=TRIP,
                      startPlace="shanghai",
                      endPlace="shenzhen",
                      departureTime="2024-06-02 16:21:00")
        travel_response = query_for_travel(self.client, info, self.host, self.headers)
        self.assertIsInstance(travel_response, TravelResult)

        # Test query for travels
        travels = [Travel(trip=TRIP,
                          startPlace="shanghai",
                          endPlace="shenzhen",
                          departureTime="2024-06-02 16:21:00") for _ in range(3)]
        travels_response = query_for_travels(self.client, travels, self.host, self.headers)
        self.assertIsInstance(travels_response, TravelResult)


if __name__ == '__main__':
    unittest.main()
