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
        basic_auth_dto = DtoLoginUser(username='admin',
                                      password='222222', verificationCode="123")
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
        self.assertIsInstance(response, dict)

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
        qi = OrderInfo(loginId=str(fake.uuid4()),
                       travelDateStart="2024-06-05 19:26:00",
                       travelDateEnd="2024-06-05 19:236:00",
                       boughtDateStart="2024-06-05 19:46:00",
                       boughtDateEnd="2024-06-06 19:26:00",
                       state=1,
                       enableTravelDateQuery=True,
                       enableBoughtDateQuery=True,
                       enableStateQuery=True)
        response = query_orders(self.client, qi, self.host, self.headers)
        self.assertEquals(response['status'], 1)

    def test_query_orders_for_refresh(self):
        qi = OrderInfo(loginId=str(fake.uuid4()),
                       travelDateStart="2024-06-05 19:26:00",
                       travelDateEnd="2024-06-05 19:236:00",
                       boughtDateStart="2024-06-05 19:46:00",
                       boughtDateEnd="2024-06-06 19:26:00",
                       state=1,
                       enableTravelDateQuery=True,
                       enableBoughtDateQuery=True,
                       enableStateQuery=True)
        response = query_orders_for_refresh(self.client, qi, self.host, self.headers)
        self.assertEquals(response['status'], 1)

    def test_calculate_sold_ticket(self):
        travel_date = "2024-06-06 10:48:00"
        train_number = "123456"
        response = calculate_sold_ticket(self.client, travel_date, train_number, self.host, self.headers)
        self.assertIsInstance(response, dict)

    def test_get_order_price(self):
        order_id = str(fake.uuid4())
        response = get_order_price(self.client, order_id, self.host, self.headers)
        self.assertIsInstance(response, dict)

    def test_pay_order(self):
        order_id = str(fake.uuid4())
        response = pay_order(self.client, order_id, self.host, self.headers)
        self.assertIsInstance(response, dict)

    def test_get_order_by_id(self):
        order_id = str(fake.uuid4())
        response = get_order_by_id(self.client, order_id, self.host, self.headers)
        self.assertIsInstance(response, dict)

    def test_modify_order(self):
        order_id = str(fake.uuid4())
        status = int(fake.random_int(min=0, max=2))
        response = modify_order(self.client, order_id, status, self.host, self.headers)
        self.assertIsInstance(response, dict)

    def test_security_info_check(self):
        check_date = fake.date()
        account_id = fake.uuid4()
        response = security_info_check(self.client, check_date, account_id, self.host, self.headers)
        self.assertIsInstance(response, dict)

    def test_save_order_info(self):
        order_info = Order(
            id=str(fake.uuid4()),
            from_="shanghai",
            to="suzhou",
            travelDate="2024-06-06 11:32:00"
        )
        response = save_order_info(self.client, order_info, self.host, self.headers)
        self.assertIsInstance(response, dict)

    def test_update_order(self):
        order = Order(
            id=str(fake.uuid4()),
            from_="shanghai",
            to="suzhou",
            travelDate="2024-06-06 11:33:00"
        )
        response = update_order(self.client, order, self.host, self.headers)
        self.assertIsInstance(response, dict)

    def test_delete_order(self):
        order_id = str(fake.uuid4())
        response = delete_order(self.client, order_id, self.host, self.headers)
        self.assertIsInstance(response, dict)

    def test_find_all_order(self):
        response = find_all_order(self.client, self.host, self.headers)
        self.assertIsInstance(response, dict)

    def test_end_to_end(self):
        # Create a new order
        order = Order(
            id=str(fake.uuid4()),
            from_="shanghai",
            to="suzhou",
            travelDate="2024-06-06 11:33:00"
        )
        create_response = create_new_order(self.client, order, self.host, self.headers)
        self.assertIsInstance(create_response, dict)

        # Get the order by ID
        order_id = "2b21d5cc-329b-4e01-8f78-e44bf21e9388"
        get_response = get_order_by_id(self.client, order_id, self.host, self.headers)
        self.assertIsInstance(get_response, dict)

        # Update the order
        updated_order = Order(
            id=str(fake.uuid4()),
            from_="shanghai",
            to="suzhou",
            travelDate="2024-06-06 11:33:00"
        )
        update_response = update_order(self.client, updated_order, self.host, self.headers)
        self.assertIsInstance(update_response, dict)

        # Query the updated order
        qi = OrderInfo(loginId=str(fake.uuid4()),
                       travelDateStart="2024-06-05 19:26:00",
                       travelDateEnd="2024-06-05 19:236:00",
                       boughtDateStart="2024-06-05 19:46:00",
                       boughtDateEnd="2024-06-06 19:26:00",
                       state=1,
                       enableTravelDateQuery=True,
                       enableBoughtDateQuery=True,
                       enableStateQuery=True)
        query_response = query_orders(self.client, qi, self.host, self.headers)
        self.assertEquals(query_response['status'], 1)

        # Delete the order
        delete_response = delete_order(self.client, order_id, self.host, self.headers)
        self.assertIsInstance(delete_response, dict)

    if __name__ == '__main__':
        unittest.main()
