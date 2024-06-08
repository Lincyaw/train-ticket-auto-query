import requests
from dataclasses import dataclass, asdict
from service.common import *


@dataclass
class OrderTicketsInfo(DataclassInstance):
    from_: str
    to: str
    date: str


def home(client: requests.Session, host: str):
    """
    /api/v1/preserveservice/welcome GET
    """
    url = "/api/v1/preserveservice/welcome"
    response = client.request(url=host + url, method='GET')
    return response.text


def preserve(client: requests.Session, oti: OrderTicketsInfo, host: str, headers: dict):
    """
    /api/v1/preserveservice/preserve POST
    """
    url = "/api/v1/preserveservice/preserve"
    response = client.request(url=host + url, method='POST', json=asdict(oti), headers=headers)
    return response.json()