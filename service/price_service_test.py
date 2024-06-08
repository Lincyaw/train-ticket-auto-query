import unittest
from service.price_service import *
from service.auth_service import DtoLoginUser, users_login
from service.test_utils import BASE_URL, headers
from faker import Faker

fake = Faker()


class TestPriceService(unittest.TestCase):
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

    def test_find_by_route_id_and_train_type(self):
        route_id = str(fake.uuid4())
        train_type = str(fake.word())
        response = find_by_route_id_and_train_type(self.client, route_id, train_type, self.host, self.headers)
        self.assertIsInstance(response, dict)

    def test_find_by_route_ids_and_train_types(self):
        rids_and_tts = [str(fake.uuid4()), "GaoTieOne"]
        response = find_by_route_ids_and_train_types(self.client, rids_and_tts, self.host, self.headers)
        self.assertIsInstance(response, dict)

    def test_find_all_price_config(self):
        response = find_all_price_config(self.client, self.host, self.headers)
        self.assertEquals(response['status'], 1)

    def test_create_and_delete_price_config(self):
        info = PriceConfig(id=str(fake.uuid4()), routeId=str(fake.uuid4()), trainType=str(fake.word()))
        create_response = create_new_price_config(self.client, info, self.host, self.headers)
        self.assertIsInstance(create_response, dict)

        delete_response = delete_price_config(self.client, str(fake.uuid4()), self.host, self.headers)
        self.assertIsInstance(delete_response, dict)

    def test_update_price_config(self):
        info = PriceConfig(id=str(fake.uuid4()), routeId=str(fake.uuid4()), trainType=str(fake.word()))
        create_response = create_new_price_config(self.client, info, self.host, self.headers)
        self.assertIsInstance(create_response, dict)

        update_info = PriceConfig(id=str(fake.uuid4()), routeId=str(fake.uuid4()), trainType=str(fake.word()))
        update_response = update_price_config(self.client, update_info, self.host, self.headers)
        self.assertIsInstance(update_response, dict)

    def test_end_to_end(self):
        # Step 1: Create a new price config
        create_info = PriceConfig(id=str(fake.uuid4()), routeId=str(fake.uuid4()), trainType=str(fake.word()))
        create_response = create_new_price_config(self.client, create_info, self.host, self.headers)
        self.assertIsInstance(create_response, dict)

        # Step 2: Find the created price config
        find_response = find_by_route_id_and_train_type(self.client, create_info.routeId, create_info.trainType, self.host, self.headers)
        self.assertIsInstance(find_response, dict)

        # Step 3: Update the price config
        update_info = PriceConfig(id=str(fake.uuid4()), routeId=str(fake.uuid4()), trainType=str(fake.word()))
        update_response = update_price_config(self.client, update_info, self.host, self.headers)
        self.assertIsInstance(update_response, dict)

        # Step 4: Find the updated price config
        find_updated_response = find_by_route_id_and_train_type(self.client, update_info.routeId, update_info.trainType, self.host, self.headers)
        self.assertIsInstance(find_updated_response, dict)

        # Step 5: Delete the price config
        delete_response = delete_price_config(self.client, str(fake.uuid4()), self.host, self.headers)
        self.assertIsInstance(delete_response, dict)

        # Step 6: Verify the price config is deleted
        find_deleted_response = find_by_route_id_and_train_type(self.client, update_info.routeId, update_info.trainType,
                                                                self.host, self.headers)
        self.assertEquals(find_deleted_response['status'], 0)

    if __name__ == '__main__':
        unittest.main()