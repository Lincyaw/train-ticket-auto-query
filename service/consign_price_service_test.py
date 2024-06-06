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
        priceConfig = ConsignPrice("59668612-f6be-487b-a133-36ebd6864dd8",
                                   index=7,
                                   initialWeight=11.11,
                                   initialPrice=22.22,
                                   withinPrice=33.33,
                                   beyondPrice=44.44)
        response = modify_price_config(self.client, priceConfig, self.host, self.headers)
        self.assertIsInstance(response, dict)

    def test_consign_price_service_workflow(self):
        # Test welcome
        welcome_response = welcome(self.client, self.host, self.headers)
        self.assertIsInstance(welcome_response, str)

        # Get price config
        price_config_response = get_price_config(self.client, self.host, self.headers)
        self.assertIsInstance(price_config_response, dict)

        # Modify price config
        priceConfig = ConsignPrice("59668612-f6be-487b-a133-36ebd6864dd8",
                                   index=7,
                                   initialWeight=11.11,
                                   initialPrice=22.22,
                                   withinPrice=33.33,
                                   beyondPrice=44.44)
        modify_config_response = modify_price_config(self.client, priceConfig, self.host, self.headers)
        self.assertIsInstance(modify_config_response, dict)

        # Get updated price config
        updated_price_config_response = get_price_config(self.client, self.host, self.headers)
        self.assertIsInstance(updated_price_config_response, dict)

        # Get price info
        price_info_response = get_price_info(self.client, self.host, self.headers)
        self.assertIsInstance(price_info_response, dict)

        # Get price by weight and region
        weight = fake.pyfloat(positive=True)
        is_within_region = fake.pybool()
        price_response = get_price_by_weight_and_region(self.client, weight, is_within_region, self.host, self.headers)
        self.assertIsInstance(price_response, dict)


if __name__ == '__main__':
    unittest.main()
