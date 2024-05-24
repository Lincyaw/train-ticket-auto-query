from typing import List
import requests
from service.common import *
from dataclasses import dataclass, asdict
@dataclass
class ContactBody(DataclassInstance):
    id: str
    accountId: str
    name: str
    documentType: int
    documentNumber: str
    phoneNumber: str

@dataclass
class Contact(DataclassInstance):
    status: int
    msg: str
    data: List


@dataclass
class StationBody(DataclassInstance):
    id: str
    name: str
    stayTime: int


@dataclass
class Station(DataclassInstance):
    status: int
    msg: str
    data: List


@dataclass
class TrainTypeBody(DataclassInstance):
    id: str
    name: str
    economyClass: int
    confortClass: int
    averageSpeed: int

@dataclass
class TrainType(DataclassInstance):
    status: int
    msg: str
    data: List


@dataclass
class ConfigBody(DataclassInstance):
    name: str
    value: str
    description: str

@dataclass
class Config(DataclassInstance):
    status: int
    msg: str
    data: List


@dataclass
class PriceInfoBody(DataclassInstance):
    id: str
    trainType: str
    routeId: str
    basicPriceRate: float
    firstClassPriceRate: float

@dataclass
class PriceInfo(DataclassInstance):
    status: int
    msg: str
    data: List


def adminbasic_welcome(client: requests.Session, host: str):
    """
    /api/v1/adminbasicservice/welcome GET
    """
    url = "/api/v1/adminbasicservice/welcome"
    response = client.request(url=host + url, method='GET')
    return response.text


def get_all_contacts(client: requests.Session, host: str):
    """
    /api/v1/adminbasicservice/adminbasic/contacts GET
    """
    url = "/api/v1/adminbasicservice/adminbasic/contacts"
    response = client.request(url=host + url, method='GET')
    return from_dict(Contact, response.json())


def delete_contact(client: requests.Session, contact_id: str, host: str):
    """
    /api/v1/adminbasicservice/adminbasic/contacts/{contactsId} DELETE
    """
    url = f"/api/v1/adminbasicservice/adminbasic/contacts/{contact_id}"
    response = client.request(url=host + url, method='DELETE')
    return response.json()


def modify_contact(client: requests.Session, contact: ContactBody, host: str):
    """
    /api/v1/adminbasicservice/adminbasic/contacts PUT
    """
    url = "/api/v1/adminbasicservice/adminbasic/contacts"
    response = client.request(url=host + url, method='PUT', json=asdict(contact))
    return response.json()


def add_contact(client: requests.Session, contact: ContactBody, host: str):
    """
    /api/v1/adminbasicservice/adminbasic/contacts POST
    """
    url = "/api/v1/adminbasicservice/adminbasic/contacts"
    response = client.request(url=host + url, method='POST', json=asdict(contact))
    return from_dict(Contact, response.json())


def get_all_stations(client: requests.Session, host: str):
    """
    /api/v1/adminbasicservice/adminbasic/stations GET
    """
    url = "/api/v1/adminbasicservice/adminbasic/stations"
    response = client.request(url=host + url, method='GET')
    return from_dict(Station, response.json())


def delete_station(client: requests.Session, station_id: str, host: str):
    """
    /api/v1/adminbasicservice/adminbasic/stations/{id} DELETE
    """
    url = f"/api/v1/adminbasicservice/adminbasic/stations/{station_id}"
    response = client.request(url=host + url, method='DELETE')
    return response.json()


def modify_station(client: requests.Session, station: StationBody, host: str):
    """
    /api/v1/adminbasicservice/adminbasic/stations PUT
    """
    url = "/api/v1/adminbasicservice/adminbasic/stations"
    response = client.request(url=host + url, method='PUT', json=asdict(station))
    return response.json()


def add_station(client: requests.Session, station: Station, host: str):
    """
    /api/v1/adminbasicservice/adminbasic/stations POST
    """
    url = "/api/v1/adminbasicservice/adminbasic/stations"
    response = client.request(url=host + url, method='POST', json=asdict(station))
    return response.json()


def get_all_trains(client: requests.Session, host: str):
    """
    /api/v1/adminbasicservice/adminbasic/trains GET
    """
    url = "/api/v1/adminbasicservice/adminbasic/trains"
    response = client.request(url=host + url, method='GET')
    return from_dict(TrainType, response.json())


def delete_train(client: requests.Session, train_id: str, host: str):
    """
    /api/v1/adminbasicservice/adminbasic/trains/{id} DELETE
    """
    url = f"/api/v1/adminbasicservice/adminbasic/trains/{train_id}"
    response = client.request(url=host + url, method='DELETE')
    return response.json()


def modify_train(client: requests.Session, train_type: TrainType, host: str):
    """
    /api/v1/adminbasicservice/adminbasic/trains PUT
    """
    url = "/api/v1/adminbasicservice/adminbasic/trains"
    response = client.request(url=host + url, method='PUT', json=asdict(train_type))
    return response.json()


def add_train(client: requests.Session, train_type: TrainType, host: str):
    """
    /api/v1/adminbasicservice/adminbasic/trains POST
    """
    url = "/api/v1/adminbasicservice/adminbasic/trains"
    response = client.request(url=host + url, method='POST', json=asdict(train_type))
    return response.json()


def get_all_configs(client: requests.Session, host: str):
    """
    /api/v1/adminbasicservice/adminbasic/configs GET
    """
    url = "/api/v1/adminbasicservice/adminbasic/configs"
    response = client.request(url=host + url, method='GET')
    return from_dict(Config, response.json())


def delete_config(client: requests.Session, config_name: str, host: str):
    """
    /api/v1/adminbasicservice/adminbasic/configs/{name} DELETE
    """
    url = f"/api/v1/adminbasicservice/adminbasic/configs/{config_name}"
    response = client.request(url=host + url, method='DELETE')
    return response.json()


def modify_config(client: requests.Session, config: Config, host: str):
    """
    /api/v1/adminbasicservice/adminbasic/configs PUT
    """
    url = "/api/v1/adminbasicservice/adminbasic/configs"
    response = client.request(url=host + url, method='PUT', json=asdict(config))
    return response.json()


def add_config(client: requests.Session, config: Config, host: str):
    """
    /api/v1/adminbasicservice/adminbasic/configs POST
    """
    url = "/api/v1/adminbasicservice/adminbasic/configs"
    response = client.request(url=host + url, method='POST', json=asdict(config))
    return response.json()


def get_all_prices(client: requests.Session, host: str):
    """
    /api/v1/adminbasicservice/adminbasic/prices GET
    """
    url = "/api/v1/adminbasicservice/adminbasic/prices"
    response = client.request(url=host + url, method='GET')
    return from_dict(PriceInfo, response.json())


def delete_price(client: requests.Session, price_id: str, host: str):
    """
    /api/v1/adminbasicservice/adminbasic/prices
    """
    url = f"/api/v1/adminbasicservice/adminbasic/prices/{price_id}"
    response = client.request(url=host + url, method='DELETE')
    return response.json()

def modify_price(client: requests.Session, price_info: PriceInfo, host: str):
    """
    /api/v1/adminbasicservice/adminbasic/prices PUT
    """
    url = "/api/v1/adminbasicservice/adminbasic/prices"
    response = client.request(url=host + url, method='PUT', json=asdict(price_info))
    return response.json()

def add_price(client: requests.Session, price_info: PriceInfo, host: str):
    """
    /api/v1/adminbasicservice/adminbasic/prices POST
    """
    url = "/api/v1/adminbasicservice/adminbasic/prices"
    response = client.request(url=host + url, method='POST', json=asdict(price_info))
    return response.json()