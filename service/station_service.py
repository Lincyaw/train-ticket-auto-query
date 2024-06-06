import requests
from dataclasses import dataclass, asdict
from service.common import *


@dataclass
class Station(DataclassInstance):
    id: str
    name: str
    stayTime: int


def home(client: requests.Session, host: str, headers: dict):
    """
    /api/v1/stationservice/welcome GET
    """
    url = "/api/v1/stationservice/welcome"
    response = client.request(url=host + url, method='GET', headers=headers)
    return response.text


def query_stations(client: requests.Session, host: str, headers: dict):
    """
    /api/v1/stationservice/stations GET
    """
    url = "/api/v1/stationservice/stations"
    response = client.request(url=host + url, method='GET', headers=headers)
    return response.json()


def create_station(client: requests.Session, station: Station, host: str, headers: dict):
    """
    /api/v1/stationservice/stations POST
    """
    url = "/api/v1/stationservice/stations"
    response = client.request(url=host + url, method='POST', json=asdict(station), headers=headers)
    return response.json()


def update_station(client: requests.Session, station: Station, host: str, headers: dict):
    """
    /api/v1/stationservice/stations PUT
    """
    url = "/api/v1/stationservice/stations"
    response = client.request(url=host + url, method='PUT', json=asdict(station), headers=headers)
    return response.json()


def delete_station(client: requests.Session, station_id: str, host: str, headers: dict):
    """
    /api/v1/stationservice/stations/{stationsId} DELETE
    """
    url = f"/api/v1/stationservice/stations/{station_id}"
    response = client.request(url=host + url, method='DELETE', headers=headers)
    return response.json()


def query_station_id(client: requests.Session, station_name: str, host: str, headers: dict):
    """
    /api/v1/stationservice/stations/id/{stationNameForId} GET
    """
    url = f"/api/v1/stationservice/stations/id/{station_name}"
    response = client.request(url=host + url, method='GET', headers=headers)
    return response.json()


def query_station_id_batch(client: requests.Session, station_names: list, host: str, headers: dict):
    """
    /api/v1/stationservice/stations/idlist POST
    """
    url = "/api/v1/stationservice/stations/idlist"
    response = client.request(url=host + url, method='POST', json=station_names, headers=headers)
    return response.json()


def query_station_name(client: requests.Session, station_id: str, host: str, headers: dict):
    """
    /api/v1/stationservice/stations/name/{stationIdForName} GET
    """
    url = f"/api/v1/stationservice/stations/name/{station_id}"
    response = client.request(url=host + url, method='GET', headers=headers)
    return response.json()


def query_station_name_batch(client: requests.Session, station_ids: list, host: str, headers: dict):
    """
    /api/v1/stationservice/stations/namelist POST
    """
    url = "/api/v1/stationservice/stations/namelist"
    response = client.request(url=host + url, method='POST', json=station_ids, headers=headers)
    return response.json()