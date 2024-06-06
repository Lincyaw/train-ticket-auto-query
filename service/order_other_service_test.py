import unittest
from service.order_other_service import *
from service.auth_service import DtoLoginUser, users_login
from service.test_utils import BASE_URL, headers
from faker import Faker

fake = Faker()


class TestOrderOtherService(unittest.TestCase):
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
        self.assertIn("Welcome to [ Order Other Service ]", response)

    def test_get_sold_tickets(self):
        seat_request = Seat(travelDate=fake.date())
        response = get_sold_tickets(self.client, self.host, seat_request, self.headers)
        self.assertIsInstance(response, list)

    def test_create_new_order(self):
        order = Order(
            id=fake.uuid4(),
            from_=fake.city(),
            to=fake.city(),
            travelDate=fake.date()
        )
        response = create_new_order(self.client, self.host, order, self.headers)
        self.assertIsInstance(response, bool)

    def test_add_new_order(self):
        order = Order(
            id=fake.uuid4(),
            from_=fake.city(),
            to=fake.city(),
            travelDate=fake.date()
        )
        response = add_new_order(self.client, self.host, order, self.headers)
        self.assertIsInstance(response, bool)

    def test_query_orders(self):
        qi = QueryInfo(loginId=fake.uuid4())
        response = query_orders(self.client, self.host, qi, self.headers)
        self.assertIsInstance(response, list)
        self.assertGreater(len(response), 0)
        self.assertIsInstance(response[0], Order)

    def test_query_orders_for_refresh(self):
        qi = QueryInfo(loginId=fake.uuid4())
        response = query_orders_for_refresh(self.client, self.host, qi, self.headers)
        self.assertIsInstance(response, list)
        self.assertGreater(len(response), 0)
        self.assertIsInstance(response[0], Order)

    def test_calculate_sold_ticket(self):
        travel_date = fake.date()
        train_number = fake.numerify(text="####")
        response = calculate_sold_ticket(self.client, self.host, travel_date, train_number, self.headers)
        self.assertIsInstance(response, int)

    def test_get_order_price(self):
        order_id = fake.uuid4()
        response = get_order_price(self.client, self.host, order_id, self.headers)
        self.assertIsInstance(response, float)

    def test_pay_order(self):
        order_id = fake.uuid4()
        response = pay_order(self.client, self.host, order_id, self.headers)
        self.assertIsInstance(response, bool)

    def test_get_order_by_id(self):
        order_id = fake.uuid4()
        response = get_order_by_id(self.client, self.host, order_id, self.headers)
        self.assertIsInstance(response, Order)

    def test_modify_order(self):
        order_id = fake.uuid4()
        status = fake.random_int(min=0, max=10)
        response = modify_order(self.client, self.host, order_id, status, self.headers)
        self.assertIsInstance(response, bool)

    def test_security_info_check(self):
        check_date = fake.date()
        account_id = fake.uuid4()
        response = security_info_check(self.client, self.host, check_date, account_id, self.headers)
        self.assertIsInstance(response, dict)

    def test_save_order_info(self):
        order_info = Order(
            id=fake.uuid4(),
            from_=fake.city(),
            to=fake.city(),
            travelDate=fake.date()
        )
        response = save_order_info(self.client, self.host, order_info, self.headers)
        self.assertIsInstance(response, bool)

    def test_update_order(self):
        order = Order(
            id=fake.uuid4(),
            from_=fake.city(),
            to=fake.city(),
            travelDate=fake.date()
        )
        response = update_order(self.client, self.host, order, self.headers)
        self.assertIsInstance(response, bool)

    def test_delete_order(self):
        order_id = fake.uuid4()
        response = delete_order(self.client, self.host, order_id, self.headers)
        self.assertIsInstance(response, bool)


    def test_find_all_order(self):
        response = find_all_order(self.client, self.host, self.headers)
        self.assertIsInstance(response, list)
        self.assertGreater(len(response), 0)
        self.assertIsInstance(response[0], Order)

    def test_end_to_end(self):
        # 创建订单
        order = Order(
            id=fake.uuid4(),
            from_=fake.city(),
            to=fake.city(),
            travelDate=fake.date()
        )
        create_response = create_new_order(self.client, self.host, order, self.headers)
        self.assertTrue(create_response)

        # 获取订单
        get_response = get_order_by_id(self.client, self.host, order.id, self.headers)
        self.assertEqual(get_response.id, order.id)

        # 修改订单
        order.from_ = fake.city()
        update_response = update_order(self.client, self.host, order, self.headers)
        self.assertTrue(update_response)

        # 删除订单
        delete_response = delete_order(self.client, self.host, order.id, self.headers)
        self.assertTrue(delete_response)


if __name__ == '__main__':
    unittest.main()