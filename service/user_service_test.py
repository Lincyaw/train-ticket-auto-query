import unittest
from service.user_service import *
from service.auth_service import DtoLoginUser, users_login
from service.test_utils import BASE_URL, headers
from faker import Faker

fake = Faker()


class TestUserService(unittest.TestCase):
    def setUp(self):
        self.client = requests.Session()
        self.host = BASE_URL
        basic_auth_dto = DtoLoginUser(username='fdse_microservice',
                                      password='111111', verificationCode="123")
        token = users_login(self.client, basic_auth_dto, headers, BASE_URL)
        self.headers = {'Authorization': f'Bearer {token}'}

    def tearDown(self):
        self.client.close()

    def test_hello(self):
        response = test_hello(self.client, self.host)
        self.assertEqual(response, "Hello")

    def test_get_all_users(self):
        response = get_all_users(self.client, self.host, self.headers)
        self.assertIsInstance(response, Response)

    def test_get_user_by_username(self):
        username = fake.user_name()
        response = get_user_by_username(self.client, username, self.host, self.headers)
        self.assertIsInstance(response, Response)

    def test_get_user_by_userid(self):
        user_id = fake.uuid4()
        response = get_user_by_userid(self.client, user_id, self.host, self.headers)
        self.assertIsInstance(response, Response)

    def test_register_user(self):
        user = UserDto(userId=fake.uuid4(),
                       userName=fake.user_name(),
                       password=fake.password(),
                       gender=fake.random_int(min=0, max=1),
                       documentType=fake.random_int(min=0, max=1),
                       documentNum=fake.random_str(min=100000, max=999999),
                       email=fake.email())
        response = register_user(self.client, user, self.host, self.headers)
        self.assertIsInstance(response, Response)

    def test_delete_user_by_id(self):
        user_id = fake.uuid4()
        response = delete_user_by_id(self.client, user_id, self.host, self.headers)
        self.assertIsInstance(response, Response)

    def test_update_user(self):
        user = UserDto(userId=fake.uuid4(),
                       userName=fake.user_name(),
                       password=fake.password(),
                       gender=fake.random_int(min=0, max=1),
                       documentType=fake.random_int(min=0, max=1),
                       documentNum=fake.random_str(min=100000, max=999999),
                       email=fake.email())
        response = update_user(self.client, user, self.host, self.headers)
        self.assertIsInstance(response, Response)

    def test_end2end(self):
        # Register a new user
        new_user = UserDto(userId=fake.uuid4(),
                           userName=fake.user_name(),
                           password=fake.password(),
                           gender=fake.random_int(min=0, max=1),
                           documentType=fake.random_int(min=0, max=1),
                           documentNum=fake.random_str(min=100000, max=999999),
                           email=fake.email())
        register_response = register_user(self.client, new_user, self.host, self.headers)
        print("Register user response:", register_response)

        # Get the new user by username
        get_by_username_response = get_user_by_username(self.client, new_user.userName, self.host, self.headers)
        print("Get user by username response:", get_by_username_response)

        # Get the new user by userid
        get_by_userid_response = get_user_by_userid(self.client, new_user.userId, self.host, self.headers)
        print("Get user by userid response:", get_by_userid_response)

        # Update the new user
        new_user.email = fake.email()
        update_response = update_user(self.client, new_user, self.host, self.headers)
        print("Update user response:", update_response)

        # Delete the new user
        delete_response = delete_user_by_id(self.client, new_user.userId, self.host, self.headers)
        print("Delete user response:", delete_response)


if __name__ == '__main__':
    unittest.main()
