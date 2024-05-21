

from auth_service import *
from common import *

client = HttpClient()


def test_get_auth_hello():
    result = auth_hello(client)
    print(f"get_auth_hello result: {result}")
    assert result == "hello"




def test_create_default_user():
    auth_dto = DtoCreateUser(userId='1', userName='default', password='123456')
    result = create_defalt_user(client, auth_dto)
    assert result.data.userId == auth_dto.userId
    assert result.data.userName == auth_dto.userName
    assert result.data.password == auth_dto.password


def test_get_users_hello():
    result = users_hello(client)
    print(f"get_users_hello result: {result}")
    assert result == "Hello"


def test_post_users_login():
    basic_auth_dto = DtoCreateUser(userId="1", userName='default', password='123456')
    headers = {'Content-Type': 'application/json'}

    result = users_login(client, basic_auth_dto, headers)
    print(f"post_users_login result: {result}")


def test_delete_user():
    result = delete_user(client, 1, None)
    print(f"get_users result: {result}")


def test_get_users():
    result = get_users(client, None)
    print(f"get_users result: {result}")
