from config import *


def get_welcome(client, headers):
    url = "/api/v1/adminuserservice/users/welcome"
    response = client.request(BASE_URL + url, method='GET', headers=headers)
    return response.text if response else None


def get_users(client, headers):
    url = "/api/v1/adminuserservice/users"
    response = client.request(BASE_URL + url, method='GET', headers=headers)
    return response.json() if response else None


def update_user(client, user_dto, headers):
    url = "/api/v1/adminuserservice/users"
    response = client.request(BASE_URL + url, method='PUT', json=user_dto,
                              headers=headers)
    return response.json() if response else None


def create_user(client, user_dto, headers):
    url = "/api/v1/adminuserservice/users"
    response = client.request(BASE_URL + url, method='POST', json=user_dto,
                              headers=headers)
    return response.json() if response else None


def delete_user(client, user_id, headers):
    url = f"/api/v1/adminuserservice/users/{user_id}"
    response = client.request(BASE_URL + url, method='DELETE', headers=headers)
    return response.json() if response else None
