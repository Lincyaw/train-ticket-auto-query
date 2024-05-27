import requests
from dataclasses import dataclass, asdict
from service.common import *


@dataclass
class RebookInfo(DataclassInstance):
    orderId: str
    oldTripId: str
    tripId: str
    date: str
    seatType: str


def home(client: requests.Session, host: str):
    """
    /api/v1/rebookservice/welcome GET
    """
    url = "/api/v1/rebookservice/welcome"
    response = client.request(url=host + url, method='GET')
    return response.text


def pay_difference(client: requests.Session, info: RebookInfo, host: str, headers: dict):
    """
    /api/v1/rebookservice/rebook/difference POST
    """
    url = "/api/v1/rebookservice/rebook/difference"
    response = client.request(url=host + url, method='POST', json=asdict(info), headers=headers)
    return response.json()


def rebook(client: requests.Session, info: RebookInfo, host: str, headers: dict):
    """
    /api/v1/rebookservice/rebook POST
    """
    url = "/api/v1/rebookservice/rebook"
    response = client.request(url=host + url, method='POST', json=asdict(info), headers=headers)
    return response.json()