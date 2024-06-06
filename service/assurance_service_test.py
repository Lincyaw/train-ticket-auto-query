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
        self.assertIsInstance(response, dict)

    def test_delete_assurance_by_order_id(self):
        order_id = fake.uuid4()
        response = delete_assurance_by_order_id(self.client, order_id, self.host, self.headers)
        self.assertIsInstance(response, dict)

    def test_modify_assurance(self):
        assuranceId = str(fake.uuid4())
        orderId = str(fake.uuid4())
        typeIndex = int(fake.random_int(min=0, max=10))
        response = modify_assurance(self.client, assuranceId, orderId, typeIndex, self.host, self.headers)
        # self.assertIsInstance(response, Response)

    def test_create_new_assurance(self):
        typeIndex = int(fake.random_int(min=0, max=10))
        orderId = str(fake.uuid4())
        response = create_new_assurance(self.client, typeIndex, orderId, self.host, self.headers)
        self.assertIsInstance(response, Response)

    def test_get_assurance_by_id(self):
        assurance_id = fake.uuid4()
        response = get_assurance_by_id(self.client, assurance_id, self.host, self.headers)
        self.assertIsInstance(response, Response)

    def test_find_assurance_by_order_id(self):
        order_id = fake.uuid4()
        response = find_assurance_by_order_id(self.client, order_id, self.host, self.headers)
        self.assertIsInstance(response, Response)

    def test_end2end(self):
        # Test welcome
        response = welcome(self.client, self.host, self.headers)
        self.assertIsInstance(response, str)

        # Test get all assurances
        all_assurances = get_all_assurances(self.client, self.host, self.headers)
        self.assertIsInstance(all_assurances, Response)

        # Test get all assurance types
        all_assurance_types = get_all_assurance_types(self.client, self.host, self.headers)
        self.assertIsInstance(all_assurance_types, Response)

        # Test create new assurance
        typeIndex = int(fake.random_int(min=0, max=10))
        orderId = str(fake.uuid4())
        new_assurance = create_new_assurance(self.client, typeIndex, orderId, self.host, self.headers)
        self.assertIsInstance(new_assurance, Response)

        # Test get assurance by id
        assurance_id = fake.uuid4()
        response = get_assurance_by_id(self.client, assurance_id, self.host, self.headers)
        self.assertIsInstance(response, Response)

        # Test find assurance by order id
        found_assurance = find_assurance_by_order_id(self.client, orderId, self.host, self.headers)
        self.assertIsInstance(found_assurance, Response)

        # Test modify assurance
        modified_assurance = modify_assurance(self.client, assurance_id, orderId, typeIndex, self.host, self.headers)
        # self.assertIsInstance(modified_assurance, Response) //error

        # Test delete assurance by id
        delete_response = delete_assurance_by_id(self.client, assurance_id, self.host, self.headers)
        self.assertIsInstance(delete_response, dict)

        # Test delete assurance by order id
        delete_order_response = delete_assurance_by_order_id(self.client, orderId, self.host, self.headers)
        self.assertIsInstance(delete_order_response, dict)
