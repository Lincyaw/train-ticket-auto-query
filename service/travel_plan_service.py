import requests
from dataclasses import dataclass, asdict
from service.common import *


@dataclass
class TransferTravelInfo:
    start_station: str
    end_station: str


@dataclass
class TripInfo:
    start_place: str
    end_place: str
    departure_time: str


@dataclass
class TravelPlanResult(DataclassInstance):
    message: str
    status: bool
    data: dict


def welcome(client: requests.Session, host: str, headers: dict):
    """
    /api/v1/travelplanservice/welcome GET
    """
    url = "/api/v1/travelplanservice/welcome"
    response = client.request(url=host + url, method='GET', headers=headers)
    return response.text


def get_transfer_result(client: requests.Session, info: TransferTravelInfo, host: str, headers: dict):
    """
    /api/v1/travelplanservice/travelPlan/transferResult POST
    """
    url = "/api/v1/travelplanservice/travelPlan/transferResult"
    response = client.request(url=host + url, method='POST', headers=headers, json=asdict(info))
    return from_dict(TravelPlanResult, response.json())


def get_by_cheapest(client: requests.Session, query_info: TripInfo, host: str, headers: dict):
    """
    /api/v1/travelplanservice/travelPlan/cheapest POST
    """
    url = "/api/v1/travelplanservice/travelPlan/cheapest"
    response = client.request(url=host + url, method='POST', headers=headers, json=asdict(query_info))
    return from_dict(TravelPlanResult, response.json())


def get_by_quickest(client: requests.Session, query_info: TripInfo, host: str, headers: dict):
    """
    /api/v1/travelplanservice/travelPlan/quickest POST
    """
    url = "/api/v1/travelplanservice/travelPlan/quickest"
    response = client.request(url=host + url, method='POST', headers=headers, json=asdict(query_info))
    return from_dict(TravelPlanResult, response.json())


def get_by_min_station(client: requests.Session, query_info: TripInfo, host: str, headers: dict):
    """
    /api/v1/travelplanservice/travelPlan/minStation POST
    """
    url = "/api/v1/travelplanservice/travelPlan/minStation"
    response = client.request(url=host + url, method='POST', headers=headers, json=asdict(query_info))
    return from_dict(TravelPlanResult, response.json())
