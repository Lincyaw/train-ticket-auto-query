import unittest
from service.food_delivery_service import *
from service.auth_service import DtoLoginUser, users_login
from service.test_utils import BASE_URL, headers
from faker import Faker

fake = Faker()


class TestFoodDeliveryService(unittest.TestCase):
    def setUp(self):
        self.client = requests.Session()
        self.host = BASE_URL
        basic_auth_dto = DtoLoginUser(username='admin',
                                      password='222222', verificationCode="123")
        token = users_login(self.client, basic_auth_dto, headers, BASE_URL)
        self.headers = {'Authorization': f'Bearer {token}'}

    def tearDown(self):
        self.client.close()

    def test_home(self):
        response = home(self.client, self.host)
        self.assertIsInstance(response, str)

    def test_create_food_delivery_order(self):
        food_1 = Food(foodName="chicken meal",
                      price=float(10.00))
        food_2 = Food(foodName="spaghetti",
                      price=float(10.00))
        fd = FoodDeliveryOrder(id=str(fake.uuid4()),
                               stationFoodStoreId=str(fake.uuid4()),
                               foodList=[food_1, food_2],
                               tripId=str(fake.uuid4()),
                               seatNo=int(777),
                               createdTime=str("2024-06-05 06:26:00"),
                               deliveryTime=str("2024-06-05 20:37:00"),
                               deliveryFee=float(5.00))

        response = create_food_delivery_order(self.client, fd, self.host, self.headers)
        self.assertIsInstance(response, FoodDeliveryOrder)

    def test_delete_food_delivery_order(self):
        order_id = fake.uuid4()
        response = delete_food_delivery_order(self.client, order_id, self.host, self.headers)
        self.assertIsInstance(response, dict)

    def test_get_food_delivery_order_by_id(self):
        order_id = fake.uuid4()
        response = get_food_delivery_order_by_id(self.client, order_id, self.host, self.headers)
        self.assertIsInstance(response, FoodDeliveryOrder)

    def test_get_all_food_delivery_orders(self):
        response = get_all_food_delivery_orders(self.client, self.host, self.headers)
        self.assertIsInstance(response, list)

    def test_get_food_delivery_order_by_store_id(self):
        store_id = fake.uuid4()
        response = get_food_delivery_order_by_store_id(self.client, store_id, self.host, self.headers)
        self.assertIsInstance(response, list)

    def test_update_trip_id(self):
        trip_order_info = TripOrderInfo()
        response = update_trip_id(self.client, trip_order_info, self.host, self.headers)
        self.assertIsInstance(response, TripOrderInfo)

    def test_update_seat_no(self):
        seat_info = SeatInfo()
        response = update_seat_no(self.client, seat_info, self.host, self.headers)
        self.assertIsInstance(response, SeatInfo)

    def test_update_delivery_time(self):
        delivery_info = DeliveryInfo()
        response = update_delivery_time(self.client, delivery_info, self.host, self.headers)
        self.assertIsInstance(response, DeliveryInfo)


if __name__ == '__main__':
    unittest.main()
