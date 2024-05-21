from typing import List
from common import *
from dataclasses import dataclass, asdict


@dataclass
class DtoCreateUser:
    userId: str
    userName: str
    password: str


@dataclass
class RegisterResponse:
    data: DtoCreateUser
    msg: str
    status: int


@dataclass
class Authority:
    authority: str

@dataclass
class User:
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
class DtoLoginUser:
    password: str
    username: str
    verificationCode: str


def auth_hello(client: HttpClient):
    """
    /api/v1/auth/hello GET
    """
    url = "/api/v1/auth/hello"
    response = client.request(BASE_URL + url, method='GET')
    return response.text


def create_defalt_user(client: HttpClient, auth_dto: DtoCreateUser):
    """
    /api/v1/auth POST
    """
    url = "/api/v1/auth"
    response = client.request(BASE_URL + url,
                              method='POST',
                              json=asdict(auth_dto),
                              headers={'Content-Type': 'application/json',
                                       'Accept': 'application/json'
                                       })
    return from_dict(RegisterResponse, response.json())


def get_users(client: HttpClient):
    """
    /api/v1/users GET
    需要 admin 用户权限
    """
    url = "/api/v1/users"
    response = client.request(BASE_URL + url, method='GET',
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


def users_hello(client: HttpClient):
    """
    /api/v1/users/hello GET
    """
    url = '/api/v1/users/hello'
    response = client.request(BASE_URL + url, method='GET')
    return response.text if response else None


def users_login(client, basic_auth_dto: DtoLoginUser, headers):
    """
    /api/v1/users/login POST
    """
    url = "/api/v1/users/login"
    response = client.request(BASE_URL + url, method='POST',
                              json=asdict(basic_auth_dto), headers=headers)
    return response.json() if response else None


def delete_user(client, user_id):
    """
    /api/v1/users/{userId} DELETE
    需要 admin 用户权限
    """
    url = f"/api/v1/users/{user_id}"
    response = client.request(BASE_URL + url, method='DELETE')
    return response.json() if response else None
