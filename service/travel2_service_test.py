import unittest
from service.travel2_service import *
from service.auth_service import DtoLoginUser, users_login
from service.test_utils import BASE_URL, headers
from faker import Faker

fake = Faker()


class TestTravel2Service(unittest.TestCase):
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

    def test_get_train_type_by_trip_id(self):
        trip_id = fake.uuid4()
        response = get_train_type_by_trip_id(self.client, trip_id, self.host, self.headers)
        self.assertIsInstance(response, dict)

    def test_get_route_by_trip_id(self):
        trip_id = fake.uuid4()
        response = get_route_by_trip_id(self.client, trip_id, self.host, self.headers)
        self.assertIsInstance(response, dict)

    def test_get_trips_by_route_id(self):
        route_ids = [fake.uuid4() for _ in range(3)]
        response = get_trips_by_route_id(self.client, route_ids, self.host, self.headers)
        self.assertIsInstance(response, dict)

    def test_create_trip(self):
        travel_info = TravelInfo(tripId=fake.uuid4(), trainTypeId=fake.uuid4(), routeId=fake.uuid4(),
                                 startStationName=fake.city(), stationsName=fake.city(),
                                 terminalStationName=fake.city(), startTime=fake.time(),
                                 endTime=fake.time())
        response = create_trip(self.client, travel_info, self.host, self.headers)
        self.assertIsInstance(response, dict)

    def test_retrieve_trip(self):
        trip_id = fake.uuid4()
        response = retrieve_trip(self.client, trip_id, self.host, self.headers)
        self.assertIsInstance(response, dict)

    def test_update_trip(self):
        travel_info = TravelInfo(tripId=fake.uuid4(), trainTypeId=fake.uuid4(), routeId=fake.uuid4(),
                                 startStationName=fake.city(), stationsName=fake.city(),
                                 terminalStationName=fake.city(), startTime=fake.time(),
                                 endTime=fake.time())
        response = update_trip(self.client, travel_info, self.host, self.headers)
        self.assertIsInstance(response, dict)

    def test_delete_trip(self):
        trip_id = fake.uuid4()
        response = delete_trip(self.client, trip_id, self.host, self.headers)
        self.assertIsInstance(response, dict)

    def test_query_trip_info(self):
        trip_info = TripInfo(startPlace=fake.city(), endPlace=fake.city(), departureTime=fake.time())
        response = query_trip_info(self.client, trip_info, self.host, self.headers)
        self.assertIsInstance(response, dict)

    def test_get_trip_all_detail_info(self):
        gtdi = TripAllDetailInfo(tripId=fake.uuid4(), from_date=fake.date(), to_date=fake.date())
        response = get_trip_all_detail_info(self.client, gtdi, self.host, self.headers)
        self.assertIsInstance(response, dict)

    def test_query_all_trips(self):
        response = query_all_trips(self.client, self.host, self.headers)
        self.assertIsInstance(response, dict)

    def test_admin_query_all_trips(self):
        response = admin_query_all_trips(self.client, self.host, self.headers)
        self.assertIsInstance(response, dict)

    def test_end_to_end(self):
        # Step 1: Create a trip
        created_trip = TravelInfo(tripId=fake.uuid4(), trainTypeId=fake.uuid4(), routeId=fake.uuid4(),
                                  startStationName=fake.city(), stationsName=fake.city(),
                                  terminalStationName=fake.city(), startTime=fake.time(),
                                  endTime=fake.time())
        created_response = create_trip(self.client, created_trip, self.host, self.headers)
        self.assertIsInstance(created_response, dict)

        # Step 2: Retrieve the created trip
        retrieved_trip = retrieve_trip(self.client, created_trip.tripId, self.host, self.headers)
        self.assertIsInstance(retrieved_trip, dict)
        self.assertEqual(retrieved_trip['data']['tripId'], created_trip.tripId)

        # Step 3: Update the trip
        updated_trip = TravelInfo(tripId=created_trip.tripId, trainTypeId=fake.uuid4(), routeId=fake.uuid4(),
                                  startStationName=fake.city(), stationsName=fake.city(),
                                  terminalStationName=fake.city(), startTime=fake.time(),
                                  endTime=fake.time())
        updated_response = update_trip(self.client, updated_trip, self.host, self.headers)
        self.assertIsInstance(updated_response, dict)

        # Step 4: Query trip info
        trip_info = TripInfo(startPlace=updated_trip.startStationName, endPlace=updated_trip.terminalStationName,
                             departureTime=updated_trip.startTime)
        queried_trip_info = query_trip_info(self.client, trip_info, self.host, self.headers)
        self.assertIsInstance(queried_trip_info, dict)

        # Step 5: Get trip all detail info
        gtdi = TripAllDetailInfo(tripId=created_trip.tripId, from_date=fake.date(), to_date=fake.date())
        trip_all_detail_info = get_trip_all_detail_info(self.client, gtdi, self.host, self.headers)
        self.assertIsInstance(trip_all_detail_info, dict)

        # Step 6: Query all trips
        all_trips = query_all_trips(self.client, self.host, self.headers)
        self.assertIsInstance(all_trips, dict)

        # Step 7: Admin query all trips
        admin_all_trips = admin_query_all_trips(self.client, self.host, self.headers)
        self.assertIsInstance(admin_all_trips, dict)

        # Step 8: Delete the trip
        deleted_response = delete_trip(self.client, created_trip.tripId, self.host, self.headers)
        self.assertIsInstance(deleted_response, dict)


if __name__ == '__main__':
    unittest.main()