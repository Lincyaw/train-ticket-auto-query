import unittest
from service.consign_price_service import *
from service.auth_service import DtoLoginUser, users_login
from service.test_utils import BASE_URL, headers
from faker import Faker

fake = Faker()


class TestConsignPriceService(unittest.TestCase):
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

    def test_get_price_by_weight_and_region(self):
        weight = fake.pyfloat(positive=True)
        is_within_region = fake.pybool()
        response = get_price_by_weight_and_region(self.client, weight, is_within_region, self.host, self.headers)
        self.assertIsInstance(response, dict)

    def test_get_price_info(self):
        response = get_price_info(self.client, self.host, self.headers)
        self.assertIsInstance(response, dict)

    def test_get_price_config(self):
        response = get_price_config(self.client, self.host, self.headers)
        self.assertIsInstance(response, dict)

    def test_modify_price_config(self):
        price_config = ConsignPrice(index=fake.random_int(min=0),
                                    initialWeight=fake.pyfloat(positive=True),
                                    initialPrice=fake.pyfloat(positive=True),
                                    withinPrice=fake.pyfloat(positive=True),
                                    beyondPrice=fake.pyfloat(positive=True))
        response = modify_price_config(self.client, price_config, self.host, self.headers)
        self.assertIsInstance(response, dict)


if __name__ == '__main__':
    unittest.main()