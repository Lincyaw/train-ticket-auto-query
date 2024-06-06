from typing import List
import requests
from service.common import *
from dataclasses import dataclass, asdict


@dataclass
class UserDto(DataclassInstance):
    userId: str
    userName: str
    password: str
    gender: int
    documentType: int
    documentNum: str
    email: str


@dataclass
class Response(DataclassInstance):
    status: int
    msg: str
    data: List[UserDto]


def admin_user_welcome(client: requests.Session, host: str, headers: dict):
    """
    /api/v1/adminuserservice/users/welcome GET
    """
    url = "/api/v1/adminuserservice/users/welcome"
    response = client.request(url=host + url, method='GET', headers=headers)
    return response.text


def get_all_users(client: requests.Session, host: str, headers: dict):
    """
    /api/v1/adminuserservice/users GET
    """
    url = "/api/v1/adminuserservice/users"
    response = client.request(url=host + url, method='GET', headers=headers)
    return from_dict(Response, response.json())


def update_user(client: requests.Session, user: UserDto, host: str, headers: dict):
    """
    /api/v1/adminuserservice/users PUT
    """
    url = "/api/v1/adminuserservice/users"
    response = client.request(url=host + url, method='PUT', json=asdict(user), headers=headers)
    return response.json()


def add_user(client: requests.Session, user: UserDto, host: str, headers: dict):
    """
    /api/v1/adminuserservice/users POST
    """
    url = "/api/v1/adminuserservice/users"
    response = client.request(url=host + url, method='POST', json=asdict(user), headers=headers)
    return response.json()


def delete_user(client: requests.Session, user_id: str, host: str, headers: dict):
    """
    /api/v1/adminuserservice/users/{userId} DELETE
    """
    url = f"/api/v1/adminuserservice/users/{user_id}"
    response = client.request(url=host + url, method='DELETE', headers=headers)
    return response.json()
