import unittest
import requests
from faker import Faker
from service.wait_order_service import *
from service.test_utils import BASE_URL, headers
from service.auth_service import DtoLoginUser, users_login

fake = Faker()


class TestWaitListOrderService(unittest.TestCase):
    def setUp(self):
        self.client = requests.Session()
        self.host = BASE_URL
        # basic_auth_dto = DtoLoginUser(username='fdse_microservice',
        #                               password='111111', verificationCode="123")
        basic_auth_dto = DtoLoginUser(username='admin',
                                      password='222222', verificationCode="123")
        token = users_login(self.client, basic_auth_dto, headers, BASE_URL)
        self.headers = {'Authorization': f'Bearer {token}'}

    def test_welcome(self):
        response = welcome(self.client, self.host, headers)
        self.assertEqual(response, "Welcome to [ Wait Order Service ] !")

    def test_create_wait_list_order(self):
        order = WaitListOrderVO(accountId=str(fake.uuid4()),
                                contactsId=str(fake.uuid4()),
                                tripId=str(fake.uuid4()),
                                seatType=7,
                                date=str(fake.date()),
                                from_location=str(fake.city()),
                                to=str(fake.city()),
                                price="648")
        result = create_wait_list_order(self.client, order, self.host, headers)
        self.assertIsInstance(result, WaitListOrderResult)

    def test_get_all_orders(self):
        result = get_all_orders(self.client, self.host, headers)
        self.assertIsInstance(result, ReturnBody)

    def test_get_wait_list_orders(self):
        result = get_wait_list_orders(self.client, self.host, headers)
        self.assertIsInstance(result, ReturnBody)

    def test_end_to_end(self):
        pass
        # # Create a wait list order
        # order = WaitListOrderVO(from_station=fake.city(), to_station=fake.city(), date=fake.date())
        # create_result = create_wait_list_order(self.client, order, self.host, headers)
        # self.assertIsInstance(create_result, WaitListOrderResult)
        #
        # # Get all orders and check if the created order exists
        # all_orders_result = get_all_orders(self.client, self.host, headers)
        # self.assertIsInstance(all_orders_result, GetAllOrdersResult)
        # created_order_exists = any(
        #     order.from_station == o.from_station and order.to_station == o.to_station and order.date == o.date
        #     for o in all_orders_result.data
        # )
        # self.assertTrue(created_order_exists)
        #
        # # Get wait list orders and check if the created order exists
        # wait_list_orders_result = get_wait_list_orders(self.client, self.host, headers)
        # self.assertIsInstance(wait_list_orders_result, GetWaitListOrdersResult)
        # created_order_exists = any(
        #     order.from_station == o.from_station and order.to_station == o.to_station and order.date == o.date
        #     for o in wait_list_orders_result.data
        # )
        # self.assertTrue(created_order_exists)


if __name__ == '__main__':
    unittest.main()
