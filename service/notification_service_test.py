import unittest
from service.notification_service import *
from service.auth_service import DtoLoginUser, users_login
from service.test_utils import BASE_URL, headers
from faker import Faker

fake = Faker()


class TestNotificationService(unittest.TestCase):
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

    # def test_test_send(self):
    #     response = test_send(self.client, self.host)
    #     self.assertIsInstance(response, bool)

    # def test_test_send_mail(self):
    #     response = test_send_mail(self.client, self.host)
    #     self.assertIsInstance(response, bool)

    def test_preserve_success(self):
        info = NotifyInfo(
            id=str(fake.uuid4()),
            sendStatus=bool(1),
            email="yimouwu@link.cuhk.edu.cn",
            orderNumber=str(fake.uuid4()),
            username="kevin",
            startPlace="Shenzhen",
            endPlace="The Chinese University of Hong Kong, SZ",
            startTime="2024-06-05 06:26:00",
            date=str("June 5"),
            seatClass=str("111"),
            seatNumber="777",
            price=str("100")
        )
        response = preserve_success(self.client, info, self.host, self.headers)
        self.assertIsInstance(response, bool)

    def test_order_create_success(self):
        info = NotifyInfo(
            id=str(fake.uuid4()),
            sendStatus=bool(1),
            email="yimouwu@link.cuhk.edu.cn",
            orderNumber=str(fake.uuid4()),
            username="kevin",
            startPlace="Shenzhen",
            endPlace="The Chinese University of Hong Kong, SZ",
            startTime="2024-06-05 06:26:00",
            date=str("June 5"),
            seatClass=str("111"),
            seatNumber="777",
            price=str("100")
        )
        response = order_create_success(self.client, info, self.host, self.headers)
        self.assertIsInstance(response, bool)

    def test_order_changed_success(self):
        info = NotifyInfo(
            id=str(fake.uuid4()),
            sendStatus=bool(1),
            email="yimouwu@link.cuhk.edu.cn",
            orderNumber=str(fake.uuid4()),
            username="kevin",
            startPlace="Shenzhen",
            endPlace="The Chinese University of Hong Kong, SZ",
            startTime="2024-06-05 06:26:00",
            date=str("June 5"),
            seatClass=str("111"),
            seatNumber="777",
            price=str("100")
        )
        response = order_changed_success(self.client, info, self.host, self.headers)
        self.assertIsInstance(response, bool)

    def test_order_cancel_success(self):
        info = NotifyInfo(
            id=str(fake.uuid4()),
            sendStatus=bool(1),
            email="yimouwu@link.cuhk.edu.cn",
            orderNumber=str(fake.uuid4()),
            username="kevin",
            startPlace="Shenzhen",
            endPlace="The Chinese University of Hong Kong, SZ",
            startTime="2024-06-05 06:26:00",
            date=str("June 5"),
            seatClass=str("111"),
            seatNumber="777",
            price=str("100")
        )
        response = order_cancel_success(self.client, info, self.host, self.headers)
        self.assertIsInstance(response, bool)

    def test_end_to_end(self):
        # Test preserveSuccess
        preserve_info = NotifyInfo(
            id=str(fake.uuid4()),
            sendStatus=bool(1),
            email="yimouwu@link.cuhk.edu.cn",
            orderNumber=str(fake.uuid4()),
            username="kevin",
            startPlace="Shenzhen",
            endPlace="The Chinese University of Hong Kong, SZ",
            startTime="2024-06-05 06:26:00",
            date=str("June 5"),
            seatClass=str("111"),
            seatNumber="777",
            price=str("100")
        )
        preserve_response = preserve_success(self.client, preserve_info, self.host, self.headers)
        self.assertIsInstance(preserve_response, bool)

        # Test orderCreateSuccess
        create_info = NotifyInfo(
            id=str(fake.uuid4()),
            sendStatus=bool(1),
            email="yimouwu@link.cuhk.edu.cn",
            orderNumber=str(fake.uuid4()),
            username="kevin",
            startPlace="Shenzhen",
            endPlace="The Chinese University of Hong Kong, SZ",
            startTime="2024-06-05 06:26:00",
            date=str("June 5"),
            seatClass=str("111"),
            seatNumber="777",
            price=str("100")
        )
        create_response = order_create_success(self.client, create_info, self.host, self.headers)
        self.assertIsInstance(create_response, bool)

        # Test orderChangedSuccess
        changed_info = NotifyInfo(
            id=str(fake.uuid4()),
            sendStatus=bool(1),
            email="yimouwu@link.cuhk.edu.cn",
            orderNumber=str(fake.uuid4()),
            username="kevin",
            startPlace="Shenzhen",
            endPlace="The Chinese University of Hong Kong, SZ",
            startTime="2024-06-05 06:26:00",
            date=str("June 5"),
            seatClass=str("111"),
            seatNumber="777",
            price=str("100")
        )
        changed_response = order_changed_success(self.client, changed_info, self.host, self.headers)
        self.assertIsInstance(changed_response, bool)

        # Test orderCancelSuccess
        cancel_info = NotifyInfo(
            id=str(fake.uuid4()),
            sendStatus=bool(1),
            email="yimouwu@link.cuhk.edu.cn",
            orderNumber=str(fake.uuid4()),
            username="kevin",
            startPlace="Shenzhen",
            endPlace="The Chinese University of Hong Kong, SZ",
            startTime="2024-06-05 06:26:00",
            date=str("June 5"),
            seatClass=str("111"),
            seatNumber="777",
            price=str("100")
        )
        cancel_response = order_cancel_success(self.client, cancel_info, self.host, self.headers)
        self.assertIsInstance(cancel_response, bool)


if __name__ == '__main__':
    unittest.main()
