import unittest
from service.contacts_service import *
from service.auth_service import DtoLoginUser, users_login
from service.test_utils import BASE_URL, headers
from faker import Faker

fake = Faker()


class TestContactsService(unittest.TestCase):
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
        response = welcome(self.client, self.host)
        self.assertIsInstance(response, str)

    def test_get_all_contacts(self):
        response = get_all_contacts(self.client, self.host, self.headers)
        self.assertIsInstance(response, list)

    def test_create_new_contacts(self):
        contacts = Contacts(id=fake.uuid4(),
                            accountId=fake.uuid4(),
                            name=fake.name(),
                            documentType=fake.random_int(min=0, max=9),
                            documentNumber=fake.bothify(text='??-########'),
                            phoneNumber=fake.phone_number())
        response = create_new_contacts(self.client, contacts, self.host, self.headers)
        self.assertIsInstance(response, dict)

    def test_create_new_contacts_admin(self):
        contacts = Contacts(id=fake.uuid4(),
                            accountId=fake.uuid4(),
                            name=fake.name(),
                            documentType=fake.random_int(min=0, max=9),
                            documentNumber=fake.bothify(text='??-########'),
                            phoneNumber=fake.phone_number())
        response = create_new_contacts_admin(self.client, contacts, self.host, self.headers)
        self.assertIsInstance(response, dict)

    def test_delete_contacts(self):
        contacts_id = fake.uuid4()
        response = delete_contacts(self.client, contacts_id, self.host, self.headers)
        self.assertIsInstance(response, dict)

    def test_modify_contacts(self):
        contacts = Contacts(id=fake.uuid4(),
                            accountId=fake.uuid4(),
                            name=fake.name(),
                            documentType=fake.random_int(min=0, max=9),
                            documentNumber=fake.bothify(text='??-########'),
                            phoneNumber=fake.phone_number())
        response = modify_contacts(self.client, contacts, self.host, self.headers)
        self.assertIsInstance(response, dict)

    def test_find_contacts_by_account_id(self):
        account_id = fake.uuid4()
        response = find_contacts_by_account_id(self.client, account_id, self.host, self.headers)
        self.assertIsInstance(response, dict)

    def test_get_contacts_by_contacts_id(self):
        contacts_id = fake.uuid4()
        response = get_contacts_by_contacts_id(self.client, contacts_id, self.host, self.headers)
        self.assertIsInstance(response, dict)


if __name__ == '__main__':
    unittest.main()