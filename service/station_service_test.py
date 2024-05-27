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
        basic_auth_dto = DtoLoginUser(username='fdse_microservice',
                                      password='111111', verificationCode="123")
        token = users_login(self.client, basic_auth_dto, headers, BASE_URL)
        self.headers = {'Authorization': f'Bearer {token}'}

    def tearDown(self):
        self.client.close()

    def test_home(self):
        response = home(self.client, self.host, self.headers)
        self.assertIsInstance(response, str)

    def test_query_stations(self):
        response = query_stations(self.client, self.host, self.headers)
        self.assertIsInstance(response, list)

    def test_create_station(self):
        station = Station(name=fake.word())
        response = create_station(self.client, station, self.host, self.headers)
        self.assertIsInstance(response, dict)

    def test_update_station(self):
        station = Station(id=fake.uuid4(), name=fake.word())
        response = update_station(self.client, station, self.host, self.headers)
        self.assertIsInstance(response, dict)

    def test_delete_station(self):
        station_id = fake.uuid4()
        response = delete_station(self.client, station_id, self.host, self.headers)
        self.assertIsInstance(response, dict)

    def test_query_station_id(self):
        station_name = fake.word()
        response = query_station_id(self.client, station_name, self.host, self.headers)
        self.assertIsInstance(response, str)

    def test_query_station_id_batch(self):
        station_names = [fake.word() for _ in range(3)]
        response = query_station_id_batch(self.client, station_names, self.host, self.headers)
        self.assertIsInstance(response, list)

    def test_query_station_name(self):
        station_id = fake.uuid4()
        response = query_station_name(self.client, station_id, self.host, self.headers)
        self.assertIsInstance(response, str)

    def test_query_station_name_batch(self):
        station_ids = [fake.uuid4() for _ in range(3)]
        response = query_station_name_batch(self.client, station_ids, self.host, self.headers)
        self.assertIsInstance(response, list)

    def test_end_to_end(self):
        # Step 1: Create a station
        created_station = Station(name=fake.word())
        created_response = create_station(self.client, created_station, self.host, self.headers)
        self.assertIsInstance(created_response, dict)
        created_station.id = created_response['id']

        # Step 2: Query the created station
        queried_station = query_stations(self.client, self.host, self.headers)
        self.assertIsInstance(queried_station, list)
        self.assertIn(created_station.id, [s['id'] for s in queried_station])

        # Step 3: Update the station
        updated_station = Station(id=created_station.id, name=fake.word())
        updated_response = update_station(self.client, updated_station, self.host, self.headers)
        self.assertIsInstance(updated_response, dict)

        # Step 4: Query station ID by name
        station_id = query_station_id(self.client, updated_station.name, self.host, self.headers)
        self.assertEqual(station_id, updated_station.id)

        # Step 5: Query station name by ID
        station_name = query_station_name(self.client, updated_station.id, self.host, self.headers)
        self.assertEqual(station_name, updated_station.name)

        # Step 6: Query station IDs by name batch
        station_names = [fake.word() for _ in range(3)]
        station_ids = query_station_id_batch(self.client, station_names, self.host, self.headers)
        self.assertIsInstance(station_ids, list)

        # Step 7: Query station names by ID batch
        station_ids = [fake.uuid4() for _ in range(3)]
        station_names = query_station_name_batch(self.client, station_ids, self.host, self.headers)
        self.assertIsInstance(station_names, list)

        # Step 8: Delete the station
        delete_response = delete_station(self.client, created_station.id, self.host, self.headers)
        self.assertIsInstance(delete_response, dict)


if __name__ == '__main__':
    unittest.main()