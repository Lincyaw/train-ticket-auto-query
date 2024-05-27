import unittest
from service.food_service import *
from service.auth_service import DtoLoginUser, users_login
from service.test_utils import BASE_URL, headers
from faker import Faker

fake = Faker()


class TestFoodService(unittest.TestCase):
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

    def test_test_send_delivery(self):
        delivery = Delivery(foodName=fake.name(),
                            orderId=fake.uuid4(),
                            stationName=fake.city(),
                            storeName=fake.company())
        response = test_send_delivery(self.client, delivery, self.host)
        self.assertTrue(response)

    def test_find_all_food_order(self):
        response = find_all_food_order(self.client, self.host, self.headers)
        self.assertIsInstance(response, list)

    def test_create_food_order(self):
        food_order = FoodOrder()
        response = create_food_order(self.client, food_order, self.host, self.headers)
        self.assertIsInstance(response, FoodOrder)

    def test_create_food_batches(self):
        food_order_list = [FoodOrder() for _ in range(3)]
        response = create_food_batches(self.client, food_order_list, self.host, self.headers)
        self.assertIsInstance(response, list)

    def test_update_food_order(self):
        food_order = FoodOrder()
        response = update_food_order(self.client, food_order, self.host, self.headers)
        self.assertIsInstance(response, FoodOrder)

    def test_delete_food_order(self):
        order_id = fake.uuid4()
        response = delete_food_order(self.client, order_id, self.host, self.headers)
        self.assertIsInstance(response, dict)

    def test_find_food_order_by_order_id(self):
        order_id = fake.uuid4()
        response = find_food_order_by_order_id(self.client, order_id, self.host, self.headers)
        self.assertIsInstance(response, FoodOrder)

    def test_get_all_food(self):
        date = fake.date()
        start_station = fake.city()
        end_station = fake.city()
        trip_id = fake.uuid4()
        response = get_all_food(self.client, date, start_station, end_station, trip_id, self.host, self.headers)
        self.assertIsInstance(response, list)


if __name__ == '__main__':
    unittest.main()