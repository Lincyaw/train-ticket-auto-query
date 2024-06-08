import random
import unittest
from service.admin_route_service import *
from service.auth_service import DtoLoginUser, users_login
from service.test_utils import BASE_URL, headers
from faker import Faker

fake = Faker()


class TestAdminRouteService(unittest.TestCase):
    def setUp(self):
        self.client = requests.Session()
        self.host = BASE_URL
        basic_auth_dto = DtoLoginUser(username='admin',
                                      password='222222', verificationCode="123")
        token = users_login(self.client, basic_auth_dto, headers, BASE_URL)
        self.client.headers.update({'Authorization': f'Bearer {token}'})

    def tearDown(self):
        self.client.close()

    def test_adminroute_welcome(self):
        response = adminroute_welcome(self.client, self.host)
        self.assertIsInstance(response, str)

    def test_get_all_routes(self):
        routes = get_all_routes(self.client, self.host)
        assert isinstance(routes.data, list), "Expected routes to be a list"
        for route in routes.data:
            assert isinstance(route, dict), "Expected each route to be a dictionary"
            assert "id" in route, "Expected 'id' key in route dictionary"
            assert isinstance(route["id"], str), "Expected 'id' to be a string"
            assert "startStation" in route, "Expected 'startStation' key in route dictionary"
            assert isinstance(route["startStation"], str), "Expected 'startStation' to be a string"
            assert "endStation" in route, "Expected 'endStation' key in route dictionary"
            assert isinstance(route["endStation"], str), "Expected 'endStation' to be a string"

    def test_delete_route(self):
        route_id = "1"
        response = delete_route(self.client, route_id, self.host)
        self.assertIsInstance(response, dict)

    def test_create_and_modify_route(self):
        route = RouteInfo(loginId=fake.uuid4(),
                          startStation="shanghai",
                          endStation="taiyuan",
                          stationList="shanghai,The Chinese University of Hong Kong, SZ ,shijiazhuang,taiyuan",
                          distanceList="0,350,1000,1300",
                          id=fake.uuid4())
        response = create_and_modify_route(self.client, route, self.host)
        self.assertIsInstance(response, dict)

    def test_end2end(self):
        """
        End-to-end test: query, add, update, delete
        """
        # 1. Query routes
        routes_before = get_all_routes(self.client, self.host)
        print("Routes before:", routes_before)

        # 2. Add a new route
        new_route = RouteInfo(loginId=fake.uuid4(),
                              startStation="shanghai",
                              endStation="taiyuan",
                              stationList="shanghai,The Chinese University of Hong Kong, SZ ,shijiazhuang,taiyuan",
                              distanceList="0,350,1000,1300",
                              id=fake.uuid4())
        add_response = create_and_modify_route(self.client, new_route, self.host)
        print("New route added:", add_response)

        # 3. Query routes and verify addition
        routes_after_add = get_all_routes(self.client, self.host)
        print("Routes after addition:", routes_after_add)

        # 4. Update the new route
        updated_route = RouteInfo(loginId=fake.uuid4(),
                                  startStation="Shenzhen",
                                  endStation="Hong Kong",
                                  stationList="Shenzhen,The Chinese University of Hong Kong, SZ ,shijiazhuang,Hong Kong",
                                  distanceList="0,450,1200,1500",
                                  id=fake.uuid4())
        update_response = create_and_modify_route(self.client, updated_route, self.host)
        print("Route updated:", update_response)

        # 5. Query routes and verify update
        routes_after_update = get_all_routes(self.client, self.host)
        print("Routes after update:", routes_after_update)

        # 6. Delete the new route
        delete_response = delete_route(self.client, new_route.id, self.host)
        print("Route deleted:", delete_response)

        # 7. Query routes and verify deletion
        routes_after_delete = get_all_routes(self.client, self.host)
        print("Routes after deletion:", routes_after_delete)
        assert not any(route["id"] == new_route.id for route in routes_after_delete.data)


if __name__ == '__main__':
    unittest.main()
