from typing import List
import requests
from dataclasses import dataclass, asdict
from service.common import *


@dataclass
class SecurityConfig(DataclassInstance):
    name: str
    id: str
    value: str
    description: str

@dataclass
class Return(DataclassInstance):
    status: str
    msg: str
    data: List


def home(client: requests.Session, host: str, headers: dict):
    """
    /api/v1/securityservice/welcome GET
    """
    url = "/api/v1/securityservice/welcome"
    response = client.request(url=host + url, method='GET', headers=headers)
    return response.text


def find_all_security_config(client: requests.Session, host: str, headers: dict):
    """
    /api/v1/securityservice/securityConfigs GET
    """
    url = "/api/v1/securityservice/securityConfigs"
    response = client.request(url=host + url, method='GET', headers=headers)
    return from_dict(Return, response.json())


def add_new_security_config(client: requests.Session, info: SecurityConfig, host: str, headers: dict):
    """
    /api/v1/securityservice/securityConfigs POST
    """
    url = "/api/v1/securityservice/securityConfigs"
    response = client.request(url=host + url, method='POST', json=asdict(info), headers=headers)
    return response.json()


def modify_security_config(client: requests.Session, info: SecurityConfig, host: str, headers: dict):
    """
    /api/v1/securityservice/securityConfigs PUT
    """
    url = "/api/v1/securityservice/securityConfigs"
    response = client.request(url=host + url, method='PUT', json=asdict(info), headers=headers)
    return response.json()


def delete_security_config(client: requests.Session, config_id: str, host: str, headers: dict):
    """
    /api/v1/securityservice/securityConfigs/{id} DELETE
    """
    url = f"/api/v1/securityservice/securityConfigs/{config_id}"
    response = client.request(url=host + url, method='DELETE', headers=headers)
    return response.json()


def check_security(client: requests.Session, account_id: str, host: str, headers: dict):
    """
    /api/v1/securityservice/securityConfigs/{accountId} GET
    """
    url = f"/api/v1/securityservice/securityConfigs/{account_id}"
    response = client.request(url=host + url, method='GET', headers=headers)
    return response.json()