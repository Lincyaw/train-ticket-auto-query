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
        basic_auth_dto = DtoLoginUser(username='admin',
                                      password='222222', verificationCode="123")
        token = users_login(self.client, basic_auth_dto, headers, BASE_URL)
        self.headers = {'Authorization': f'Bearer {token}'}

    def tearDown(self):
        self.client.close()

    def test_welcome(self):
        response = welcome(self.client, self.host)
        self.assertIsInstance(response, str)

    def test_get_all_contacts(self):
        response = get_all_contacts(self.client, self.host, self.headers)
        self.assertIsInstance(response, dict)

    def test_create_new_contacts(self):
        contacts = Contacts(id=str(fake.uuid4()),
                            accountId=str(fake.uuid4()),
                            name=str(fake.name()),
                            documentType=int(fake.random_int(min=0, max=9)),
                            documentNumber=str(fake.bothify(text='??-########')),
                            phoneNumber="15811803568")
        response = create_new_contacts(self.client, contacts, self.host, self.headers)
        self.assertIsInstance(response, dict)

    def test_create_new_contacts_admin(self):
        contacts = Contacts(id=str(fake.uuid4()),
                            accountId=str(fake.uuid4()),
                            name=str(fake.name()),
                            documentType=int(fake.random_int(min=0, max=9)),
                            documentNumber=str(fake.bothify(text='??-########')),
                            phoneNumber="+1 15811803568")
        response = create_new_contacts_admin(self.client, contacts, self.host, self.headers)
        self.assertIsInstance(response, dict)

    def test_delete_contacts(self):
        contactsId = "a9e7f430-f204-422f-bd56-c99d8246b139"
        response = delete_contacts(self.client, contactsId, self.host, self.headers)
        self.assertIsInstance(response, dict)

    def test_modify_contacts(self):
        contacts = Contacts(id="d7641d2d-15de-48b1-8a89-f5b168e8feb7",
                            accountId=str(fake.uuid4()),
                            name="Changed Name",
                            documentType=int(fake.random_int(min=0, max=9)),
                            documentNumber=str(fake.bothify(text='??-########')),
                            phoneNumber="+1 15811803568")
        response = modify_contacts(self.client, contacts, self.host, self.headers)
        self.assertIsInstance(response, dict)

    def test_find_contacts_by_account_id(self):
        accountId = "914e7699-f77e-40de-85f5-6ac46c3162c8"
        response = find_contacts_by_account_id(self.client, accountId, self.host, self.headers)
        self.assertIsInstance(response, dict)

    def test_get_contacts_by_contacts_id(self):
        id = "9f806e73-95a8-4948-8180-370c7f8c596e"
        response = get_contacts_by_contacts_id(self.client, id, self.host, self.headers)
        self.assertIsInstance(response, dict)

    def test_end_to_end(self):
        # Test welcome
        welcome_response = welcome(self.client, self.host)
        self.assertIsInstance(welcome_response, str)

        # Create a new contact
        contacts = Contacts(id=str(fake.uuid4()),
                            accountId=str(fake.uuid4()),
                            name=str(fake.name()),
                            documentType=int(fake.random_int(min=0, max=9)),
                            documentNumber=str(fake.bothify(text='??-########')),
                            phoneNumber="15811803568")
        create_response = create_new_contacts(self.client, contacts, self.host, self.headers)
        self.assertIsInstance(create_response, dict)

        # Get all contacts
        get_all_response = get_all_contacts(self.client, self.host, self.headers)
        self.assertIsInstance(get_all_response, dict)

        # Modify the contact
        contacts.name = "Modified Name"
        modify_response = modify_contacts(self.client, contacts, self.host, self.headers)
        self.assertIsInstance(modify_response, dict)

        # Find contacts by account ID
        account_id = contacts.accountId
        find_by_account_response = find_contacts_by_account_id(self.client, account_id, self.host, self.headers)
        self.assertIsInstance(find_by_account_response, dict)

        # Get contacts by contacts ID
        contacts_id = contacts.id
        get_by_contacts_id_response = get_contacts_by_contacts_id(self.client, contacts_id, self.host, self.headers)
        self.assertIsInstance(get_by_contacts_id_response, dict)

        # Delete the contact
        delete_response = delete_contacts(self.client, contacts_id, self.host, self.headers)
        self.assertIsInstance(delete_response, dict)


if __name__ == '__main__':
    unittest.main()