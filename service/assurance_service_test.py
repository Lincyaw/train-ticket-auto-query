import unittest
from service.assurance_service import *
from service.auth_service import DtoLoginUser, users_login
from service.test_utils import BASE_URL, headers
from faker import Faker

fake = Faker()


class TestAssuranceService(unittest.TestCase):
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

    def test_get_all_assurances(self):
        response = get_all_assurances(self.client, self.host, self.headers)
        self.assertIsInstance(response, Response)

    def test_get_all_assurance_types(self):
        response = get_all_assurance_types(self.client, self.host, self.headers)
        self.assertIsInstance(response, Response)

    def test_delete_assurance_by_id(self):
        assurance_id = fake.uuid4()
        response = delete_assurance_by_id(self.client, assurance_id, self.host, self.headers)
        self.assertIsInstance(response, Response)

    def test_delete_assurance_by_order_id(self):
        order_id = fake.uuid4()
        response = delete_assurance_by_order_id(self.client, order_id, self.host, self.headers)
        self.assertIsInstance(response, Response)

    def test_modify_assurance(self):
        assurance_id = fake.uuid4()
        order_id = fake.uuid4()
        type_index = fake.random_int(min=0, max=10)
        response = modify_assurance(self.client, assurance_id, order_id, type_index, self.host, self.headers)
        self.assertIsInstance(response, Response)

    def test_create_new_assurance(self):
        type_index = fake.random_int(min=0, max=10)
        order_id = fake.uuid4()
        response = create_new_assurance(self.client, type_index, order_id, self.host, self.headers)
        self.assertIsInstance(response, Response)

    def test_get_assurance_by_id(self):
        assurance_id = fake.uuid4()
        response = get_assurance_by_id(self.client, assurance_id, self.host, self.headers)
        self.assertIsInstance(response, Response)

    def test_find_assurance_by_order_id(self):
        order_id = fake.uuid4()
        response = find_assurance_by_order_id(self.client, order_id, self.host, self.headers)
