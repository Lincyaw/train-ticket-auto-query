import pytest
from common import HttpClient
from admin_basic_info import *
from auth import *

client = HttpClient()

# TODO
def test_get_welcome():
    response = get_welcome(client, None)
    print(response)


def test_get_contacts():
    headers = {}
    response = get_contacts(client, headers)
    print(response['data'])

    contact = {'id': 'New Contact'}
    response = create_contact(client, contact, headers)



def test_delete_contact():
    headers = {}
    contact_id = 1
    response = delete_contact(client, contact_id, headers)


def test_update_contact():
    headers = {}
    contact = {'id': 1, 'name': 'John Updated'}
    response = update_contact(client, contact, headers)


def test_create_contact():
    headers = {}
    contact = {'name': 'New Contact'}
    response = create_contact(client, contact, headers)


def test_get_stations():
    basic_auth_dto = {'username': 'fdse_microservice', 'password': '111111',
                      "verificationCode": "1234"}
    headers = {'Content-Type': 'application/json'}
    users_login(client, basic_auth_dto, headers)
    headers = {}
    response = get_stations(client, headers)
    print(response)


def test_delete_station():
    headers = {}
    station_id = 1
    response = delete_station(client, station_id, headers)


def test_update_station():
    headers = {}
    station = {'id': 1, 'name': 'Station Updated'}
    response = update_station(client, station, headers)


def test_create_station():
    headers = {}
    station = {'name': 'New Station'}
    response = create_station(client, station, headers)


def test_get_trains():
    headers = {}
    response = get_trains(client, headers)


def test_delete_train():
    headers = {}
    train_id = 1
    response = delete_train(client, train_id, headers)


def test_update_train():
    headers = {}
    train = {'id': 1, 'name': 'Train Updated'}
    response = update_train(client, train, headers)


def test_create_train():
    headers = {}
    train = {'name': 'New Train'}
    response = create_train(client, train, headers)


def test_get_configs():
    headers = {}
    response = get_configs(client, headers)


def test_delete_config():
    headers = {}
    config_name = 'test_config'
    response = delete_config(client, config_name, headers)


def test_update_config():
    headers = {}
    config = {'name': 'test_config', 'value': 'Updated Value'}
    response = update_config(client, config, headers)


def test_create_config():
    headers = {}
    config = {'name': 'new_config', 'value': 'New Config Value'}
    response = create_config(client, config, headers)


def test_get_prices():
    headers = {}
    response = get_prices(client, headers)


def test_delete_price():
    headers = {}
    price_id = 1
    response = delete_price(client, price_id, headers)


def test_update_price():
    headers = {}
    price = {'id': 1, 'price': 10.99}
    response = update_price(client, price, headers)


def test_create_price():
    headers = {}
    price = {'price': 9.99}
    response = create_price(client, price, headers)
