import unittest
from service.consign_service import *
from service.auth_service import DtoLoginUser, users_login
from service.test_utils import BASE_URL, headers
from faker import Faker
from datetime import datetime

fake = Faker()


class TestConsignService(unittest.TestCase):
    def setUp(self):
        self.client = requests.Session()
        self.host = BASE_URL
        basic_auth_dto = DtoLoginUser(username='fdse_microservice',
                                      password='111111', verificationCode="123")
        token = users_login(self.client, basic_auth_dto, headers, BASE_URL)
        self.headers = {'Authorization': f'Bearer {token}'}

    def tearDown(self):
        self.client.close()

    def test_welcome(self):
        response = welcome(self.client, self.host, self.headers)
        self.assertIsInstance(response, str)

    def test_insert_consign(self):
        consign = Consign(accountId=fake.uuid4(),
                          handleDate=datetime.now(),
                          targetDate=datetime.now(),
                          from_=fake.city(),
                          to=fake.city(),
                          consignee=fake.name(),
                          phone=fake.phone_number(),
                          weight=fake.pyfloat(positive=True),
                          id=fake.uuid4(),
                          orderId=fake.uuid4(),
                          consignee_idcard=fake.uuid4(),
                          price=fake.pyfloat(positive=True))
        response = insert_consign(self.client, consign, self.host, self.headers)
        self.assertIsInstance(response, dict)

    def test_update_consign(self):
        consign = Consign(accountId=fake.uuid4(),
                          handleDate=datetime.now(),
                          targetDate=datetime.now(),
                          from_=fake.city(),
                          to=fake.city(),
                          consignee=fake.name(),
                          phone=fake.phone_number(),
                          weight=fake.pyfloat(positive=True),
                          id=fake.uuid4(),
                          orderId=fake.uuid4(),
                          consignee_idcard=fake.uuid4(),
                          price=fake.pyfloat(positive=True))
        response = update_consign(self.client, consign, self.host, self.headers)
        self.assertIsInstance(response, dict)

    def test_find_by_account_id(self):
        account_id = fake.uuid4()
        response = find_by_account_id(self.client, account_id, self.host, self.headers)
        self.assertIsInstance(response, dict)

    def test_find_by_order_id(self):
        order_id = fake.uuid4()
        response = find_by_order_id(self.client, order_id, self.host, self.headers)
        self.assertIsInstance(response, dict)

    def test_find_by_consignee(self):
        consignee = fake.name()
        response = find_by_consignee(self.client, consignee, self.host, self.headers)
        self.assertIsInstance(response, dict)


if __name__ == '__main__':
    unittest.main()
