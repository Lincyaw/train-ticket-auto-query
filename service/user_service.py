from config import *

def userService_hello(client):
    url = "/api/v1/userservice/users/hello"
    response = client.request(BASE_URL + url, method='GET')
    return response.text if response else None

def get_all_users(client, headers):
    url = '/api/v1/userservice/users'
    response = client.request(BASE_URL + url, method='GET', headers = headers)
    return response.json() if response else None

def get_user_by_username(client, user_name, headers):
    url = f"/api/v1/userservice/users/{user_name}"
    response = client.request(BASE_URL+url, method='GET', headers=headers)
    return response.json() if response else None

def get_user_by_id(client, user_id, headers):
    url = f"/api/v1/userservice/users/id/{user_id}"
    response = client.request(BASE_URL + url, method='GET', headers=headers)
    return response.json() if response else None

def create_user(client, user_dto, headers):
    url = "/api/v1/userservice/users/register"
    response = client.request(BASE_URL + url, method='POST',
                              json=user_dto.to_dict(), headers=headers)
    return response.json() if response else None

def delete_user_by_id(client, user_id, headers):
    url = f"/api/v1/userservice/users/{user_id}"
    response = client.request(BASE_URL + url, method='DELETE', headers=headers)
    return response.json() if response else None

def update_user(client, user_dto, headers):
    url = '/api/v1/userservice/users'
    response = client.request(BASE_URL + url, method='PUT', headers=headers, json=user_dto.to_dict())
    return response.json() if response else None