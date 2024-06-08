import unittest
from service.train_service import *
from service.auth_service import DtoLoginUser, users_login
from service.test_utils import BASE_URL, headers
from faker import Faker

fake = Faker()


class TestTrainService(unittest.TestCase):
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
        response = home(self.client, self.host, self.headers)
        self.assertIsInstance(response, str)

    def test_create(self):
        train_type = TrainType(id=str(fake.uuid4()),
                               name=str(fake.name()),
                               economyClass=int(0),
                               confortClass=int(1),
                               averageSpeed=int(283))
        response = create(self.client, train_type, self.host, self.headers)
        self.assertEquals(response['status'], 1)

    def test_retrieve(self):
        train_type_id = str(fake.uuid4())
        response = retrieve(self.client, train_type_id, self.host, self.headers)
        self.assertIsInstance(response, dict)

    def test_retrieve_by_name(self):
        train_type_name = str(fake.name())
        response = retrieve_by_name(self.client, train_type_name, self.host, self.headers)
        self.assertIsInstance(response, dict)

    def test_retrieve_by_names(self):
        train_type_names = [fake.word() for _ in range(3)]
        response = retrieve_by_names(self.client, train_type_names, self.host, self.headers)
        self.assertIsInstance(response, dict)

    def test_update(self):
        train_type = TrainType(id="3c31a36c-e7f1-49e1-b1c3-82830f23ec1c",
                               name=str(fake.name()),
                               economyClass=int(0),
                               confortClass=int(1),
                               averageSpeed=int(283))
        response = update(self.client, train_type, self.host, self.headers)
        self.assertEquals(response['status'], 1)

    def test_delete(self):
        train_type_id = "c3f6abd3-933c-473a-94d4-46b4c033136e"
        response = delete(self.client, train_type_id, self.host, self.headers)
        self.assertEquals(response['status'], 1)
        # self.assertEquals(response, dict)

    def test_query(self):
        response = query(self.client, self.host, self.headers)
        print(response)
        self.assertIsInstance(response, dict)

    def test_end_to_end(self):
        # Step 1: Create a train type
        created_train_type = TrainType(id="6870f450-ea2f-4fab-b082-71bd59e1850d",
                               name=str(fake.name()),
                               economyClass=int(0),
                               confortClass=int(1),
                               averageSpeed=int(283))
        created_response = create(self.client, created_train_type, self.host, self.headers)
        self.assertEqual(created_response['status'], 1)
        # created_train_type.id = created_response['data']['id']  # Update the ID of the created train type

        # Step 2: Retrieve the created train type
        retrieved_train_type = retrieve(self.client, "f49f94c4-cc68-4e39-8246-0dd3aced5a6b", self.host, self.headers)
        self.assertEqual(retrieved_train_type['status'], 1)
        # self.assertEqual(retrieved_train_type['data']['id'], created_train_type.id)

        # Step 3: Update the train type
        updated_train_type = TrainType(id="6870f450-ea2f-4fab-b082-71bd59e1850d",
                               name=str(fake.name()),
                               economyClass=int(0),
                               confortClass=int(1),
                               averageSpeed=int(295))
        updated_response = update(self.client, updated_train_type, self.host, self.headers)
        # self.assertEqual(updated_response['status'], 1)

        # Step 4: Retrieve the updated train type by name
        retrieved_by_name = retrieve_by_name(self.client, "Michelle Park", self.host, self.headers)
        self.assertEqual(retrieved_by_name['status'], 1)
        # self.assertEqual(retrieved_by_name['data']['name'], updated_train_type.name)

        # Step 5: Retrieve train types by names
        train_type_names = [str(fake.word()) for _ in range(3)]
        retrieved_by_names = retrieve_by_names(self.client, train_type_names, self.host, self.headers)
        self.assertIsInstance(retrieved_by_names, dict)

        # Step 6: Query all train types
        queried_train_types = query(self.client, self.host, self.headers)
        self.assertEqual(queried_train_types['status'], 1)

        # Step 7: Delete the train type
        deleted_response = delete(self.client, str(fake.uuid4()), self.host, self.headers)
        self.assertIsInstance(deleted_response, dict)


if __name__ == '__main__':
    unittest.main()
