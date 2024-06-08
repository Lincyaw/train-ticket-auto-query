import requests
from typing import List
from dataclasses import dataclass, asdict
from service.common import *

@dataclass
class ReturnBody(DataclassInstance):
    status: int
    msg: str
    data: List

@dataclass
class TripInfo(DataclassInstance):
    startPlace: str
    endPlace: str
    departureTime: str


@dataclass
class TripAllDetailInfo(DataclassInstance):
    tripId: str
    travelDate: str
    from_location: str
    to: str


@dataclass
class TravelInfo(DataclassInstance):
    loginId: str
    tripId: str
    trainTypeName: str
    routeId: str
    startStationName: str
    stationsName: str
    terminalStationName: str
    startTime: str
    endTime: str


def home(client: requests.Session, host: str, headers: dict):
    """
    /api/v1/travel2service/welcome GET
    """
    url = "/api/v1/travel2service/welcome"
    response = client.request(url=host + url, method='GET', headers=headers)
    return response.text


def get_train_type_by_trip_id(client: requests.Session, trip_id: str, host: str, headers: dict):
    """
    /api/v1/travel2service/train_types/{tripId} GET
    """
    url = f"/api/v1/travel2service/train_types/{trip_id}"
    response = client.request(url=host + url, method='GET', headers=headers)
    return response.json()


def get_route_by_trip_id(client: requests.Session, trip_id: str, host: str, headers: dict):
    """
    /api/v1/travel2service/routes/{tripId} GET
    """
    url = f"/api/v1/travel2service/routes/{trip_id}"
    response = client.request(url=host + url, method='GET', headers=headers)
    return response.json()


def get_trips_by_route_id(client: requests.Session, route_ids: List[str], host: str, headers: dict):
    """
    /api/v1/travel2service/trips/routes POST
    """
    url = "/api/v1/travel2service/trips/routes"
    response = client.request(url=host + url, method='POST', json=route_ids, headers=headers)
    return response.json()


def create_trip(client: requests.Session, travel_info: TravelInfo, host: str, headers: dict):
    """
    /api/v1/travel2service/trips POST
    """
    url = "/api/v1/travel2service/trips"
    response = client.request(url=host + url, method='POST', json=asdict(travel_info), headers=headers)
    return response.json()


def retrieve_trip(client: requests.Session, trip_id: str, host: str, headers: dict):
    """
    /api/v1/travel2service/trips/{tripId} GET
    """
    url = f"/api/v1/travel2service/trips/{trip_id}"
    response = client.request(url=host + url, method='GET', headers=headers)
    return from_dict(ReturnBody, response.json())


def update_trip(client: requests.Session, travel_info: TravelInfo, host: str, headers: dict):
    """
    /api/v1/travel2service/trips PUT
    """
    url = "/api/v1/travel2service/trips"
    response = client.request(url=host + url, method='PUT', json=asdict(travel_info), headers=headers)
    return response.json()


def delete_trip(client: requests.Session, trip_id: str, host: str, headers: dict):
    """
    /api/v1/travel2service/trips/{tripId} DELETE
    """
    url = f"/api/v1/travel2service/trips/{trip_id}"
    response = client.request(url=host + url, method='DELETE', headers=headers)
    return response.json()


def query_trip_info(client: requests.Session, trip_info: TripInfo, host: str, headers: dict):
    """
    /api/v1/travel2service/trips/left POST
    """
    url = "/api/v1/travel2service/trips/left"
    response = client.request(url=host + url, method='POST', json=asdict(trip_info), headers=headers)
    return response.json()


def get_trip_all_detail_info(client: requests.Session, gtdi: TripAllDetailInfo, host: str, headers: dict):
    """
    /api/v1/travel2service/trip_detail POST
    """
    url = "/api/v1/travel2service/trip_detail"
    response = client.request(url=host + url, method='POST', json=asdict(gtdi), headers=headers)
    return response.json()


def query_all_trips(client: requests.Session, host: str, headers: dict):
    """
    /api/v1/travel2service/trips GET
    """
    url = "/api/v1/travel2service/trips"
    response = client.request(url=host + url, method='GET', headers=headers)
    return from_dict(ReturnBody, response.json())


def admin_query_all_trips(client: requests.Session, host: str, headers: dict):
    """
    /api/v1/travel2service/admin_trip GET
    """
    url = "/api/v1/travel2service/admin_trip"
    response = client.request(url=host + url, method='GET', headers=headers)
    return from_dict(ReturnBody, response.json())