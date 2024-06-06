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
        consign = Consign(id=fake.uuid4(),
                          orderId=fake.uuid4(),
                          accountId=fake.uuid4(),
                          handleDate="2024-06-03 09:00:00",
                          targetDate="2024-06-03 10:00:00",
                          # from: str
                          from_location="shanghai",
                          to="suzhou",
                          consignee="kevin",
                          phone="15811803568",
                          weight="140.00",
                          isWithin=True)
        response = insert_consign(self.client, consign, self.host, self.headers)
        self.assertIsInstance(response, dict)

    def test_update_consign(self):
        consign = Consign(id=fake.uuid4(),
                          orderId=fake.uuid4(),
                          accountId=fake.uuid4(),
                          handleDate="2024-06-03 09:00:00",
                          targetDate="2024-06-03 10:00:00",
                          # from: str
                          from_location="shanghai",
                          to="suzhou",
                          consignee="kevin",
                          phone="15811803568",
                          weight="140.00",
                          isWithin=True)
        response = update_consign(self.client, consign, self.host, self.headers)
        self.assertIsInstance(response, dict)

    def test_find_by_account_id(self):
        id = "59668612-f6be-487b-a133-36ebd6864dd8" #这个是之前在数据库consign_price_service中生成的
        response = find_by_account_id(self.client, id, self.host, self.headers)
        self.assertIsInstance(response, dict)

    def test_find_by_order_id(self):
        id = str(fake.uuid4())
        response = find_by_order_id(self.client, id, self.host, self.headers)
        self.assertIsInstance(response, dict)

    def test_find_by_consignee(self):
        consignee = str(fake.name())
        response = find_by_consignee(self.client, consignee, self.host, self.headers)
        self.assertIsInstance(response, dict)

    def test_end_to_end(self):
        # Test welcome
        welcome_response = welcome(self.client, self.host, self.headers)
        self.assertIsInstance(welcome_response, str)

        # Create a new consign
        consign = Consign(id=fake.uuid4(),
                          orderId=fake.uuid4(),
                          accountId=fake.uuid4(),
                          handleDate="2024-06-03 09:00:00",
                          targetDate="2024-06-03 10:00:00",
                          from_location="shanghai",
                          to="suzhou",
                          consignee="kevin",
                          phone="15811803568",
                          weight="140.00",
                          isWithin=True)
        insert_response = insert_consign(self.client, consign, self.host, self.headers)
        self.assertIsInstance(insert_response, dict)

        # Update the consign
        consign.to = "beijing"
        update_response = update_consign(self.client, consign, self.host, self.headers)
        self.assertIsInstance(update_response, dict)

        # Find consign by account ID
        account_id = consign.accountId
        find_by_account_response = find_by_account_id(self.client, account_id, self.host, self.headers)
        self.assertIsInstance(find_by_account_response, dict)

        # Find consign by order ID
        order_id = consign.orderId
        find_by_order_response = find_by_order_id(self.client, order_id, self.host, self.headers)
        self.assertIsInstance(find_by_order_response, dict)

        # Find consign by consignee
        consignee = consign.consignee
        find_by_consignee_response = find_by_consignee(self.client, consignee, self.host, self.headers)
        self.assertIsInstance(find_by_consignee_response, dict)


if __name__ == '__main__':
    unittest.main()
