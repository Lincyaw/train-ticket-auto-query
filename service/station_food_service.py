import requests
from dataclasses import dataclass, asdict
from service.common import *


@dataclass
class StationFoodStore(DataclassInstance):
    id: str
    stationName: str


def home(client: requests.Session, host: str):
    """
    /api/v1/stationfoodservice/stationfoodstores/welcome GET
    """
    url = "/api/v1/stationfoodservice/stationfoodstores/welcome"
    response = client.request(url=host + url, method='GET')
    return response.text


def list_food_stores(client: requests.Session, host: str, headers: dict):
    """
    /api/v1/stationfoodservice/stationfoodstores GET
    """
    url = "/api/v1/stationfoodservice/stationfoodstores"
    response = client.request(url=host + url, method='GET', headers=headers)
    return response.json()


def list_food_stores_by_station_name(client: requests.Session, station_name: str, host: str, headers: dict):
    """
    /api/v1/stationfoodservice/stationfoodstores/{stationId} GET
    """
    url = f"/api/v1/stationfoodservice/stationfoodstores/{station_name}"
    response = client.request(url=host + url, method='GET', headers=headers)
    return response.json()


def get_food_stores_by_station_names(client: requests.Session, station_names: list, host: str):
    """
    /api/v1/stationfoodservice/stationfoodstores POST
    """
    url = "/api/v1/stationfoodservice/stationfoodstores"
    response = client.request(url=host + url, method='POST', json=station_names)
    return response.json()


def get_food_list_by_store_id(client: requests.Session, store_id: str, host: str, headers: dict):
    """
    /api/v1/stationfoodservice/stationfoodstores/bystoreid/{stationFoodStoreId} GET
    """
    url = f"/api/v1/stationfoodservice/stationfoodstores/bystoreid/{store_id}"
    response = client.request(url=host + url, method='GET', headers=headers)
    return response.json()