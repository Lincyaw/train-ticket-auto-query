import unittest
from service.station_service import *
from service.auth_service import DtoLoginUser, users_login
from service.test_utils import BASE_URL, headers
from faker import Faker

fake = Faker()


class TestStationService(unittest.TestCase):
    def setUp(self):
        self.client = requests.Session()
        self.host = BASE_URL
        basic_auth_dto = DtoLoginUser(username='admin',
                                      password='222222', verificationCode="123")
        token = users_login(self.client, basic_auth_dto, headers, BASE_URL)
        self.headers = {'Authorization': f'Bearer {token}'}

    def tearDown(self):
        self.client.close()

    def test_home(self):
        response = home(self.client, self.host, self.headers)
        self.assertIsInstance(response, str)

    def test_query_stations(self):
        response = query_stations(self.client, self.host, self.headers)
        self.assertIsInstance(response, dict)

    def test_create_station(self):
        station = Station(name=str(fake.word()),
                          id=str(fake.uuid4()),
                          stayTime=7)
        response = create_station(self.client, station, self.host, self.headers)
        self.assertIsInstance(response, dict)

    def test_update_station(self):
        station = Station(name=str(fake.word()),
                          id=str(fake.uuid4()),
                          stayTime=8)
        response = update_station(self.client, station, self.host, self.headers)
        self.assertIsInstance(response, dict)

    def test_delete_station(self):
        station_id = "0a589682-986c-49a0-aa8b-e548e3c8cb11"
        response = delete_station(self.client, station_id, self.host, self.headers)
        self.assertIsInstance(response, dict)

    def test_query_station_id(self):
        station_name = "life"
        response = query_station_id(self.client, station_name, self.host, self.headers)
        self.assertIsInstance(response, dict)

    def test_query_station_id_batch(self):
        station_names = ["hand", "nanjing", "jiaxingnan"]
        response = query_station_id_batch(self.client, station_names, self.host, self.headers)
        self.assertEquals(response['status'], 1)

    def test_query_station_name(self):
        station_id = "0a589682-986c-49a0-aa8b-e548e3c8cb11"
        response = query_station_name(self.client, station_id, self.host, self.headers)
        self.assertIsInstance(response, dict)

    def test_query_station_name_batch(self):
        station_ids = ["0e212edf-e20b-48c5-a778-decde516a45b", "7f9ce335-9821-4020-988a-956c2a73a267", "b44b0048-5072-40cd-a40e-fde2ee79792a"]
        response = query_station_name_batch(self.client, station_ids, self.host, self.headers)
        self.assertEquals(response['status'], 1)

    def test_end_to_end(self):
        # Step 1: Create a station
        created_station = Station(name=str(fake.word()),
                          id=str(fake.uuid4()),
                          stayTime=7)
        created_response = create_station(self.client, created_station, self.host, self.headers)
        self.assertIsInstance(created_response, dict)

        # Step 2: Query the created station
        queried_station = query_stations(self.client, self.host, self.headers)
        self.assertEquals(queried_station['status'], 1)

        # Step 3: Update the station
        updated_station = Station(name=str(fake.word()),
                          id=str(fake.uuid4()),
                          stayTime=8)
        updated_response = update_station(self.client, updated_station, self.host, self.headers)
        self.assertIsInstance(updated_response, dict)

        # Step 4: Query station ID by name
        station_id = query_station_id(self.client, "taiyuan", self.host, self.headers)
        self.assertEqual(station_id['data'], "961f9505-e88b-4bbf-9418-b9ca8834d4e1")

        # Step 5: Query station name by ID
        station_name = query_station_name(self.client, "b44b0048-5072-40cd-a40e-fde2ee79792a", self.host, self.headers)
        self.assertEqual(station_name['data'], "science")

        # Step 6: Query station IDs by name batch
        station_names = ["newstation", "nanjing", "life"]
        station_ids = query_station_id_batch(self.client, station_names, self.host, self.headers)
        self.assertIsInstance(station_ids, dict)

        # Step 7: Query station names by ID batch
        station_ids = ["c7475434-7fbc-4113-803a-d04248fcb279", "d71c7b77-b09f-4381-b7a1-95ec2388c228"]
        station_names = query_station_name_batch(self.client, station_ids, self.host, self.headers)
        self.assertIsInstance(station_names, dict)

        # Step 8: Delete the station
        delete_response = delete_station(self.client, "d71c7b77-b09f-4381-b7a1-95ec2388c228", self.host, self.headers)
        self.assertIsInstance(delete_response, dict)


if __name__ == '__main__':
    unittest.main()