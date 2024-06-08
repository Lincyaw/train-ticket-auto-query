from typing import List
import requests
from dataclasses import dataclass, asdict
from service.common import *


@dataclass
class TrainType(DataclassInstance):
    id: str
    name: str
    economyClass: int
    confortClass: int
    averageSpeed: int


def home(client: requests.Session, host: str, headers: dict):
    """
    /api/v1/trainservice/trains/welcome GET
    """
    url = "/api/v1/trainservice/trains/welcome"
    response = client.request(url=host + url, method='GET', headers=headers)
    return response.text


def create(client: requests.Session, train_type: TrainType, host: str, headers: dict):
    """
    /api/v1/trainservice/trains POST
    """
    url = "/api/v1/trainservice/trains"
    response = client.request(url=host + url, method='POST', json=asdict(train_type), headers=headers)
    return response.json()


def retrieve(client: requests.Session, train_type_id: str, host: str, headers: dict):
    """
    /api/v1/trainservice/trains/{id} GET
    """
    url = f"/api/v1/trainservice/trains/{train_type_id}"
    response = client.request(url=host + url, method='GET', headers=headers)
    return response.json()


def retrieve_by_name(client: requests.Session, train_type_name: str, host: str, headers: dict):
    """
    /api/v1/trainservice/trains/byName/{name} GET
    """
    url = f"/api/v1/trainservice/trains/byName/{train_type_name}"
    response = client.request(url=host + url, method='GET', headers=headers)
    return response.json()


def retrieve_by_names(client: requests.Session, train_type_names: List[str], host: str, headers: dict):
    """
    /api/v1/trainservice/trains/byNames POST
    """
    url = "/api/v1/trainservice/trains/byNames"
    response = client.request(url=host + url, method='POST', json=train_type_names, headers=headers)
    return response.json()


def update(client: requests.Session, train_type: TrainType, host: str, headers: dict):
    """
    /api/v1/trainservice/trains PUT
    """
    url = "/api/v1/trainservice/trains"
    response = client.request(url=host + url, method='PUT', json=asdict(train_type), headers=headers)
    return response.json()


def delete(client: requests.Session, train_type_id: str, host: str, headers: dict):
    """
    /api/v1/trainservice/trains/{id} DELETE
    """
    url = f"/api/v1/trainservice/trains/{train_type_id}"
    response = client.request(url=host + url, method='DELETE', headers=headers)
    return response.json()


def query(client: requests.Session, host: str, headers: dict):
    """
    /api/v1/trainservice/trains GET
    """
    url = "/api/v1/trainservice/trains"
    response = client.request(url=host + url, method='GET', headers=headers)
    return response.json()
