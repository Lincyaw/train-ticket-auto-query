import requests
from dataclasses import dataclass, asdict
from service.common import *


@dataclass
class Payment(DataclassInstance):
    id: str


def home(client: requests.Session, host: str):
    """
    /api/v1/paymentservice/welcome GET
    """
    url = "/api/v1/paymentservice/welcome"
    response = client.request(url=host + url, method='GET')
    return response.text


def pay(client: requests.Session, info: Payment, host: str, headers: dict):
    """
    /api/v1/paymentservice/payment POST
    """
    url = "/api/v1/paymentservice/payment"
    response = client.request(url=host + url, method='POST', json=asdict(info), headers=headers)
    return response.json()


def add_money(client: requests.Session, info: Payment, host: str, headers: dict):
    """
    /api/v1/paymentservice/payment/money POST
    """
    url = "/api/v1/paymentservice/payment/money"
    response = client.request(url=host + url, method='POST', json=asdict(info), headers=headers)
    return response.json()


def query(client: requests.Session, host: str, headers: dict):
    """
    /api/v1/paymentservice/payment GET
    """
    url = "/api/v1/paymentservice/payment"
    response = client.request(url=host + url, method='GET', headers=headers)
    return response.json()