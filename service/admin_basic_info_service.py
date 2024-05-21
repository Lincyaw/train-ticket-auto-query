from config import *


def get_welcome(client, headers):
    url = '/api/v1/adminbasicservice/welcome'
    response = client.request(BASE_URL + url, headers=headers)
    return response.text if response else None


def get_contacts(client, headers):
    url = '/api/v1/adminbasicservice/adminbasic/contacts'
    response = client.request(BASE_URL + url, headers=headers)
    return response.json() if response else None


def delete_contact(client, contact_id, headers):
    url = f'/api/v1/adminbasicservice/adminbasic/contacts/{contact_id}'
    response = client.request(BASE_URL + url, method='DELETE', headers=headers)
    return response.json() if response else None


def update_contact(client, contact, headers):
    url = '/api/v1/adminbasicservice/adminbasic/contacts'
    response = client.request(BASE_URL + url, method='PUT', json=contact,
                              headers=headers)
    return response.json() if response else None


def create_contact(client, contact, headers):
    url = '/api/v1/adminbasicservice/adminbasic/contacts'
    response = client.request(BASE_URL + url, method='POST', json=contact,
                              headers=headers)
    return response.json() if response else None


def get_stations(client, headers):
    url = '/api/v1/adminbasicservice/adminbasic/stations'
    response = client.request(BASE_URL + url, headers=headers)
    return response.json() if response else None


def delete_station(client, station_id, headers):
    url = f'/api/v1/adminbasicservice/adminbasic/stations/{station_id}'
    response = client.request(BASE_URL + url, method='DELETE', headers=headers)
    return response.json() if response else None


def update_station(client, station, headers):
    url = '/api/v1/adminbasicservice/adminbasic/stations'
    response = client.request(BASE_URL + url, method='PUT', json=station,
                              headers=headers)
    return response.json() if response else None


def create_station(client, station, headers):
    url = '/api/v1/adminbasicservice/adminbasic/stations'
    response = client.request(BASE_URL + url, method='POST', json=station,
                              headers=headers)
    return response.json() if response else None


def get_trains(client, headers):
    url = '/api/v1/adminbasicservice/adminbasic/trains'
    response = client.request(BASE_URL + url, headers=headers)
    return response.json() if response else None


def delete_train(client, train_id, headers):
    url = f'/api/v1/adminbasicservice/adminbasic/trains/{train_id}'
    response = client.request(BASE_URL + url, method='DELETE', headers=headers)
    return response.json() if response else None


def update_train(client, train, headers):
    url = '/api/v1/adminbasicservice/adminbasic/trains'
    response = client.request(BASE_URL + url, method='PUT', json=train,
                              headers=headers)
    return response.json() if response else None


def create_train(client, train, headers):
    url = '/api/v1/adminbasicservice/adminbasic/trains'
    response = client.request(BASE_URL + url, method='POST', json=train,
                              headers=headers)
    return response.json() if response else None


def get_configs(client, headers):
    url = '/api/v1/adminbasicservice/adminbasic/configs'
    response = client.request(BASE_URL + url, headers=headers)
    return response.json() if response else None


def delete_config(client, config_name, headers):
    url = f'/api/v1/adminbasicservice/adminbasic/configs/{config_name}'
    response = client.request(BASE_URL + url, method='DELETE', headers=headers)
    return response.json() if response else None


def update_config(client, config, headers):
    url = '/api/v1/adminbasicservice/adminbasic/configs'
    response = client.request(BASE_URL + url, method='PUT', json=config,
                              headers=headers)
    return response.json() if response else None


def create_config(client, config, headers):
    url = '/api/v1/adminbasicservice/adminbasic/configs'
    response = client.request(BASE_URL + url, method='POST', json=config,
                              headers=headers)
    return response.json() if response else None


def get_prices(client, headers):
    url = '/api/v1/adminbasicservice/adminbasic/prices'
    response = client.request(BASE_URL + url, headers=headers)
    return response.json() if response else None


def delete_price(client, price_id, headers):
    url = f'/api/v1/adminbasicservice/adminbasic/prices/{price_id}'
    response = client.request(BASE_URL + url, method='DELETE', headers=headers)
    return response.json() if response else None


def update_price(client, price, headers):
    url = '/api/v1/adminbasicservice/adminbasic/prices'
    response = client.request(BASE_URL + url, method='PUT', json=price,
                              headers=headers)
    return response.json() if response else None


def create_price(client, price, headers):
    url = '/api/v1/adminbasicservice/adminbasic/prices'
    response = client.request(BASE_URL + url, method='POST', json=price,
                              headers=headers)
    return response.json() if response else None
