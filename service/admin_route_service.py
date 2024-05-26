from typing import List
import requests
from service.common import *
from dataclasses import dataclass, asdict


@dataclass
class RouteInfo(DataclassInstance):
    id: str
    startStation: str
    endStation: str
    stationList: List[str]
    distanceList: List[float]


@dataclass
class Route(DataclassInstance):
    status: int
    msg: str
    data: List[RouteInfo]


def adminroute_welcome(client: requests.Session, host: str):
    """
    /api/v1/adminrouteservice/welcome GET
    """
    url = "/api/v1/adminrouteservice/welcome"
    response = client.request(url=host + url, method='GET')
    return response.text


def get_all_routes(client: requests.Session, host: str):
    """
    /api/v1/adminrouteservice/adminroute GET
    """
    url = "/api/v1/adminrouteservice/adminroute"
    response = client.request(url=host + url, method='GET')
    return from_dict(Route, response.json())


def delete_route(client: requests.Session, route_id: str, host: str):
    """
    /api/v1/adminrouteservice/adminroute/{routeId} DELETE
    """
    url = f"/api/v1/adminrouteservice/adminroute/{route_id}"
    response = client.request(url=host + url, method='DELETE')
    return response.json()


def create_and_modify_route(client: requests.Session, route: RouteInfo, host: str):
    """
    /api/v1/adminrouteservice/adminroute POST
    """
    url = "/api/v1/adminrouteservice/adminroute"
    response = client.request(url=host + url, method='POST', json=asdict(route))
    return response.json()
