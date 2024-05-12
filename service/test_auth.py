from auth import *
from common import *

client = HttpClient()


def test_get_auth_hello():
    result = hello(client)
    assert result == "hello"

# TODO
def test_get_users_hello():
    result = users_hello(client)
    print(f"get_users_hello result: {result}")

def test_post_users_login():
    basic_auth_dto = {'username': 'fdse_microservice', 'password': '111111',
                      "verificationCode": "1234"}
    headers = {'Content-Type': 'application/json'}

    result = users_login(client, basic_auth_dto, headers)
    print(f"post_users_login result: {result}")


def test_get_users():
    result = get_users(client, None)
    print(f"get_users result: {result}")

# def test_delete_user():
#     user_id = '123'
#     headers = {'Authorization': 'Bearer your_token'}
#
#     result = delete_user(client, user_id, None)
#     print(f"delete_user result: {result}")
