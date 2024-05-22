from service.auth_service import *

BASE_URL = "http://10.10.10.220:30193"
headers = {
    'Proxy-Connection': 'keep-alive',
    'Accept': 'application/json',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
    'Content-Type': 'application/json',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Connection': 'keep-alive',
}


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
    # 4. 改（如果有）
    # 5. 查；验证有没有改成功
    # 6. 删
    # 7. 查；验证有没有删成功
