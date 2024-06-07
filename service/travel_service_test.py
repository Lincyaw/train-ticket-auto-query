import random

import requests
from dataclasses import asdict
from service.travel_service import *
import unittest
from service.station_service import *
from service.auth_service import DtoLoginUser, users_login
from service.test_utils import BASE_URL, headers
from faker import Faker

fake = Faker()


class TestTravelService(unittest.TestCase):
    def setUp(self):
        self.client = requests.Session()
        self.host = BASE_URL
        basic_auth_dto = DtoLoginUser(username='admin',
                                      password='222222', verificationCode="123")
        token = users_login(self.client, basic_auth_dto, headers, BASE_URL)
        self.client.headers.update({'Authorization': f'Bearer {token}'})

    def test_welcome(self):
        response = welcome(self.client, self.host, headers)
        self.assertEqual(response, "Welcome to [ Travel Service ] !")

    def test_get_train_type_by_trip_id(self):
        trip_id = str(fake.uuid4())
        train_type = get_train_type_by_trip_id(self.client, trip_id, self.host,
                                               headers)
        print(train_type)
        self.assertIsInstance(train_type, ReturnBody)

    def test_get_route_by_trip_id(self):
        trip_id = str(fake.uuid4())
        route = get_route_by_trip_id(self.client, trip_id, self.host, headers)
        self.assertIsInstance(route, ReturnBody)

    def test_get_trips_by_route_id(self):
        route_ids = [str(fake.uuid4()) for _ in range(3)]
        trips = get_trips_by_route_id(self.client, route_ids, self.host,
                                      headers)
        self.assertEquals(trips['status'], 1)

    def test_create_trip(self):
        trip_id = random.choice(
            [start + str(random.randint(10000, 90000))
             for
             start in
             ["Z", "T", "K", "G", "D"]])  # 要求 id 必须以这几个字母开头

        route_ids = TravelInfo(loginId=str(fake.uuid4()),
                               tripId=trip_id,
                               trainTypeName=str(fake.name()),
                               routeId=str(fake.uuid4()),
                               startStationName=str(fake.name()),
                               stationsName=str(fake.name()),
                               terminalStationName=str(fake.name()),
                               startTime=str(fake.date_time()),
                               endTime=str(fake.date_time()))
        response = create_trip(self.client, route_ids, self.host, headers)
        self.assertIsInstance(response, str)
        assert response
        trip = retrieve_trip(self.client, trip_id, self.host, headers)
        print(trip)
        self.assertIsInstance(trip, ReturnBody)

        info = TravelInfo(loginId=str(fake.uuid4()),
                          tripId=trip_id,
                          trainTypeName=str(fake.name()),
                          routeId=str(fake.uuid4()),
                          startStationName=str(fake.name()),
                          stationsName=str(fake.name()),
                          terminalStationName=str(fake.name()),
                          startTime=str(fake.date_time()),
                          endTime=str(fake.date_time()))
        updated_trip = update_trip(self.client, info, self.host, headers)
        self.assertIsInstance(updated_trip, dict)
        print(updated_trip)

        response = delete_trip(self.client, trip_id, self.host, headers)
        self.assertIsInstance(response, str)
        print(response)

    def test_query_trips(self):
        info = TripInfo(
            startPlace=str(fake.city()),
            endPlace=str(fake.city()),
            departureTime="2024-06-06 22:59:00"
        )
        trips = query_trips(self.client, info, self.host, headers)
        self.assertIsInstance(trips, dict)
        print(trips)

    def test_query_trips_in_parallel(self):
        info = TripInfo(
            startPlace=str(fake.city()),
            endPlace=str(fake.city()),
            departureTime="2024-06-06 22:59:00"
        )
        trips = query_trips_in_parallel(self.client, info, self.host, headers)
        print(trips)
        self.assertIsInstance(trips, dict)

    def test_get_trip_all_detail_info(self):
        gtdi = TripAllDetailInfo(tripId=str(fake.uuid4()),
                                 travelDate=str(fake.date_time()),
                                 from_location=str(fake.city()),
                                 to=str(fake.city()))
        detail_info = get_trip_all_detail_info(self.client, gtdi, self.host,
                                               headers)
        self.assertIsInstance(detail_info, dict)

    def test_query_all_trips(self):
        trips = query_all_trips(self.client, self.host, headers)
        print(trips)
        self.assertIsInstance(trips, ReturnBody)

    def test_admin_query_all_trips(self):
        admin_trips = admin_query_all_trips(self.client, self.host, headers)
        print(admin_trips)
        self.assertIsInstance(admin_trips, ReturnBody)

    def test_end_to_end(self):
        # 测试欢迎接口
        response = welcome(self.client, self.host, headers)
        self.assertEqual(response, "Welcome to [ Travel Service ] !")

        # 创建Trip
        route_ids = TravelInfo(loginId=str(fake.uuid4()),
                               tripId=str(fake.uuid4()),
                               trainTypeName=str(fake.name()),
                               routeId=str(fake.uuid4()),
                               startStationName=str(fake.name()),
                               stationsName=str(fake.name()),
                               terminalStationName=str(fake.name()),
                               startTime=str(fake.date_time()),
                               endTime=str(fake.date_time()))
        create_response = create_trip(self.client, route_ids, self.host,
                                      headers)
        self.assertIsInstance(create_response, str)

        # 获取创建的Trip
        created_trip = retrieve_trip(self.client, str(fake.uuid4()), self.host,
                                     headers)
        self.assertIsInstance(created_trip, ReturnBody)

        # 获取TrainType
        train_type = get_train_type_by_trip_id(self.client, str(fake.uuid4()),
                                               self.host, headers)
        self.assertIsInstance(train_type, ReturnBody)

        # 获取Route
        route = get_route_by_trip_id(self.client, str(fake.uuid4()), self.host,
                                     headers)
        self.assertIsInstance(route, ReturnBody)

        # 更新Trip
        update_info = TravelInfo(loginId=str(fake.uuid4()),
                                 tripId=str(fake.uuid4()),
                                 trainTypeName=str(fake.name()),
                                 routeId=str(fake.uuid4()),
                                 startStationName=str(fake.name()),
                                 stationsName=str(fake.name()),
                                 terminalStationName=str(fake.name()),
                                 startTime=str(fake.date_time()),
                                 endTime=str(fake.date_time()))
        updated_trip = update_trip(self.client, update_info, self.host, headers)
        self.assertIsInstance(updated_trip, dict)

        # 查询Trip
        query_info = TripInfo(
            startPlace=str(fake.city()),
            endPlace=str(fake.city()),
            departureTime="2024-06-06 22:59:00"
        )
        queried_trips = query_trips(self.client, query_info, self.host, headers)
        self.assertIsInstance(queried_trips, dict)

        # 并行查询Trip
        queried_parallel_trips = query_trips_in_parallel(self.client,
                                                         query_info, self.host,
                                                         headers)
        self.assertIsInstance(queried_parallel_trips, dict)

        # 获取Trip详细信息
        detail_info = TripAllDetailInfo(tripId=str(fake.uuid4()),
                                        travelDate=str(fake.date_time()),
                                        from_location=str(fake.city()),
                                        to=str(fake.city()))
        trip_detail = get_trip_all_detail_info(self.client, detail_info,
                                               self.host, headers)
        self.assertIsInstance(trip_detail, dict)

        # 删除Trip
        delete_response = delete_trip(self.client, str(fake.uuid4()), self.host,
                                      headers)
        self.assertIsInstance(delete_response, str)


if __name__ == '__main__':
    unittest.main()
