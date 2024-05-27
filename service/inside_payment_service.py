import requests
from dataclasses import dataclass, asdict
from service.common import *


@dataclass
class PaymentInfo(DataclassInstance):
    orderId: str


@dataclass
class AccountInfo(DataclassInstance):
    pass


def home(client: requests.Session, host: str):
    """
    /api/v1/inside_pay_service/welcome GET
    """
    url = "/api/v1/inside_pay_service/welcome"
    response = client.request(url=host + url, method='GET')
    return response.text


def pay(client: requests.Session, info: PaymentInfo, host: str, headers: dict):
    """
    /api/v1/inside_pay_service/inside_payment POST
    """
    url = "/api/v1/inside_pay_service/inside_payment"
    response = client.request(url=host + url, method='POST', json=asdict(info), headers=headers)
    return response.json()


def create_account(client: requests.Session, info: AccountInfo, host: str, headers: dict):
    """
    /api/v1/inside_pay_service/inside_payment/account POST
    """
    url = "/api/v1/inside_pay_service/inside_payment/account"
    response = client.request(url=host + url, method='POST', json=asdict(info), headers=headers)
    return response.json()


def add_money(client: requests.Session, user_id: str, money: str, host: str, headers: dict):
    """
    /api/v1/inside_pay_service/inside_payment/{userId}/{money} GET
    """
    url = f"/api/v1/inside_pay_service/inside_payment/{user_id}/{money}"
    response = client.request(url=host + url, method='GET', headers=headers)
    return response.json()


def query_payment(client: requests.Session, host: str, headers: dict):
    """
    /api/v1/inside_pay_service/inside_payment/payment GET
    """
    url = "/api/v1/inside_pay_service/inside_payment/payment"
    response = client.request(url=host + url, method='GET', headers=headers)
    return response.json()


def query_account(client: requests.Session, host: str, headers: dict):
    """
    /api/v1/inside_pay_service/inside_payment/account GET
    """
    url = "/api/v1/inside_pay_service/inside_payment/account"
    response = client.request(url=host + url, method='GET', headers=headers)
    return response.json()


def draw_back(client: requests.Session, user_id: str, money: str, host: str, headers: dict):
    """
    /api/v1/inside_pay_service/inside_payment/drawback/{userId}/{money} GET
    """
    url = f"/api/v1/inside_pay_service/inside_payment/drawback/{user_id}/{money}"
    response = client.request(url=host + url, method='GET', headers=headers)
    return response.json()


def pay_difference(client: requests.Session, info: PaymentInfo, host: str, headers: dict):
    """
    /api/v1/inside_pay_service/inside_payment/difference POST
    """
    url = "/api/v1/inside_pay_service/inside_payment/difference"
    response = client.request(url=host + url, method='POST', json=asdict(info), headers=headers)
    return response.json()


def query_add_money(client: requests.Session, host: str, headers: dict):
    """
    /api/v1/inside_pay_service/inside_payment/money GET
    """
    url = "/api/v1/inside_pay_service/inside_payment/money"
    response = client.request(url=host + url, method='GET', headers=headers)
    return response.json()