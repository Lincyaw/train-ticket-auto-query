import unittest
from service.station_food_service import *
from service.auth_service import DtoLoginUser, users_login
from service.test_utils import BASE_URL, headers
from faker import Faker

fake = Faker()


class TestStationFoodService(unittest.TestCase):
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

    def test_list_food_stores(self):
        response = list_food_stores(self.client, self.host, self.headers)
        self.assertIsInstance(response, list)

    def test_list_food_stores_by_station_name(self):
        station_name = fake.word()
        response = list_food_stores_by_station_name(self.client, station_name, self.host, self.headers)
        self.assertIsInstance(response, list)

    def test_get_food_stores_by_station_names(self):
        station_names = [fake.word() for _ in range(3)]
        response = get_food_stores_by_station_names(self.client, station_names, self.host)
        self.assertIsInstance(response, list)

    def test_get_food_list_by_store_id(self):
        store_id = fake.uuid4()
        response = get_food_list_by_store_id(self.client, store_id, self.host, self.headers)
        self.assertIsInstance(response, dict)

    def test_end_to_end(self):
        # Step 1: List all food stores
        all_stores = list_food_stores(self.client, self.host, self.headers)
        self.assertIsInstance(all_stores, list)

        if len(all_stores) > 0:
            # Step 2: List food stores by station name
            station_name = all_stores[0]['stationName']
            station_stores = list_food_stores_by_station_name(self.client, station_name, self.host, self.headers)
            self.assertIsInstance(station_stores, list)

            # Step 3: Get food stores by station names
            station_names = [store['stationName'] for store in all_stores[:3]]
            stores_by_names = get_food_stores_by_station_names(self.client, station_names, self.host)
            self.assertIsInstance(stores_by_names, list)

            # Step 4: Get food list by store ID
            store_id = all_stores[0]['id']
            food_list = get_food_list_by_store_id(self.client, store_id, self.host, self.headers)
            self.assertIsInstance(food_list, dict)


if __name__ == '__main__':
    unittest.main()