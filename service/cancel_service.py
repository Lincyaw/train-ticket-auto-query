import requests
from service.common import *


def welcome(client: requests.Session, host: str, headers: dict):
    """
    /api/v1/cancelservice/welcome GET
    """
    url = "/api/v1/cancelservice/welcome"
    response = client.request(url=host + url, method='GET', headers=headers)
    return response.text


def calculate_refund(client: requests.Session, order_id: str, host: str, headers: dict):
    """
    /api/v1/cancelservice/cancel/refound/{orderId} GET
    """
    url = f"/api/v1/cancelservice/cancel/refound/{order_id}"
    response = client.request(url=host + url, method='GET', headers=headers)
    return response.json()


def cancel_ticket(client: requests.Session, order_id: str, login_id: str, host: str, headers: dict):
    """
    /api/v1/cancelservice/cancel/{orderId}/{loginId} GET
    """
    url = f"/api/v1/cancelservice/cancel/{order_id}/{login_id}"
    response = client.request(url=host + url, method='GET', headers=headers)
    return response.json()
