import unittest
import requests
from faker import Faker
from service.travel_plan_service import *
from service.test_utils import BASE_URL, headers as test_headers

fake = Faker()


class TestTravelPlanService(unittest.TestCase):
    def setUp(self):
        self.client = requests.Session()
        self.host = BASE_URL

    def test_welcome(self):
        response = welcome(self.client, self.host, test_headers)
        self.assertEqual(response, "Welcome to [ TravelPlan Service ] !")

    def test_get_transfer_result(self):
        info = TransferTravelInfo(start_station=fake.city(), end_station=fake.city())
        result = get_transfer_result(self.client, info, self.host, test_headers)
        self.assertIsInstance(result, TravelPlanResult)

    def test_get_by_cheapest(self):
        query_info = TripInfo(start_place=fake.city(), end_place=fake.city(), departure_time=fake.date_time())
        result = get_by_cheapest(self.client, query_info, self.host, test_headers)
        self.assertIsInstance(result, TravelPlanResult)

    def test_get_by_quickest(self):
        query_info = TripInfo(start_place=fake.city(), end_place=fake.city(), departure_time=fake.date_time())
        result = get_by_quickest(self.client, query_info, self.host, test_headers)
        self.assertIsInstance(result, TravelPlanResult)

    def test_get_by_min_station(self):
        query_info = TripInfo(start_place=fake.city(), end_place=fake.city(), departure_time=fake.date_time())
        result = get_by_min_station(self.client, query_info, self.host, test_headers)
        self.assertIsInstance(result, TravelPlanResult)

    def test_end_to_end(self):
        # Get transfer result
        transfer_info = TransferTravelInfo(start_station=fake.city(), end_station=fake.city())
        transfer_result = get_transfer_result(self.client, transfer_info, self.host, test_headers)
        self.assertIsInstance(transfer_result, TravelPlanResult)

        # Get cheapest plan
        query_info = TripInfo(start_place=fake.city(), end_place=fake.city(), departure_time=fake.date_time())
        cheapest_result = get_by_cheapest(self.client, query_info, self.host, test_headers)
        self.assertIsInstance(cheapest_result, TravelPlanResult)

        # Get quickest plan
        quickest_result = get_by_quickest(self.client, query_info, self.host, test_headers)
        self.assertIsInstance(quickest_result, TravelPlanResult)

        # Get min station plan
        min_station_result = get_by_min_station(self.client, query_info, self.host, test_headers)
        self.assertIsInstance(min_station_result, TravelPlanResult)


if __name__ == '__main__':
    unittest.main()
