import unittest
from service.security_service import *
from service.auth_service import DtoLoginUser, users_login
from service.test_utils import BASE_URL, headers
from faker import Faker

fake = Faker()


class TestSecurityService(unittest.TestCase):
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

    def test_find_all_security_config(self):
        response = find_all_security_config(self.client, self.host, self.headers)
        self.assertIsInstance(response, Return)

    def test_add_new_security_config(self):
        info = SecurityConfig(name=str(fake.name()),
                              id=str(fake.uuid4()),
                              value="777",
                              description="Have a good day!")
        response = add_new_security_config(self.client, info, self.host, self.headers)
        self.assertIsInstance(response, dict)

    def test_modify_security_config(self):
        info = SecurityConfig(name="yimou :D",
                              id=str(fake.uuid4()),
                              value="777",
                              description="Have a good day!")
        response = modify_security_config(self.client, info, self.host, self.headers)
        self.assertIsInstance(response, dict)

    def test_delete_security_config(self):
        config_id = str(fake.uuid4())
        response = delete_security_config(self.client, config_id, self.host, self.headers)
        self.assertIsInstance(response, dict)

    def test_check_security(self):
        account_id = str(fake.uuid4())
        response = check_security(self.client, account_id, self.host, self.headers)
        self.assertIsInstance(response, dict)

    def test_end_to_end(self):
        # Step 1: Add new security config
        add_info = SecurityConfig(name=str(fake.uuid4()),
                              id=str(fake.uuid4()),
                              value="777",
                              description="Have a good day!")
        add_response = add_new_security_config(self.client, add_info, self.host, self.headers)
        self.assertIsInstance(add_response, dict)

        # Step 2: Find all security configs
        find_all_response = find_all_security_config(self.client, self.host, self.headers)
        self.assertIsInstance(find_all_response, Return)

        # Step 3: Modify security config
        modify_info = SecurityConfig(name="yimou :D",
                              id=str(fake.uuid4()),
                              value="777",
                              description="Have a good day!")
        modify_response = modify_security_config(self.client, modify_info, self.host, self.headers)
        self.assertIsInstance(modify_response, dict)

        # Step 4: Check security
        check_response = check_security(self.client, str(fake.uuid4()), self.host, self.headers)
        self.assertIsInstance(check_response, dict)

        # Step 5: Delete security config
        delete_response = delete_security_config(self.client, str(fake.uuid4()), self.host, self.headers)
        self.assertIsInstance(delete_response, dict)


if __name__ == '__main__':
    unittest.main()
