import unittest
from service.admin_user_service import *
from service.auth_service import DtoLoginUser, users_login
from service.test_utils import BASE_URL, headers
from faker import Faker

fake = Faker()


class TestAdminUserService(unittest.TestCase):
    def setUp(self):
        self.client = requests.Session()
        self.host = BASE_URL
        basic_auth_dto = DtoLoginUser(username='admin',
                                      password='222222', verificationCode="123")
        token = users_login(self.client, basic_auth_dto, headers, BASE_URL)
        self.headers = {'Authorization': f'Bearer {token}'}

    def tearDown(self):
        self.client.close()

    def test_admin_user_welcome(self):
        response = admin_user_welcome(self.client, self.host, self.headers)
        self.assertIsInstance(response, str)

    def test_get_all_users(self):
        response = get_all_users(self.client, self.host, self.headers)
        self.assertIsInstance(response, Response)

    def test_update_user(self):
        user = UserDto(userId=fake.uuid4(),
                       userName=fake.user_name(),
                       password=fake.password(),
                       gender=fake.random_int(min=0, max=1),
                       documentType=fake.random_int(min=0, max=1),
                       documentNum=fake.random_int(min=100000, max=999999),
                       email=fake.email())
        response = update_user(self.client, user, self.host, self.headers)
        self.assertIsInstance(response, dict)

    def test_add_user(self):
        user = UserDto(userId=fake.uuid4(),
                       userName=fake.user_name(),
                       password=fake.password(),
                       gender=fake.random_int(min=0, max=1),
                       documentType=fake.random_int(min=0, max=1),
                       documentNum=fake.random_int(min=100000, max=999999),
                       email=fake.email())
        response = add_user(self.client, user, self.host, self.headers)
        self.assertIsInstance(response, dict)

    def test_delete_user(self):
        user_id = fake.uuid4()
        response = delete_user(self.client, user_id, self.host, self.headers)
        self.assertIsInstance(response, dict)

    def test_end2end(self):
        # Get all users
        all_users = get_all_users(self.client, self.host, self.headers)
        print("All users:", all_users)

        # Add a new user
        new_user = UserDto(userId=fake.uuid4(),
                           userName=fake.user_name(),
                           password=fake.password(),
                           gender=fake.random_int(min=0, max=1),
                           documentType=fake.random_int(min=0, max=1),
                           documentNum=fake.random_int(min=100000, max=999999),
                           email=fake.email())
        add_response = add_user(self.client, new_user, self.host, self.headers)
        print("Add user response:", add_response)

        # Update the new user
        new_user.userName = fake.user_name()
        update_response = update_user(self.client, new_user, self.host, self.headers)
        print("Update user response:", update_response)

        # Delete the new user
        delete_response = delete_user(self.client, new_user.userId, self.host, self.headers)
        print("Delete user response:", delete_response)


if __name__ == '__main__':
    unittest.main()