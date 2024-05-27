import unittest
from service.order_service import *
from service.auth_service import DtoLoginUser, users_login
from service.test_utils import BASE_URL, headers
from faker import Faker

fake = Faker()


class TestOrderService(unittest.TestCase):
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

    def test_get_sold_tickets(self):
        seat_request = Seat(travelDate=fake.date())
        response = get_sold_tickets(self.client, seat_request, self.host, self.headers)
        self.assertIsInstance(response, str)

    def test_create_new_order(self):
        order = Order(
            id=fake.uuid4(),
            from_=fake.city(),
            to=fake.city(),
            travelDate=fake.date()
        )
        response = create_new_order(self.client, order, self.host, self.headers)
        self.assertIsInstance(response, dict)

    def test_add_new_order(self):
        order = Order(
            id=fake.uuid4(),
            from_=fake.city(),
            to=fake.city(),
            travelDate=fake.date()
        )
        response = add_new_order(self.client, order, self.host, self.headers)
        self.assertIsInstance(response, dict)

    def test_query_orders(self):
        qi = OrderInfo(loginId=fake.user_name())
        response = query_orders(self.client, qi, self.host, self.headers)
        self.assertIsInstance(response, list)

    def test_query_orders_for_refresh(self):
        qi = OrderInfo(loginId=fake.user_name())
        response = query_orders_for_refresh(self.client, qi, self.host, self.headers)
        self.assertIsInstance(response, list)

    def test_calculate_sold_ticket(self):
        travel_date = fake.date()
        train_number = fake.numerify(text='####')
        response = calculate_sold_ticket(self.client, travel_date, train_number, self.host, self.headers)
        self.assertIsInstance(response, dict)

    def test_get_order_price(self):
        order_id = fake.uuid4()
        response = get_order_price(self.client, order_id, self.host, self.headers)
        self.assertIsInstance(response, dict)

    def test_pay_order(self):
        order_id = fake.uuid4()
        response = pay_order(self.client, order_id, self.host, self.headers)
        self.assertIsInstance(response, dict)

    def test_get_order_by_id(self):
        order_id = fake.uuid4()
        response = get_order_by_id(self.client, order_id, self.host, self.headers)
        self.assertIsInstance(response, dict)

    def test_modify_order(self):
        order_id = fake.uuid4()
        status = fake.random_int(min=0, max=2)
        response = modify_order(self.client, order_id, status, self.host, self.headers)
        self.assertIsInstance(response, dict)

    def test_security_info_check(self):
        check_date = fake.date()
        account_id = fake.uuid4()
        response = security_info_check(self.client, check_date, account_id, self.host, self.headers)
        self.assertIsInstance(response, dict)

    def test_save_order_info(self):
        order_info = Order(
            id=fake.uuid4(),
            from_=fake.city(),
            to=fake.city(),
            travelDate=fake.date()
        )
        response = save_order_info(self.client, order_info, self.host, self.headers)
        self.assertIsInstance(response, dict)

    def test_update_order(self):
        order = Order(
            id=fake.uuid4(),
            from_=fake.city(),
            to=fake.city(),
            travelDate=fake.date()
        )
        response = update_order(self.client, order, self.host, self.headers)
        self.assertIsInstance(response, dict)

    def test_delete_order(self):
        order_id = fake.uuid4()
        response = delete_order(self.client, order_id, self.host, self.headers)
        self.assertIsInstance(response, dict)

    def test_find_all_order(self):
        response = find_all_order(self.client, self.host, self.headers)
        self.assertIsInstance(response, list)

    if __name__ == '__main__':
        unittest.main()
