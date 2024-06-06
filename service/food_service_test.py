import random
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

    # def test_test_send_delivery(self):
    #     # delivery = Delivery(foodName=str("HotPot"),
    #     #                     orderId=UUID(fake.uuid4()),
    #     #                     stationName="Shang Hai",
    #     #                     storeName="MiaoTing Instant-Boiled Mutton")
    #     response = test_send_delivery(self.client, self.host)
    #     self.assertTrue(response)

    def test_find_all_food_order(self):
        response = find_all_food_order(self.client, self.host, self.headers)
        self.assertIsInstance(response, QueryAllMessage)

    def test_create_food_order(self):
        food_order = FoodOrder(id := str(fake.uuid4()),
                               orderId := str(fake.uuid4()),
                               foodType=int(7),
                               stationName="Shang Hai",
                               storeName="New Store",
                               foodName="New Food Name",
                               price=float(3.00))
        response = create_food_order(self.client, food_order, self.host, self.headers)
        self.assertEquals(response['status'], 1)

    def test_create_food_batches(self):
        food_order_list = [FoodOrder(id := str(fake.uuid4()),
                                     orderId := str(fake.uuid4()),
                                     foodType=int(7),
                                     stationName="Shang Hai",
                                     storeName="New Store",
                                     foodName="New Food Name",
                                     price=float(random.randrange(3,7))) for _ in range(3)]
        response = create_food_batches(self.client, food_order_list, self.host, self.headers)
        self.assertEquals(response['status'], 1)

    def test_update_food_order(self):
        food_order = FoodOrder(id := "3e43f769-0d87-4c6c-ab16-4285acedccfd",
                               orderId := str(fake.uuid4()),
                               foodType=int(7),
                               stationName="Shang Hai",
                               storeName="New Store",
                               foodName="New Food Name",
                               price=float(3.00))
        response = update_food_order(self.client, food_order, self.host, self.headers)
        self.assertEquals(response['status'], 1)

    def test_delete_food_order(self):
        order_id = "3e60a21a-22ce-4414-818c-0679d461a68a"
        response = delete_food_order(self.client, order_id, self.host, self.headers)
        self.assertIsInstance(response, dict)

    def test_find_food_order_by_order_id(self):
        orderId = "99c0f713-42a8-40ef-8147-9add60284223"
        response = find_food_order_by_order_id(self.client, orderId, self.host, self.headers)
        self.assertIsInstance(response, dict)

    def test_get_all_food(self):
        date = "2024-06-05 06:26:00"
        start_station = "New Store"
        end_station = "shenzhen"
        trip_id = "ee21914f-c6da-4b0b-b8db-aad201e3b690"
        response = get_all_food(self.client, date, start_station, end_station, trip_id, self.host, self.headers)
        self.assertIsInstance(response, dict)


if __name__ == '__main__':
    unittest.main()
