import requests
from dataclasses import dataclass, asdict
from typing import List
from service.common import *


@dataclass
class PriceConfig(DataclassInstance):
    id: str
    routeId: str
    trainType: str


def home(client: requests.Session, host: str):
    """
    /api/v1/priceservice/prices/welcome GET
    """
    url = "/api/v1/priceservice/prices/welcome"
    response = client.request(url=host + url, method='GET')
    return response.text


def find_by_route_id_and_train_type(client: requests.Session, route_id: str, train_type: str, host: str, headers: dict):
    """
    /api/v1/priceservice/prices/{routeId}/{trainType} GET
    """
    url = f"/api/v1/priceservice/prices/{route_id}/{train_type}"
    response = client.request(url=host + url, method='GET', headers=headers)
    return response.json()


def find_by_route_ids_and_train_types(client: requests.Session, rids_and_tts: List[str], host: str, headers: dict):
    """
    /api/v1/priceservice/prices/byRouteIdsAndTrainTypes POST
    """
    url = "/api/v1/priceservice/prices/byRouteIdsAndTrainTypes"
    response = client.request(url=host + url, method='POST', json=rids_and_tts, headers=headers)
    return response.json()


def find_all_price_config(client: requests.Session, host: str, headers: dict):
    """
    /api/v1/priceservice/prices GET
    """
    url = "/api/v1/priceservice/prices"
    response = client.request(url=host + url, method='GET', headers=headers)
    return response.json()


def create_new_price_config(client: requests.Session, info: PriceConfig, host: str, headers: dict):
    """
    /api/v1/priceservice/prices POST
    """
    url = "/api/v1/priceservice/prices"
    response = client.request(url=host + url, method='POST', json=asdict(info), headers=headers)
    return response.json()


def delete_price_config(client: requests.Session, prices_id: str, host: str, headers: dict):
    """
    /api/v1/priceservice/prices/{pricesId} DELETE
    """
    url = f"/api/v1/priceservice/prices/{prices_id}"
    response = client.request(url=host + url, method='DELETE', headers=headers)
    return response.json()


def update_price_config(client: requests.Session, info: PriceConfig, host: str, headers: dict):
    """
    /api/v1/priceservice/prices PUT
    """
    url = "/api/v1/priceservice/prices"
    response = client.request(url=host + url, method='PUT', json=asdict(info), headers=headers)
    return response.json()