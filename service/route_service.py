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


def route_welcome(client: requests.Session, host: str):
    """
    /api/v1/routeservice/welcome GET
    """
    url = "/api/v1/routeservice/welcome"
    response = client.request(url=host + url, method='GET')
    return response.text


def create_and_modify_route(client: requests.Session, route: RouteInfo, host: str, headers: dict):
    """
    /api/v1/routeservice/routes POST
    """
    url = "/api/v1/routeservice/routes"
    response = client.request(url=host + url, method='POST', json=asdict(route), headers=headers)
    return response.json()


def delete_route(client: requests.Session, route_id: str, host: str, headers: dict):
    """
    /api/v1/routeservice/routes/{routeId} DELETE
    """
    url = f"/api/v1/routeservice/routes/{route_id}"
    response = client.request(url=host + url, method='DELETE', headers=headers)
    return response.json()


def query_by_id(client: requests.Session, route_id: str, host: str, headers: dict):
    """
    /api/v1/routeservice/routes/{routeId} GET
    """
    url = f"/api/v1/routeservice/routes/{route_id}"
    response = client.request(url=host + url, method='GET', headers=headers)
    return from_dict(Route, response.json())


def query_by_ids(client: requests.Session, route_ids: List[str], host: str, headers: dict):
    """
    /api/v1/routeservice/routes/byIds POST
    """
    url = "/api/v1/routeservice/routes/byIds"
    response = client.request(url=host + url, method='POST', json=route_ids, headers=headers)
    return response.json()


def query_all(client: requests.Session, host: str, headers: dict):
    """
    /api/v1/routeservice/routes GET
    """
    url = "/api/v1/routeservice/routes"
    response = client.request(url=host + url, method='GET', headers=headers)
    return from_dict(Route, response.json())


def query_by_start_and_terminal(client: requests.Session, start: str, end: str, host: str, headers: dict):
    """
    /api/v1/routeservice/routes/{start}/{end} GET
    """
    url = f"/api/v1/routeservice/routes/{start}/{end}"
    response = client.request(url=host + url, method='GET', headers=headers)
    return from_dict(Route, response.json())