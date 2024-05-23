from service.auth_service import *
from service.test_utils import *

def test_get_auth_hello():
    client = requests.Session()
    result = auth_hello(client, BASE_URL)
    print(f"get_auth_hello result: {result}")
    assert result == "hello"


def test_create_default_user():
    auth_dto = DtoCreateUser(userId='111111', userName='default3333',
                             password='12345226')
    client = requests.Session()
    result = create_default_user(client, auth_dto, BASE_URL)
    assert result.data.userId == auth_dto.userId
    assert result.data.userName == auth_dto.userName
    assert result.data.password == auth_dto.password


def test_get_users_hello():
    client = requests.Session()
    basic_auth_dto = DtoLoginUser(username='admin',
                                  password='222222', verificationCode="123")
    token = users_login(client, basic_auth_dto, headers, BASE_URL)
    client.headers.update({'Authorization': f'Bearer {token}'})
    result = users_hello(client, BASE_URL)
    print(f"get_users_hello result: {result}")
    assert result == "Hello"


def test_post_users_login():
    client = requests.Session()
    basic_auth_dto = DtoLoginUser(username='fdse_microservice',
                                  password='111111', verificationCode="123")
    headers = {'Content-Type': 'application/json'}
    result = users_login(client, basic_auth_dto, headers, BASE_URL)
    print(f"post_users_login result: {result}")


def test_delete_user():
    client = requests.Session()
    basic_auth_dto = DtoLoginUser(username='admin',
                                  password='222222', verificationCode="123")
    token = users_login(client, basic_auth_dto, headers, BASE_URL)
    client.headers.update({'Authorization': f'Bearer {token}'})
    result = delete_user(client, 1, BASE_URL)
    print(f"delete user result: {result}")


def test_get_users():
    client = requests.Session()
    basic_auth_dto = DtoLoginUser(username='admin',
                                  password='222222', verificationCode="123")
    token = users_login(client, basic_auth_dto, headers, BASE_URL)
    client.headers.update({'Authorization': f'Bearer {token}'})
    result = get_users(client, BASE_URL)
    for user in result:
        print(f"get_users result: {user}")


def test_end2end():
    """
    TODO: 增改删查
    """
    # 1. 查
    # 2. 加
    # 3. 查；验证有没有加成功
    # 4. 改（如果有）(是否有 Update)
    # 5. 查；验证有没有改成功 (如果有)（是否有update）
    # 6. 删
    # 7. 查；验证有没有删成功
    """
    End-to-end test: query, add, update, delete
    """
    client = requests.Session()
    basic_auth_dto = DtoLoginUser(username='admin',
                                  password='222222', verificationCode="123")
    token = users_login(client, basic_auth_dto, headers, BASE_URL)
    client.headers.update({'Authorization': f'Bearer {token}'})

    # 1. Query
    users_before = get_users(client, BASE_URL)
    print("Users before:", users_before)

    # 2. Add
    new_user_dto = DtoCreateUser(userId='999990099', userName='newer0011',
                                 password='newpassword')
    new_user = create_default_user(client, new_user_dto, BASE_URL)
    print("New user added:", new_user)

    # 3. Query and verify addition
    users_after_add = get_users(client, BASE_URL)
    print("Users after addition:", users_after_add)
    assert len(users_after_add) == len(users_before) + 1
    assert any(user.userId == new_user_dto.userId for user in users_after_add)

    # # 4. Update (if the user exists)
    # updated_user_dto = DtoCreateUser(userId=new_user_dto.userId, userName='updateduser',
    #                                  password='updatedpassword')
    # updated_user = create_default_user(client, updated_user_dto, BASE_URL)
    # print("User updated:", updated_user)

    # # 5. Query and verify update
    # users_after_update = get_users(client, BASE_URL)
    # print("Users after update:", users_after_update)
    # assert any(user.userName == updated_user_dto.userName for user in users_after_update)

    # 6. Delete
    delete_result = delete_user(client, new_user_dto.userId, BASE_URL)
    print("User deleted:", delete_result)

    # 7. Query and verify deletion
    users_after_delete = get_users(client, BASE_URL)
    print("Users after deletion:", users_after_delete)
    assert len(users_after_delete) == len(users_before)
    assert not any(user.userId == new_user_dto.userId for user in users_after_delete)
