import requests
from dataclasses import dataclass, asdict
from service.common import *
from typing import List


@dataclass
class WaitListOrderVO:
    accountId: str
    contactsId: str
    tripId: str
    seatType: int
    date: str
    from_location: str
    to: str
    price: str

@dataclass
class WaitListOrderResult(DataclassInstance):
    message: str
    status: bool


@dataclass
class GetAllOrdersResult(DataclassInstance):
    message: str
    status: bool
    data: List[WaitListOrderVO]


@dataclass
class GetWaitListOrdersResult(DataclassInstance):
    message: str
    status: bool
    data: List[WaitListOrderVO]

@dataclass
class ReturnBody(DataclassInstance):
    status: int
    msg: str
    data: List


def welcome(client: requests.Session, host: str, headers: dict):
    """
    /api/v1/waitorderservice/welcome GET
    """
    url = "/api/v1/waitorderservice/welcome"
    response = client.request(url=host + url, method='GET', headers=headers)
    return response.text


def create_wait_list_order(client: requests.Session, order: WaitListOrderVO, host: str, headers: dict):
    """
    /api/v1/waitorderservice/order POST
    """
    url = "/api/v1/waitorderservice/order"
    response = client.request(url=host + url, method='POST', headers=headers, json=asdict(order))
    return response.json()


def get_all_orders(client: requests.Session, host: str, headers: dict):
    """
    /api/v1/waitorderservice/orders GET
    """
    url = "/api/v1/waitorderservice/orders"
    response = client.request(url=host + url, method='GET', headers=headers)
    return from_dict(ReturnBody, response.json())


def get_wait_list_orders(client: requests.Session, host: str, headers: dict):
    """
    /api/v1/waitorderservice/waitlistorders GET
    """
    url = "/api/v1/waitorderservice/waitlistorders"
    response = client.request(url=host + url, method='GET', headers=headers)
    return from_dict(ReturnBody, response.json())
