import unittest
from service.route_service import *
from service.auth_service import DtoLoginUser, users_login
from service.test_utils import BASE_URL, headers
from faker import Faker

fake = Faker()


class TestRouteService(unittest.TestCase):
    def setUp(self):
        self.client = requests.Session()
        self.host = BASE_URL
        basic_auth_dto = DtoLoginUser(username='fdse_microservice',
                                      password='111111', verificationCode="123")
        token = users_login(self.client, basic_auth_dto, headers, BASE_URL)
        self.headers = {'Authorization': f'Bearer {token}'}

    def tearDown(self):
        self.client.close()

    def test_route_welcome(self):
        response = route_welcome(self.client, self.host)
        self.assertIsInstance(response, str)

    def test_create_and_modify_route(self):
        route = RouteInfo(id=fake.uuid4(),
                          startStation=fake.city(),
                          endStation=fake.city(),
                          stationList=[fake.city() for _ in range(3)],
                          distanceList=[fake.pyfloat(min_value=0, max_value=100) for _ in range(3)])
        response = create_and_modify_route(self.client, route, self.host, self.headers)
        self.assertIsInstance(response, dict)

    def test_delete_route(self):
        route_id = fake.uuid4()
        response = delete_route(self.client, route_id, self.host, self.headers)
        self.assertIsInstance(response, dict)

    def test_query_by_id(self):
        route_id = fake.uuid4()
        response = query_by_id(self.client, route_id, self.host, self.headers)
        self.assertIsInstance(response, dict)

    def test_query_by_ids(self):
        route_ids = [fake.uuid4() for _ in range(3)]
        response = query_by_ids(self.client, route_ids, self.host, self.headers)
        self.assertIsInstance(response, dict)

    def test_query_all(self):
        routes = query_all(self.client, self.host, self.headers)
        self.assertIsInstance(routes, Route)

    def test_query_by_start_and_terminal(self):
        start = fake.city()
        end = fake.city()
        response = query_by_start_and_terminal(self.client, start, end, self.host, self.headers)
        self.assertIsInstance(response, dict)

    def test_end2end(self):
        # Query all routes
        all_routes = query_all(self.client, self.host, self.headers)
        print("All routes:", all_routes)

        # Create a new route
        new_route = RouteInfo(id=fake.uuid4(),
                              startStation=fake.city(),
                              endStation=fake.city(),
                              stationList=[fake.city() for _ in range(3)],
                              distanceList=[fake.pyfloat(min_value=0, max_value=100) for _ in range(3)])
        create_response = create_and_modify_route(self.client, new_route, self.host, self.headers)
        print("Create route response:", create_response)

        # Query the new route
        query_response = query_by_id(self.client, new_route.id, self.host, self.headers)
        print("Query route response:", query_response)

        # Delete the new route
        delete_response = delete_route(self.client, new_route.id, self.host, self.headers)
        print("Delete route response:", delete_response)


if __name__ == '__main__':
    unittest.main()