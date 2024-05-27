import unittest
import requests
from dataclasses import asdict
from faker import Faker
from service.travel_service import *
from service.test_utils import BASE_URL, headers as test_headers

fake = Faker()

class TestTravelService(unittest.TestCase):
    def setUp(self):
        self.client = requests.Session()
        self.host = BASE_URL

    def test_welcome(self):
        response = welcome(self.client, self.host, test_headers)
        self.assertEqual(response, "Welcome to [ Travel Service ] !")

    def test_get_train_type_by_trip_id(self):
        trip_id = fake.uuid4()
        train_type = get_train_type_by_trip_id(self.client, trip_id, self.host, test_headers)
        self.assertIsInstance(train_type, TrainType)

    def test_get_route_by_trip_id(self):
        trip_id = fake.uuid4()
        route = get_route_by_trip_id(self.client, trip_id, self.host, test_headers)
        self.assertIsInstance(route, Route)

    def test_get_trips_by_route_id(self):
        route_ids = [fake.uuid4() for _ in range(3)]
        trips = get_trips_by_route_id(self.client, route_ids, self.host, test_headers)
        self.assertIsInstance(trips, list)
        self.assertGreater(len(trips), 0)
        self.assertIsInstance(trips[0], Trip)

    def test_create_trip(self):
        route_ids = TravelInfo(trip_id=fake.uuid4())
        response = create_trip(self.client, route_ids, self.host, test_headers)
        self.assertIsInstance(response, str)

    def test_retrieve_trip(self):
        trip_id = fake.uuid4()
        trip = retrieve_trip(self.client, trip_id, self.host, test_headers)
        self.assertIsInstance(trip, Trip)

    def test_update_trip(self):
        info = TravelInfo(trip_id=fake.uuid4())
        updated_trip = update_trip(self.client, info, self.host, test_headers)
        self.assertIsInstance(updated_trip, Trip)

    def test_delete_trip(self):
        trip_id = fake.uuid4()
        response = delete_trip(self.client, trip_id, self.host, test_headers)
        self.assertIsInstance(response, str)

    def test_query_trips(self):
        info = TripInfo(
            start_place=fake.city(),
            end_place=fake.city(),
            departure_time=fake.date_time().isoformat()
        )
        trips = query_trips(self.client, info, self.host, test_headers)
        self.assertIsInstance(trips, list)
        self.assertIsInstance(trips[0], TripResponse)

    def test_query_trips_in_parallel(self):
        info = TripInfo(
            start_place=fake.city(),
            end_place=fake.city(),
            departure_time=fake.date_time().isoformat()
        )
        trips = query_trips_in_parallel(self.client, info, self.host, test_headers)
        self.assertIsInstance(trips, list)
        self.assertIsInstance(trips[0], TripResponse)

    def test_get_trip_all_detail_info(self):
        gtdi = TripAllDetailInfo(trip_id=fake.uuid4())
        detail_info = get_trip_all_detail_info(self.client, gtdi, self.host, test_headers)
        self.assertIsInstance(detail_info, dict)

    def test_query_all_trips(self):
        trips = query_all_trips(self.client, self.host, test_headers)
        self.assertIsInstance(trips, list)
        self.assertIsInstance(trips[0], Trip)

    def test_admin_query_all_trips(self):
        admin_trips = admin_query_all_trips(self.client, self.host, test_headers)
        self.assertIsInstance(admin_trips, list)
        self.assertIsInstance(admin_trips[0], AdminTrip)

    def test_end_to_end(self):
        # 测试欢迎接口
        response = welcome(self.client, self.host, test_headers)
        self.assertEqual(response, "Welcome to [ Travel Service ] !")

        # 创建Trip
        route_ids = TravelInfo(trip_id=fake.uuid4())
        create_response = create_trip(self.client, route_ids, self.host, test_headers)
        self.assertIsInstance(create_response, str)

        # 获取创建的Trip
        created_trip = retrieve_trip(self.client, route_ids.trip_id, self.host, test_headers)
        self.assertIsInstance(created_trip, Trip)

        # 获取TrainType
        train_type = get_train_type_by_trip_id(self.client, created_trip.tripId, self.host, test_headers)
        self.assertIsInstance(train_type, TrainType)

        # 获取Route
        route = get_route_by_trip_id(self.client, created_trip.tripId, self.host, test_headers)
        self.assertIsInstance(route, Route)

        # 更新Trip
        update_info = TravelInfo(trip_id=created_trip.tripId)
        updated_trip = update_trip(self.client, update_info, self.host, test_headers)
        self.assertIsInstance(updated_trip, Trip)

        # 查询Trip
        query_info = TripInfo(
            start_place=route.startStation,
            end_place=route.terminalStation,
            departure_time=created_trip.startingTime
        )
        queried_trips = query_trips(self.client, query_info, self.host, test_headers)
        self.assertIsInstance(queried_trips, list)
        self.assertIn(created_trip.tripId, [trip.tripId for trip in queried_trips])

        # 并行查询Trip
        queried_parallel_trips = query_trips_in_parallel(self.client, query_info, self.host, test_headers)
        self.assertIsInstance(queried_parallel_trips, list)
        self.assertIn(created_trip.tripId, [trip.tripId for trip in queried_parallel_trips])

        # 获取Trip详细信息
        detail_info = TripAllDetailInfo(trip_id=created_trip.tripId)
        trip_detail = get_trip_all_detail_info(self.client, detail_info, self.host, test_headers)
        self.assertIsInstance(trip_detail, dict)

        # 删除Trip
        delete_response = delete_trip(self.client, created_trip.tripId, self.host, test_headers)
        self.assertIsInstance(delete_response, str)

        # 验证Trip已删除
        queried_trips_after_delete = query_trips(self.client, query_info, self.host, test_headers)
        self.assertNotIn(created_trip.tripId, [trip.tripId for trip in queried_trips_after_delete])

if __name__ == '__main__':
    unittest.main()