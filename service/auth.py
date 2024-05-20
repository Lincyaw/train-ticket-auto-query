from config import *


def hello(client):
    url = "/api/v1/auth/hello"
    response = client.request(BASE_URL + url, method='GET')
    return response.text if response else None


def users_hello(client):
    url = "/api/v1/users/hello"
    response = client.request(BASE_URL + url, method='GET')
    return response.json() if response else None


def users_login(client, basic_auth_dto, headers):
    url = "/api/v1/users/login"
    response = client.request(BASE_URL + url, method='POST',
                              json=basic_auth_dto, headers=headers)
    return response.json() if response else None


def get_users(client, headers):
    url = "/api/v1/users"
    response = client.request(BASE_URL + url, method='GET', headers=headers)
    return response.json() if response else None


def delete_user(client, user_id, headers):
    url = f"/api/v1/users/{user_id}"
    response = client.request(BASE_URL + url, method='DELETE', headers=headers)
    return response.json() if response else None