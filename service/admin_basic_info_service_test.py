import unittest
import requests
from service.admin_basic_info_service import *
from service.auth_service import DtoLoginUser, users_login
from service.test_utils import BASE_URL, headers
from faker import Faker
fake = Faker()


class TestAdminBasicInfoService(unittest.TestCase):
    def setUp(self):
        self.client = requests.Session()
        self.host = BASE_URL
        basic_auth_dto = DtoLoginUser(username='admin',
                                  password='222222', verificationCode="123")
        token = users_login(self.client, basic_auth_dto, headers, BASE_URL)
        self.client.headers.update({'Authorization': f'Bearer {token}'})

    def tearDown(self):
        self.client.close()

    def test_adminbasic_welcome(self):
        response = adminbasic_welcome(self.client, self.host)
        self.assertIsInstance(response, str)

    def test_get_all_contacts(self):
        # auth_dto = DtoCreateUser(userId='111111', userName='default3333',
        #                      password='12345226')
        # client = requests.Session()
        # result = create_default_user(client, auth_dto, BASE_URL)
        contacts = get_all_contacts(self.client, self.host)
        assert isinstance(contacts.data, list), "Expected contacts to be a list"
        for contact in contacts.data:
            assert isinstance(contact, dict), "Expected each contact to be a dictionary"
            assert "id" in contact, "Expected 'id' key in contact dictionary"
            assert isinstance(contact["id"], str), "Expected 'id' to be a string"
            assert "name" in contact, "Expected 'name' key in contact dictionary"
            assert isinstance(contact["name"], str), "Expected 'name' to be a string"

    def test_delete_contact(self):
        contact_id = "1"
        response = delete_contact(self.client, contact_id, self.host)
        self.assertIsInstance(response, dict)

    def test_modify_contact(self):
        contact = ContactBody (id=fake.uuid4(), 
                              accountId = fake.uuid4(),
                              name="Modified Contact",
                              documentType = 2,
                              documentNumber = "2",
                              phoneNumber = "123456"
                            )
        response = modify_contact(self.client, contact, self.host)
        self.assertIsInstance(response, dict)

    def test_add_contact(self):
        contact = ContactBody (id=fake.uuid4(), 
                              accountId = fake.uuid4(),
                              name=fake.user_name(),
                              documentType = 3,
                              documentNumber = "4",
                              phoneNumber = "4567891011"
                            )
        # orginal_length = len(contacts_after_add.data)
        response = add_contact(self.client, contact, self.host)
        # assert len(contacts_after_add.data) == len(contacts_before.data) + 1

    def test_get_all_stations(self):
        stations = get_all_stations(self.client, self.host)
        assert isinstance(stations.data, list), "Expected contacts to be a list"
        for station in stations.data:
            assert isinstance(station, dict), "Expected each contact to be a dictionary"
            assert "id" in station, "Expected 'id' key in contact dictionary"
            assert isinstance(station["id"], str), "Expected 'id' to be a string"
            assert "name" in station, "Expected 'name' key in contact dictionary"
            assert isinstance(station["name"], str), "Expected 'name' to be a string"
            assert "stayTime" in station, "Expected 'name' key in contact dictionary"
            assert isinstance(station["stayTime"], int), "Expected 'name' to be a string"

    def test_delete_station(self):
        station_id = "2be2c685-70a1-4989-80af-c80281f060e8"
        response = delete_station(self.client, station_id, self.host)
        self.assertIsInstance(response, dict)

    def test_modify_station(self):
        station = StationBody(id="5984585e-708e-4962-b4b6-f6e8d93e52bb", name="nanjing", stayTime=10)
        response = modify_station(self.client, station, self.host)
        self.assertIsInstance(response, dict)

    def test_add_station(self):
        station = StationBody(id="2", name="222 Modified Station", stayTime=222)
        response = add_station(self.client, station, self.host)
        self.assertIsInstance(response, dict)

    def test_get_all_trains(self):
        trains = get_all_trains(self.client, self.host)
        self.assertIsInstance(trains.data, list)
        for train in trains.data:
            assert isinstance(train, dict), "Expected each contact to be a dictionary"
            assert "id" in train, "Expected 'id' key in contact dictionary"
            assert isinstance(train["id"], str), "Expected 'id' to be a string"
            assert "name" in train, "Expected 'name' key in contact dictionary"
            assert isinstance(train["name"], str), "Expected 'name' to be a string"
            assert "economyClass" in train, "Expected 'name' key in contact dictionary"
            assert isinstance(train["economyClass"], int), "Expected 'name' to be a string"
            assert "confortClass" in train, "Expected 'name' key in contact dictionary"
            assert isinstance(train["confortClass"], int), "Expected 'name' to be a string"
            assert "averageSpeed" in train, "Expected 'name' key in contact dictionary"
            assert isinstance(train["averageSpeed"], int), "Expected 'name' to be a string"

    def test_delete_train(self):
        train_id = "1"
        response = delete_train(self.client, train_id, self.host)
        self.assertIsInstance(response, dict)

    def test_modify_train(self):
        train_type = TrainTypeBody(id="1", name="Modified Train", economyClass= 111, confortClass=111, averageSpeed=1111)
        response = modify_train(self.client, train_type, self.host)
        self.assertIsInstance(response, dict)

    def test_add_train(self):
        train_type = TrainTypeBody(id="2", name="222 Modified Train", economyClass= 222, confortClass=222, averageSpeed=2222)
        response = add_train(self.client, train_type, self.host)
        self.assertIsInstance(response, dict)

    def test_get_all_configs(self):
        configs = get_all_configs(self.client, self.host)
        self.assertIsInstance(configs.data, list)
        for config in configs.data:
            assert isinstance(config, dict), "Expected each contact to be a dictionary"
            assert "value" in config, "Expected 'id' key in contact dictionary"
            assert isinstance(config["value"], str), "Expected 'id' to be a string"
            assert "name" in config, "Expected 'name' key in contact dictionary"
            assert isinstance(config["name"], str), "Expected 'name' to be a string"
            assert "description" in config, "Expected 'name' key in contact dictionary"
            assert isinstance(config["description"], str), "Expected 'name' to be a string"


    def test_delete_config(self):
        config_name = "config1"
        response = delete_config(self.client, config_name, self.host)
        self.assertIsInstance(response, dict)

    def test_modify_config(self):
        config = ConfigBody(name="config1", value="Modified Value", description="Modified Config")
        response = modify_config(self.client, config, self.host)
        self.assertIsInstance(response, dict)

    def test_add_config(self):
        config = ConfigBody(name="config2", value="New Value", description="New Config")
        response = add_config(self.client, config, self.host)
        self.assertIsInstance(response, dict)

    def test_get_all_prices(self):
        prices = get_all_prices(self.client, self.host)
        self.assertIsInstance(prices.data, list)
        for price in prices.data:
            assert isinstance(price, dict), "Expected each contact to be a dictionary"
            assert "id" in price, "Expected 'id' key in contact dictionary"
            assert isinstance(price["id"], str), "Expected 'id' to be a string"
            assert "trainType" in price, "Expected 'trainType' key in contact dictionary"
            assert isinstance(price["trainType"], str), "Expected 'trainType' to be a string"
            assert "routeId" in price, "Expected 'routeId' key in contact dictionary"
            assert isinstance(price["routeId"], str), "Expected 'routeId' to be a string"
            assert "basicPriceRate" in price, "Expected 'basicPriceRate' key in contact dictionary"
            assert isinstance(price["basicPriceRate"], float), "Expected 'basicPriceRate' to be a string"
            assert "firstClassPriceRate" in price, "Expected 'firstClassPriceRate' key in contact dictionary"
            assert isinstance(price["firstClassPriceRate"], float), "Expected 'firstClassPriceRate' to be a string"

    def test_delete_price(self):
        price_id = "1"
        response = delete_price(self.client, price_id, self.host)
        self.assertIsInstance(response, dict)

    def test_modify_price(self):
        price_info = PriceInfoBody(id="1", trainType="G", routeId="1", basicPriceRate=0.5, firstClassPriceRate=1.0)
        response = modify_price(self.client, price_info, self.host)
        self.assertIsInstance(response, dict)

    def test_add_price(self):
        price_info = PriceInfoBody(id="2", trainType="D", routeId="2", basicPriceRate=0.6, firstClassPriceRate=1.2)
        response = add_price(self.client, price_info, self.host)
        self.assertIsInstance(response, dict)


    def test_end2end(self):
        """
        End-to-end test: query, add, update, delete
        """
        # 1. Query contacts
        contacts_before =get_all_contacts(self.client, self.host)
        print("Contacts before:", contacts_before)
        
        # 2. Add a new contact
        new_contact = ContactBody(id=fake.uuid4(), 
                                  accountId=fake.uuid4(),
                                  name=fake.user_name(),
                                  documentType=22,
                                  documentNumber="0000",
                                  phoneNumber=fake.basic_phone_number())
        add_response = add_contact(self.client, new_contact, self.host)
        print("New contact added:", add_response)

        # 3. Query contacts and verify addition
        contacts_after_add = get_all_contacts(self.client, self.host)
        print("Contacts after addition:", contacts_after_add)
        # assert len(contacts_after_add.data) == len(contacts_before.data) + 1
        # assert any(contact["id"] == new_contact.id for contact in contacts_after_add.data)

        # 4. Update the new contact
        updated_contact = ContactBody(id="4d94638a-0094-41b5-be76-4485d10cd047", 
                                      accountId="538fa219-acf2-4bc2-8ba8-8be24a0e608b",
                                      name="Updated Contact",
                                      documentType=7,
                                      documentNumber="000",
                                      phoneNumber="000000")
        update_response = modify_contact(self.client, updated_contact, self.host)
        print("Contact updated:", update_response)

        # 5. Query contacts and verify update
        contacts_after_update = get_all_contacts(self.client, self.host)
        print("Contacts after update:", contacts_after_update)
        assert any(contact["name"] == updated_contact.name for contact in contacts_after_update.data)

        # 6. Delete the new contact
        delete_response = delete_contact(self.client, new_contact.id, self.host)
        print("Contact deleted:", delete_response)

        # 7. Query contacts and verify deletion
        contacts_after_delete = get_all_contacts(self.client, self.host)
        print("Contacts after deletion:", contacts_after_delete)
        assert len(contacts_after_delete.data) == len(contacts_before.data) + 1
        assert not any(contact["id"] == new_contact.id for contact in contacts_after_delete.data)

if __name__ == '__main__':
    unittest.main()