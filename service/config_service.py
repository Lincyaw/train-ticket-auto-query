import requests
from service.common import *
from dataclasses import dataclass, asdict


@dataclass
class Config(DataclassInstance):
    name: str
    value: str
    description: str


def welcome(client: requests.Session, host: str, headers: dict):
    """
    /api/v1/configservice/welcome GET
    """
    url = "/api/v1/configservice/welcome"
    response = client.request(url=host + url, method='GET', headers=headers)
    return response.text


def query_all(client: requests.Session, host: str, headers: dict):
    """
    /api/v1/configservice/configs GET
    """
    url = "/api/v1/configservice/configs"
    response = client.request(url=host + url, method='GET', headers=headers)
    return from_dict(Config, response.json())


def create_config(client: requests.Session, config: Config, host: str, headers: dict):
    """
    /api/v1/configservice/configs POST
    """
    url = "/api/v1/configservice/configs"
    response = client.request(url=host + url, method='POST', json=asdict(config), headers=headers)
    return response.json()


def update_config(client: requests.Session, config: Config, host: str, headers: dict):
    """
    /api/v1/configservice/configs PUT
    """
    url = "/api/v1/configservice/configs"
    response = client.request(url=host + url, method='PUT', json=asdict(config), headers=headers)
    return response.json()


def delete_config(client: requests.Session, config_name: str, host: str, headers: dict):
    """
    /api/v1/configservice/configs/{configName} DELETE
    """
    url = f"/api/v1/configservice/configs/{config_name}"
    response = client.request(url=host + url, method='DELETE', headers=headers)
    return response.json()


def retrieve_config(client: requests.Session, config_name: str, host: str, headers: dict):
    """
    /api/v1/configservice/configs/{configName} GET
    """
    url = f"/api/v1/configservice/configs/{config_name}"
    response = client.request(url=host + url, method='GET', headers=headers)
    return from_dict(Config, response.json())