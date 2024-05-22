from typing import List
import requests
from service.common import *
from dataclasses import dataclass, asdict


@dataclass
class DtoCreateUser:
    userId: str
    userName: str
    password: str


@dataclass
class RegisterResponse(DataclassInstance):
    data: DtoCreateUser
    msg: str
    status: int


@dataclass
class Authority(DataclassInstance):
    authority: str


@dataclass
class User(DataclassInstance):
    userId: str
    username: str
    password: str
    roles: List[str]
    enabled: bool
    accountNonLocked: bool
    credentialsNonExpired: bool
    accountNonExpired: bool
    authorities: List[Authority]


@dataclass
class DtoLoginUser(DataclassInstance):
    password: str
    username: str
    verificationCode: str


def auth_hello(client: requests.Session, host: str):
    """
    /api/v1/auth/hello GET
    """
    url = "/api/v1/auth/hello"
    response = client.request(url=host + url, method='GET')
    return response.text


def create_default_user(client: requests.Session, auth_dto: DtoCreateUser,
                        host: str):
    """
    /api/v1/auth POST
    """
    url = "/api/v1/auth"
    response = client.request(url=host + url,
                              method='POST',
                              json=asdict(auth_dto))
    return from_dict(RegisterResponse, response.json())


def get_users(client: requests.Session, host: str):
    """
    /api/v1/users GET
    需要 admin 用户权限
    """
    url = "/api/v1/users"
    response = client.request(url=host + url, method='GET',
                              headers={"Accept": "*/*"})
    users = []
    for item in response.json():
        authorities = [Authority(**auth) for auth in item['authorities']]
        user = User(
            userId=item['userId'],
            username=item['username'],
            password=item['password'],
            roles=item['roles'],
            enabled=item['enabled'],
            accountNonLocked=item['accountNonLocked'],
            credentialsNonExpired=item['credentialsNonExpired'],
            accountNonExpired=item['accountNonExpired'],
            authorities=authorities
        )
        users.append(user)
    return users


def users_hello(client: requests.Session, host: str):
    """
    /api/v1/users/hello GET
    """
    url = '/api/v1/users/hello'
    response = client.request(url=host + url, method='GET')
    return response.text if response else None


def users_login(client: requests.Session, basic_auth_dto: DtoLoginUser,
                headers, host: str):
    """
    /api/v1/users/login POST
    """
    url = "/api/v1/users/login"
    response = client.request(url=host + url, method='POST',
                              json=asdict(basic_auth_dto), headers=headers)
    # print(response)
    if response and response.json():
        response_json = response.json()
        # 检查 'data' 和 'token' 字段是否存在
        if 'data' in response_json and 'token' in response_json['data']:
            return response_json['data']['token']
        else:
            print("Response JSON does not contain 'data' or 'token' fields.")
            return None
    else:
        print("Empty or invalid response.")
        return None


def delete_user(client: requests.Session, user_id, host: str):
    """
    /api/v1/users/{userId} DELETE
    需要 admin 用户权限
    """
    url = f"/api/v1/users/{user_id}"
    response = client.request(url=host + url, method='DELETE')
    return response.json() if response else None
