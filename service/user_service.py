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


def test_hello(client: requests.Session, host: str):
    """
    /api/v1/userservice/users/hello GET
    """
    url = "/api/v1/userservice/users/hello"
    response = client.request(url=host + url, method='GET')
    return response.text


def get_all_users(client: requests.Session, host: str, headers: dict):
    """
    /api/v1/userservice/users GET
    """
    url = "/api/v1/userservice/users"
    response = client.request(url=host + url, method='GET', headers=headers)
    return from_dict(Response, response.json())


def get_user_by_username(client: requests.Session, username: str, host: str, headers: dict):
    """
    /api/v1/userservice/users/{userName} GET
    """
    url = f"/api/v1/userservice/users/{username}"
    response = client.request(url=host + url, method='GET', headers=headers)
    return from_dict(Response, response.json())


def get_user_by_userid(client: requests.Session, user_id: str, host: str, headers: dict):
    """
    /api/v1/userservice/users/id/{userId} GET
    """
    url = f"/api/v1/userservice/users/id/{user_id}"
    response = client.request(url=host + url, method='GET', headers=headers)
    return from_dict(Response, response.json())


def register_user(client: requests.Session, user: UserDto, host: str, headers: dict):
    """
    /api/v1/userservice/users/register POST
    """
    url = "/api/v1/userservice/users/register"
    response = client.request(url=host + url, method='POST', json=asdict(user), headers=headers)
    return response.json()


def delete_user_by_id(client: requests.Session, user_id: str, host: str, headers: dict):
    """
    /api/v1/userservice/users/{userId} DELETE
    """
    url = f"/api/v1/userservice/users/{user_id}"
    response = client.request(url=host + url, method='DELETE', headers=headers)
    return response.json()


def update_user(client: requests.Session, user: UserDto, host: str, headers: dict):
    """
    /api/v1/userservice/users PUT
    """
    url = "/api/v1/userservice/users"
    response = client.request(url=host + url, method='PUT', json=asdict(user), headers=headers)
    return from_dict(Response, response.json())