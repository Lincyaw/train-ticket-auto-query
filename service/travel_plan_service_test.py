import unittest
import requests
from faker import Faker
from service.travel_plan_service import *
from service.test_utils import BASE_URL, headers
from service.auth_service import DtoLoginUser, users_login

fake = Faker()


class TestTravelPlanService(unittest.TestCase):
    def setUp(self):
        self.client = requests.Session()
        self.host = BASE_URL
        basic_auth_dto = DtoLoginUser(username='fdse_microservice',
                                      password='111111', verificationCode="123")
        token = users_login(self.client, basic_auth_dto, headers, BASE_URL)
        self.headers = {'Authorization': f'Bearer {token}'}

    def test_welcome(self):
        response = welcome(self.client, self.host, headers)
        self.assertEqual(response, "Welcome to [ TravelPlan Service ] !")

    def test_get_transfer_result(self):
        info = TransferTravelInfo(startStation="shenzhen",
                                  viaStation="Hong Kong",
                                  endStation="California",
                                  travelDate=str(fake.date_time()),
                                  trainType="AirBus111")
        result = get_transfer_result(self.client, info, self.host, headers)
        print(result)
        self.assertEquals(result['status'], 1)

    def test_get_by_cheapest(self):
        query_info = TripInfo(startPlace=str(fake.city()),
                              endPlace=str(fake.city()),
                              departureTime=str(fake.date_time()))
        result = get_by_cheapest(self.client, query_info, self.host, headers)
        self.assertIsInstance(result, dict)

    def test_get_by_quickest(self):
        query_info = TripInfo(startPlace=str(fake.city()),
                              endPlace=str(fake.city()),
                              departureTime=str(fake.date_time()))
        result = get_by_quickest(self.client, query_info, self.host, headers)
        self.assertIsInstance(result, dict)

    def test_get_by_min_station(self):
        query_info = TripInfo(startPlace=str(fake.city()),
                              endPlace=str(fake.city()),
                              departureTime=str(fake.date_time()))
        result = get_by_min_station(self.client, query_info, self.host, headers)
        self.assertIsInstance(result, dict)




    def test_end_to_end(self):
        # Get transfer result
        transfer_info = TransferTravelInfo(startStation="shenzhen",
                                  viaStation="Hong Kong",
                                  endStation="California",
                                  travelDate=str(fake.date_time()),
                                  trainType="AirBus111")
        transfer_result = get_transfer_result(self.client, transfer_info, self.host, headers)
        self.assertIsInstance(transfer_result, dict)

        # Get cheapest plan
        query_info = TripInfo(startPlace=str(fake.city()),
                              endPlace=str(fake.city()),
                              departureTime=str(fake.date_time()))
        cheapest_result = get_by_cheapest(self.client, query_info, self.host, headers)
        print((cheapest_result))
        self.assertIsInstance(cheapest_result, dict)

        # Get quickest plan
        quickest_result = get_by_quickest(self.client, query_info, self.host, headers)
        print(quickest_result)
        self.assertIsInstance(quickest_result, dict)

        # Get min station plan
        min_station_result = get_by_min_station(self.client, query_info, self.host, headers)
        print(min_station_result)
        self.assertIsInstance(min_station_result, dict)


if __name__ == '__main__':
    unittest.main()
