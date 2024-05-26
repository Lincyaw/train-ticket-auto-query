import requests
from service.common import *
from dataclasses import dataclass, asdict


@dataclass
class ConsignPrice(DataclassInstance):
    index: int
    initialWeight: float
    initialPrice: float
    withinPrice: float
    beyondPrice: float


def welcome(client: requests.Session, host: str, headers: dict):
    """
    /api/v1/consignpriceservice/welcome GET
    """
    url = "/api/v1/consignpriceservice/welcome"
    response = client.request(url=host + url, method='GET', headers=headers)
    return response.text


def get_price_by_weight_and_region(client: requests.Session, weight: float, is_within_region: bool, host: str, headers: dict):
    """
    /api/v1/consignpriceservice/consignprice/{weight}/{isWithinRegion} GET
    """
    url = f"/api/v1/consignpriceservice/consignprice/{weight}/{is_within_region}"
    response = client.request(url=host + url, method='GET', headers=headers)
    return from_dict(ConsignPrice, response.json())


def get_price_info(client: requests.Session, host: str, headers: dict):
    """
    /api/v1/consignpriceservice/consignprice/price GET
    """
    url = "/api/v1/consignpriceservice/consignprice/price"
    response = client.request(url=host + url, method='GET', headers=headers)
    return from_dict(ConsignPrice, response.json())


def get_price_config(client: requests.Session, host: str, headers: dict):
    """
    /api/v1/consignpriceservice/consignprice/config GET
    """
    url = "/api/v1/consignpriceservice/consignprice/config"
    response = client.request(url=host + url, method='GET', headers=headers)
    return from_dict(ConsignPrice, response.json())


def modify_price_config(client: requests.Session, price_config: ConsignPrice, host: str, headers: dict):
    """
    /api/v1/consignpriceservice/consignprice POST
    """
    url = "/api/v1/consignpriceservice/consignprice"
    response = client.request(url=host + url, method='POST', json=asdict(price_config), headers=headers)
    return response.json()