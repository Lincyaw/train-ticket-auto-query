from typing import List
import requests
from service.common import *
from dataclasses import dataclass, field


@dataclass
class Travel(DataclassInstance):
    tripId: str
    trainTypeId: str
    startStationName: str
    startTime: str
    endStationName: str
    arriveTime: str

    @staticmethod
    def from_dict(obj: Any) -> 'Travel':
        return Travel(
            tripId=str(obj.get("tripId")),
            trainTypeId=str(obj.get("trainTypeId")),
            startStationName=str(obj.get("startStationName")),
            startTime=str(obj.get("startTime")),
            endStationName=str(obj.get("endStationName")),
            arriveTime=str(obj.get("arriveTime"))
        )


@dataclass
class TravelResult(DataclassInstance):
    status: int
    msg: str
    data: List[Travel] = field(default_factory=list)


def welcome(client: requests.Session, host: str, headers: dict):
    """
    /api/v1/basicservice/welcome GET
    """
    url = "/api/v1/basicservice/welcome"
    response = client.request(url=host + url, method='GET', headers=headers)
    return response.text


def query_for_travel(client: requests.Session, travel: Travel, host: str, headers: dict):
    """
    /api/v1/basicservice/basic/travel POST
    """
    url = "/api/v1/basicservice/basic/travel"
    response = client.request(url=host + url, method='POST', json=dataclass.asdict(travel), headers=headers)
    return from_dict(TravelResult, response.json())


def query_for_travels(client: requests.Session, travels: List[Travel], host: str, headers: dict):
    """
    /api/v1/basicservice/basic/travels POST
    """
    url = "/api/v1/basicservice/basic/travels"
    response = client.request(url=host + url, method='POST', json=[dataclass.asdict(travel) for travel in travels],
                              headers=headers)
    return from_dict(TravelResult, response.json())


def query_for_station_id(client: requests.Session, station_name: str, host: str, headers: dict):
    """
    /api/v1/basicservice/basic/{stationName} GET
    """
    url = f"/api/v1/basicservice/basic/{station_name}"
    response = client.request(url=host + url, method='GET', headers=headers)
    return from_dict(Travel, response.json())
