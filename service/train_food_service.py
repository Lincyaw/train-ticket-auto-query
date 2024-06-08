import requests
from dataclasses import dataclass
from service.common import *
from typing import  List


@dataclass
class TrainFood(DataclassInstance):
    id: str
    tripId: str
    foodList: List


def home(client: requests.Session, host: str):
    """
    /api/v1/trainfoodservice/trainfoods/welcome GET
    """
    url = "/api/v1/trainfoodservice/trainfoods/welcome"
    response = client.request(url=host + url, method='GET')
    return response.text


def list_train_food(client: requests.Session, host: str, headers: dict):
    """
    /api/v1/trainfoodservice/trainfoods GET
    """
    url = "/api/v1/trainfoodservice/trainfoods"
    response = client.request(url=host + url, method='GET', headers=headers)
    return response.json()


def list_train_food_by_trip_id(client: requests.Session, trip_id: str, host: str, headers: dict):
    """
    /api/v1/trainfoodservice/trainfoods/{tripId} GET
    """
    url = f"/api/v1/trainfoodservice/trainfoods/{trip_id}"
    response = client.request(url=host + url, method='GET', headers=headers)
    return response.json()