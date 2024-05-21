from auth_service import *
from common import *

client = HttpClient()


def test_get_auth_hello():
    result = auth_hello(client)
    print(f"get_auth_hello result: {result}")
    assert result == "hello"


def test_create_default_user():
    auth_dto = DtoCreateUser(userId='111111', userName='default3',
                             password='12345226')
    result = create_defalt_user(client, auth_dto)
    assert result.data.userId == auth_dto.userId
    assert result.data.userName == auth_dto.userName
    assert result.data.password == auth_dto.password


def test_get_users_hello():
    result = users_hello(client)
    print(f"get_users_hello result: {result}")
    assert result == "Hello"


def test_post_users_login():
    basic_auth_dto = DtoLoginUser(username='default2',
                                  password='123456', verificationCode="123")
    headers = {'Content-Type': 'application/json'}

    result = users_login(client, basic_auth_dto, headers)
    print(f"post_users_login result: {result}")


def test_delete_user():
    admin_client = HttpClient(max_samples=3, admin=True)
    result = delete_user(admin_client, 1)
    print(f"delete user result: {result}")


def test_get_users():
    admin = HttpClient(admin=True)
    result = get_users(admin)
    for user in result:
        print(f"get_users result: {user}")
