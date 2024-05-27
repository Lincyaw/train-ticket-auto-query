import unittest
import requests
from faker import Faker
from service.wait_order_service import *
from service.test_utils import BASE_URL, headers as test_headers

fake = Faker()


class TestWaitListOrderService(unittest.TestCase):
    def setUp(self):
        self.client = requests.Session()
        self.host = BASE_URL

    def test_welcome(self):
        response = welcome(self.client, self.host, test_headers)
        self.assertEqual(response, "Welcome to [ Wait Order Service ] !")

    def test_create_wait_list_order(self):
        order = WaitListOrderVO(from_station=fake.city(), to_station=fake.city(), date=fake.date())
        result = create_wait_list_order(self.client, order, self.host, test_headers)
        self.assertIsInstance(result, WaitListOrderResult)

    def test_get_all_orders(self):
        result = get_all_orders(self.client, self.host, test_headers)
        self.assertIsInstance(result, GetAllOrdersResult)

    def test_get_wait_list_orders(self):
        result = get_wait_list_orders(self.client, self.host, test_headers)
        self.assertIsInstance(result, GetWaitListOrdersResult)

    def test_end_to_end(self):
        # Create a wait list order
        order = WaitListOrderVO(from_station=fake.city(), to_station=fake.city(), date=fake.date())
        create_result = create_wait_list_order(self.client, order, self.host, test_headers)
        self.assertIsInstance(create_result, WaitListOrderResult)

        # Get all orders and check if the created order exists
        all_orders_result = get_all_orders(self.client, self.host, test_headers)
        self.assertIsInstance(all_orders_result, GetAllOrdersResult)
        created_order_exists = any(
            order.from_station == o.from_station and order.to_station == o.to_station and order.date == o.date
            for o in all_orders_result.data
        )
        self.assertTrue(created_order_exists)

        # Get wait list orders and check if the created order exists
        wait_list_orders_result = get_wait_list_orders(self.client, self.host, test_headers)
        self.assertIsInstance(wait_list_orders_result, GetWaitListOrdersResult)
        created_order_exists = any(
            order.from_station == o.from_station and order.to_station == o.to_station and order.date == o.date
            for o in wait_list_orders_result.data
        )
        self.assertTrue(created_order_exists)


if __name__ == '__main__':
    unittest.main()
