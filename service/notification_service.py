import requests
from dataclasses import dataclass, asdict
from service.common import *


@dataclass
class NotifyInfo(DataclassInstance):
    id: str
    sendStatus: bool
    email: str
    orderNumber: str
    username: str
    startPlace: str
    endPlace: str
    startTime: str
    date: str
    seatClass: str
    seatNumber: str
    price: str


def home(client: requests.Session, host: str):
    """
    /api/v1/notifyservice/welcome GET
    """
    url = "/api/v1/notifyservice/welcome"
    response = client.request(url=host + url, method='GET')
    return response.text


# def test_send(client: requests.Session, host: str):
#     """
#     /api/v1/notifyservice/test_send_mq GET
#     """
#     url = "/api/v1/notifyservice/test_send_mq"
#     response = client.request(url=host + url, method='GET')
#     return response.json()


# def test_send_mail(client: requests.Session, host: str):
#     """
#     /api/v1/notifyservice/test_send_mail GET
#     """
#     url = "/api/v1/notifyservice/test_send_mail"
#     response = client.request(url=host + url, method='GET')
#     return response.json()


def preserve_success(client: requests.Session, info: NotifyInfo, host: str, headers: dict):
    """
    /api/v1/notifyservice/notification/preserve_success POST
    """
    url = "/api/v1/notifyservice/notification/preserve_success"
    response = client.request(url=host + url, method='POST', json=asdict(info), headers=headers)
    return response.json()


def order_create_success(client: requests.Session, info: NotifyInfo, host: str, headers: dict):
    """
    /api/v1/notifyservice/notification/order_create_success POST
    """
    url = "/api/v1/notifyservice/notification/order_create_success"
    response = client.request(url=host + url, method='POST', json=asdict(info), headers=headers)
    return response.json()


def order_changed_success(client: requests.Session, info: NotifyInfo, host: str, headers: dict):
    """
    /api/v1/notifyservice/notification/order_changed_success POST
    """
    url = "/api/v1/notifyservice/notification/order_changed_success"
    response = client.request(url=host + url, method='POST', json=asdict(info), headers=headers)
    return response.json()


def order_cancel_success(client: requests.Session, info: NotifyInfo, host: str, headers: dict):
    """
    /api/v1/notifyservice/notification/order_cancel_success POST
    """
    url = "/api/v1/notifyservice/notification/order_cancel_success"
    response = client.request(url=host + url, method='POST', json=asdict(info), headers=headers)
    return response.json()