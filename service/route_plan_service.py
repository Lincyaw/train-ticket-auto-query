from typing import List
import requests
from service.common import *
from dataclasses import dataclass, asdict
from datetime import datetime


@dataclass
class RoutePlanInfo(DataclassInstance):
    startStation: str
    endStation: str
    travelDate: datetime
    num: int


@dataclass
class RoutePlan(DataclassInstance):
    status: int
    msg: str
    data: List[dict]


def routeplan_welcome(client: requests.Session, host: str):
    """
    /api/v1/routeplanservice/welcome GET
    """
    url = "/api/v1/routeplanservice/welcome"
    response = client.request(url=host + url, method='GET')
    return response.text


def get_cheapest_routes(client: requests.Session, info: RoutePlanInfo, host: str, headers: dict):
    """
    /api/v1/routeplanservice/routePlan/cheapestRoute POST
    """
    url = "/api/v1/routeplanservice/routePlan/cheapestRoute"
    response = client.request(url=host + url, method='POST', json=asdict(info), headers=headers)
    return response.json()


def get_quickest_routes(client: requests.Session, info: RoutePlanInfo, host: str, headers: dict):
    """
    /api/v1/routeplanservice/routePlan/quickestRoute POST
    """
    url = "/api/v1/routeplanservice/routePlan/quickestRoute"
    response = client.request(url=host + url, method='POST', json=asdict(info), headers=headers)
    return response.json()


def get_min_stop_stations(client: requests.Session, info: RoutePlanInfo, host: str, headers: dict):
    """
    /api/v1/routeplanservice/routePlan/minStopStations POST
    """
    url = "/api/v1/routeplanservice/routePlan/minStopStations"
    response = client.request(url=host + url, method='POST', json=asdict(info), headers=headers)
    return response.json()