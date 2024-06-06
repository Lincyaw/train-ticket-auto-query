from typing import List
import requests
from service.common import *
from dataclasses import dataclass, field
from uuid import UUID


@dataclass
class Assurance(DataclassInstance):
    id: str
    orderId: str
    typeIndex: int


@dataclass
class Response(DataclassInstance):
    status: int
    msg: str
    data: List


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
    return response.json()


def delete_assurance_by_order_id(client: requests.Session, order_id: UUID, host: str, headers: dict):
    """
    /api/v1/assuranceservice/assurances/orderid/{orderId} DELETE
    """
    url = f"/api/v1/assuranceservice/assurances/orderid/{order_id}"
    response = client.request(url=host + url, method='DELETE', headers=headers)
    return response.json()


def modify_assurance(client: requests.Session, assuranceId: str, orderId: str, typeIndex: int, host: str, headers: dict):
    """
    /api/v1/assuranceservice/assurances/{assuranceId}/{orderId}/{typeIndex} PATCH
    """
    url = f"/api/v1/assuranceservice/assurances/{assuranceId}/{orderId}/{typeIndex}"
    response = client.request(url=host + url, method='PATCH', headers=headers)
    return response.json()


def create_new_assurance(client: requests.Session, typeIndex: int, orderId: str, host: str, headers: dict):
    """
    /api/v1/assuranceservice/assurances/{typeIndex}/{orderId} GET
    """
    url = f"/api/v1/assuranceservice/assurances/{typeIndex}/{orderId}"
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