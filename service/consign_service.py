import requests
from service.common import *
from dataclasses import dataclass, asdict
from datetime import datetime
from uuid import UUID


@dataclass
class Consign(DataclassInstance):
    accountId: UUID
    handleDate: datetime
    targetDate: datetime
    from_: str
    to: str
    consignee: str
    phone: str
    weight: float
    id: UUID
    orderId: UUID
    consignee_idcard: UUID
    price: float


def welcome(client: requests.Session, host: str, headers: dict):
    """
    /api/v1/consignservice/welcome GET
    """
    url = "/api/v1/consignservice/welcome"
    response = client.request(url=host + url, method='GET', headers=headers)
    return response.text


def insert_consign(client: requests.Session, consign: Consign, host: str, headers: dict):
    """
    /api/v1/consignservice/consigns POST
    """
    url = "/api/v1/consignservice/consigns"
    response = client.request(url=host + url, method='POST', json=asdict(consign), headers=headers)
    return response.json()


def update_consign(client: requests.Session, consign: Consign, host: str, headers: dict):
    """
    /api/v1/consignservice/consigns PUT
    """
    url = "/api/v1/consignservice/consigns"
    response = client.request(url=host + url, method='PUT', json=asdict(consign), headers=headers)
    return response.json()


def find_by_account_id(client: requests.Session, account_id: UUID, host: str, headers: dict):
    """
    /api/v1/consignservice/consigns/account/{id} GET
    """
    url = f"/api/v1/consignservice/consigns/account/{account_id}"
    response = client.request(url=host + url, method='GET', headers=headers)
    return from_dict(Consign, response.json())


def find_by_order_id(client: requests.Session, order_id: UUID, host: str, headers: dict):
    """
    /api/v1/consignservice/consigns/order/{id} GET
    """
    url = f"/api/v1/consignservice/consigns/order/{order_id}"
    response = client.request(url=host + url, method='GET', headers=headers)
    return from_dict(Consign, response.json())


def find_by_consignee(client: requests.Session, consignee: str, host: str, headers: dict):
    """
    /api/v1/consignservice/consigns/{consignee} GET
    """
    url = f"/api/v1/consignservice/consigns/{consignee}"
    response = client.request(url=host + url, method='GET', headers=headers)
    return from_dict(Consign, response.json())