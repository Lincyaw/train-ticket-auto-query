from user_service import *
from common import *
from user_service import *

client = HttpClient()

# def userService_hello(client):
#     url = "/api/v1/userservice/users/hello"
#     response = client.request(BASE_URL + url, method='GET')
#     return response.json() if response else None
#
def test_userService_hello():
    result = userService_hello(client)
    print(f"test_userService_hello result: {result}")

# def get_all_users(client, headers):
#     url = '/api/v1/userservice/users'
#     response = client.request(BASE_URL + url, method='GET', headers = headers)
#     return response.json() if response else None
#
def test_get_all_users():
    result = get_all_users(client,None)
    print(f"test_get_all_users result: {result}")

# def get_user_by_username(client, user_name, headers):
#     url = f"/api/v1/userservice/users/{user_name}"
#     response = client.request(BASE_URL+url, method='GET', headers=headers)
#     return response.json() if response else None
#
def test_get_user_by_username():
    result = get_user_by_username(client,'Amy',None)
    print(f"test_get_user_by_username result: {result}")
# def get_user_by_id(client, user_id, headers):
#     url = f"/api/v1/userservice/users/id/{user_id}"
#     response = client.request(BASE_URL + url, method='GET', headers=headers)
#     return response.json() if response else None
#
def test_get_user_by_id():
    result = get_user_by_id(client,1,None)
    print(f"test_get_user_by_id result: {result}")
# def create_user(client, user_dto:User_dto, headers):
#     url = "/api/v1/userservice/users/register"
#     response = client.request(BASE_URL + url, method='POST',
#                               json=user_dto.to_dict(), headers=headers)
#     return response.json() if response else None
#
# def __init__(self, userId, userName, password, gender, documentType, documentNum, email):
def test_create_user():
    user_dto = User_dto(1,'Amy','123456','Female',None,None,'123456@gmail.com')
    result = create_user(client,user_dto,None)
    print(f"test_create_user result: {result}")
# def delete_user_by_id(client, user_id, headers):
#     url = f"/api/v1/userservice/users/{user_id}"
#     response = client.request(BASE_URL + url, method='DELETE', headers=headers)
#     return response.json() if response else None
#
def test_delete_user_by_id():
    result = delete_user_by_id(client,1,None)
    print(f"test_delete_user_by_id: {result}")
# def update_user(client, user_dto:User_dto, headers):
#     url = '/api/v1/userservice/users'
#     response = client.request(BASE_URL + url, method='PUT', headers=headers, json=user_dto.to_dict())
#     return response.json() if response else None
def test_update_user():
    user_dto=User_dto(1, 'Amy', '123456', 'Female', None, None, '123456@gmail.com')
    result = update_user(client,user_dto,None)
    print(f"test_update_user: {result}")