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
class User:
    accountNonExpired: bool
    accountNonLocked: bool
    authorities: Dict[str, Any]  # 你可以根据具体的结构修改类型
    credentialsNonExpired: bool
    enabled: bool
    password: str
    roles: List[str]
    userId: str
    username: str


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


def get_users(client: HttpClient, headers):
    """
    /api/v1/users GET
    """
    url = "/api/v1/users"
    response = client.request(BASE_URL + url, method='GET',
                              headers={"Accept": "*/*"})
    return from_dict(User, response.json()) if response != None else None


def users_hello(client: HttpClient):
    """
    /api/v1/users/hello GET
    """
    url = '/api/v1/users/hello'
    response = client.request(BASE_URL + url, method='GET')
    return response.text if response else None


def users_login(client, basic_auth_dto: DtoCreateUser, headers):
    """
    /api/v1/users/login POST
    """
    url = "/api/v1/users/login"
    response = client.request(BASE_URL + url, method='POST',
                              json=asdict(basic_auth_dto), headers=headers)
    return response.json() if response else None


def delete_user(client, user_id, headers):
    """
    /api/v1/users/{userId} DELETE
    """
    url = f"/api/v1/users/{user_id}"
    response = client.request(BASE_URL + url, method='DELETE', headers=headers)
    return response.json() if response else None
