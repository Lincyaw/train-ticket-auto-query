from common import *
from admin_user import *

client = HttpClient()


def test_get_welcome():
    headers = {'Content-Type': 'application/json'}

    result = get_welcome(client, headers)
    print(f"get_welcome result: {result}")


def test_get_users():
    client = HttpClient()
    headers = {'Content-Type': 'application/json'}

    result = get_users(client, headers)
    print(f"get_users result: {result}")


def test_update_user():
    client = HttpClient()
    headers = {'Content-Type': 'application/json'}
    user_dto = {'username': 'testuser', 'password': 'testpassword'}

    result = update_user(client, user_dto, headers)
    print(f"update_user result: {result}")


def test_create_user():
    client = HttpClient()
    headers = {'Content-Type': 'application/json'}
    user_dto = {'username': 'newuser', 'password': 'newpassword'}

    result = create_user(client, user_dto, headers)
    print(f"create_user result: {result}")


def test_delete_user():
    client = HttpClient()
    headers = {'Content-Type': 'application/json'}
    user_id = '123'

    result = delete_user(client, user_id, headers)
    print(f"delete_user result: {result}")
