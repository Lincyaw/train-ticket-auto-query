from typing import List
import requests
from service.common import *
from dataclasses import dataclass, field
from uuid import UUID


@dataclass
class Assurance(DataclassInstance):
    id: UUID
    orderId: UUID
    typeIndex: int


@dataclass
class Response(DataclassInstance):
    status: int
    msg: str
    data: List[Assurance] = field(default_factory=list)


def welcome(client: requests.Session, host: str, headers: dict):
    """
    /api/v1/assuranceservice/welcome GET
    """
    url = "/api/v1/assuranceservice/welcome"
    response = client.request(url=host + url, method='GET', headers=headers)
    return response.text


def get_all_assurances(client: requests.Session, host: str, headers: dict):
    """
    /api/v1/assuranceservice/assurances GET
    """
    url = "/api/v1/assuranceservice/assurances"
    response = client.request(url=host + url, method='GET', headers=headers)
    return from_dict(Response, response.json())


def get_all_assurance_types(client: requests.Session, host: str, headers: dict):
    """
    /api/v1/assuranceservice/assurances/types GET
    """
    url = "/api/v1/assuranceservice/assurances/types"
    response = client.request(url=host + url, method='GET', headers=headers)
    return from_dict(Response, response.json())


def delete_assurance_by_id(client: requests.Session, assurance_id: UUID, host: str, headers: dict):
    """
    /api/v1/assuranceservice/assurances/assuranceid/{assuranceId} DELETE
    """
    url = f"/api/v1/assuranceservice/assurances/assuranceid/{assurance_id}"
    response = client.request(url=host + url, method='DELETE', headers=headers)
    return from_dict(Response, response.json())


def delete_assurance_by_order_id(client: requests.Session, order_id: UUID, host: str, headers: dict):
    """
    /api/v1/assuranceservice/assurances/orderid/{orderId} DELETE
    """
    url = f"/api/v1/assuranceservice/assurances/orderid/{order_id}"
    response = client.request(url=host + url, method='DELETE', headers=headers)
    return response.json()


def modify_assurance(client: requests.Session, assurance_id: UUID, order_id: UUID, type_index: int, host: str, headers: dict):
    """
    /api/v1/assuranceservice/assurances/{assuranceId}/{orderId}/{typeIndex} PATCH
    """
    url = f"/api/v1/assuranceservice/assurances/{assurance_id}/{order_id}/{type_index}"
    response = client.request(url=host + url, method='PATCH', headers=headers)
    return from_dict(Response, response.json())


def create_new_assurance(client: requests.Session, type_index: int, order_id: UUID, host: str, headers: dict):
    """
    /api/v1/assuranceservice/assurances/{typeIndex}/{orderId} GET
    """
    url = f"/api/v1/assuranceservice/assurances/{type_index}/{order_id}"
    response = client.request(url=host + url, method='GET', headers=headers)
    return from_dict(Response, response.json())


def get_assurance_by_id(client: requests.Session, assurance_id: UUID, host: str, headers: dict):
    """
    /api/v1/assuranceservice/assurances/assuranceid/{assuranceId} GET
    """
    url = f"/api/v1/assuranceservice/assurances/assuranceid/{assurance_id}"
    response = client.request(url=host + url, method='GET', headers=headers)
    return from_dict(Response, response.json())


def find_assurance_by_order_id(client: requests.Session, order_id: UUID, host: str, headers: dict):
    """
    /api/v1/assuranceservice/assurance/orderid/{orderId} GET
    """
    url = f"/api/v1/assuranceservice/assurance/orderid/{order_id}"
    response = client.request(url=host + url, method='GET', headers=headers)
    return from_dict(Response, response.json())