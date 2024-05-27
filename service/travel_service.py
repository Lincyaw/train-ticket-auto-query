import requests
from dataclasses import dataclass, asdict
from service.common import *
from typing import List


@dataclass
class TravelInfo:
    trip_id: str


@dataclass
class TripInfo:
    start_place: str
    end_place: str
    departure_time: str


@dataclass
class TripAllDetailInfo:
    trip_id: str


@dataclass
class TrainType(DataclassInstance):
    id: str
    name: str
    economyClass: int
    confortClass: int


@dataclass
class Route(DataclassInstance):
    id: str
    stations: List[str]
    distances: List[int]
    startStation: str
    terminalStation: str


@dataclass
class Trip(DataclassInstance):
    id: str
    tripId: str
    trainTypeId: str
    routeId: str
    startingStationId: str
    stationsId: str
    terminalStationId: str
    startingTime: str
    endTime: str


@dataclass
class TripResponse(DataclassInstance):
    tripId: str
    trainTypeId: str
    startStation: str
    terminalStation: str
    startTime: str
    endTime: str
    economyClass: int
    confortClass: int


@dataclass
class AdminTrip(DataclassInstance):
    id: str
    trainType: str
    routeId: str
    startStationId: str
    stationsId: str
    terminalStationId: str
    startTime: str
    endTime: str


def welcome(client: requests.Session, host: str, headers: dict):
    """
    /api/v1/travelservice/welcome GET
    """
    url = "/api/v1/travelservice/welcome"
    response = client.request(url=host + url, method="GET", headers=headers)
    return response.text


def get_train_type_by_trip_id(client: requests.Session, trip_id: str, host: str, headers: dict):
    """
    /api/v1/travelservice/train_types/{tripId} GET
    """
    url = f"/api/v1/travelservice/train_types/{trip_id}"
    response = client.request(url=host + url, method="GET", headers=headers)
    return from_dict(TrainType, response.json())


def get_route_by_trip_id(client: requests.Session, trip_id: str, host: str, headers: dict):
    """
    /api/v1/travelservice/routes/{tripId} GET
    """
    url = f"/api/v1/travelservice/routes/{trip_id}"
    response = client.request(url=host + url, method="GET", headers=headers)
    return from_dict(Route, response.json())


def get_trips_by_route_id(client: requests.Session, route_ids: List[str], host: str, headers: dict):
    """
    /api/v1/travelservice/trips/routes POST
    """
    url = "/api/v1/travelservice/trips/routes"
    response = client.request(url=host + url, method="POST", headers=headers, json=route_ids)
    return [from_dict(Trip, t) for t in response.json()]


def create_trip(client: requests.Session, route_ids: TravelInfo, host: str, headers: dict):
    """
    /api/v1/travelservice/trips POST
    """
    url = "/api/v1/travelservice/trips"
    response = client.request(url=host + url, method="POST", headers=headers, json=asdict(route_ids))
    return response.text


def retrieve_trip(client: requests.Session, trip_id: str, host: str, headers: dict):
    """
    /api/v1/travelservice/trips/{tripId} GET
    """
    url = f"/api/v1/travelservice/trips/{trip_id}"
    response = client.request(url=host + url, method="GET", headers=headers)
    return from_dict(Trip, response.json())


def update_trip(client: requests.Session, info: TravelInfo, host: str, headers: dict):
    """
    /api/v1/travelservice/trips PUT
    """
    url = "/api/v1/travelservice/trips"
    response = client.request(url=host + url, method="PUT", headers=headers, json=asdict(info))
    return from_dict(Trip, response.json())


def delete_trip(client: requests.Session, trip_id: str, host: str, headers: dict):
    """
    /api/v1/travelservice/trips/{tripId} DELETE
    """
    url = f"/api/v1/travelservice/trips/{trip_id}"
    response = client.request(url=host + url, method="DELETE", headers=headers)
    return response.text


def query_trips(client: requests.Session, info: TripInfo, host: str, headers: dict):
    """
    /api/v1/travelservice/trips/left POST
    """
    url = "/api/v1/travelservice/trips/left"
    response = client.request(url=host + url, method="POST", headers=headers, json=asdict(info))
    return [from_dict(TripResponse, tr) for tr in response.json()]


def query_trips_in_parallel(client: requests.Session, info: TripInfo, host: str, headers: dict):
    """
    /api/v1/travelservice/trips/left_parallel POST
    """
    url = "/api/v1/travelservice/trips/left_parallel"
    response = client.request(url=host + url, method="POST", headers=headers, json=asdict(info))
    return [from_dict(TripResponse, tr) for tr in response.json()]


def get_trip_all_detail_info(client: requests.Session, gtdi: TripAllDetailInfo, host: str, headers: dict):
    """
    /api/v1/travelservice/trip_detail POST
    """
    url = "/api/v1/travelservice/trip_detail"
    response = client.request(url=host + url, method="POST", headers=headers, json=asdict(gtdi))
    return response.json()


def query_all_trips(client: requests.Session, host: str, headers: dict):
    """
    /api/v1/travelservice/trips GET
    """
    url = "/api/v1/travelservice/trips"
    response = client.request(url=host + url, method="GET", headers=headers)
    return [from_dict(Trip, t) for t in response.json()]


def admin_query_all_trips(client: requests.Session, host: str, headers: dict):
    """
    /api/v1/travelservice/admin_trip GET
    """
    url = "/api/v1/travelservice/admin_trip"
    response = client.request(url=host + url, method="GET", headers=headers)
    return [from_dict(AdminTrip, t) for t in response.json()]
