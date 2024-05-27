import requests
from dataclasses import dataclass, asdict
from service.common import *
from uuid import UUID


@dataclass
class ExecuteServiceResult(DataclassInstance):
    message: str
    status: bool


def welcome(client: requests.Session, host: str, headers: dict):
    """
    /api/v1/executeservice/welcome GET
    """
    url = "/api/v1/executeservice/welcome"
    response = client.request(url=host + url, method='GET', headers=headers)
    return response.text


def execute_ticket(client: requests.Session, order_id: UUID, host: str, headers: dict):
    """
    /api/v1/executeservice/execute/execute/{orderId} GET
    """
    url = f"/api/v1/executeservice/execute/execute/{order_id}"
    response = client.request(url=host + url, method='GET', headers=headers)
    return from_dict(ExecuteServiceResult, response.json())


def collect_ticket(client: requests.Session, order_id: UUID, host: str, headers: dict):
    """
    /api/v1/executeservice/execute/collected/{orderId} GET
    """
    url = f"/api/v1/executeservice/execute/collected/{order_id}"
    response = client.request(url=host + url, method='GET', headers=headers)
    return from_dict(ExecuteServiceResult, response.json())