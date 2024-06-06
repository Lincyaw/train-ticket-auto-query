import requests
from dataclasses import dataclass, asdict
from service.common import *
from uuid import UUID
from typing import List


@dataclass
class Delivery(DataclassInstance):
    foodName: str
    orderId: UUID
    stationName: str
    storeName: str


@dataclass
class FoodOrder(DataclassInstance):
    id: str
    orderId: str
    foodType: int
    stationName: str
    storeName: str
    foodName: str
    price: float

@dataclass
class QueryAllMessage(DataclassInstance):
    status: int
    msg: str
    data: List

@dataclass
class FoodOrderReturn(DataclassInstance):
    status: int
    msg: str
    data: List

def home(client: requests.Session, host: str):
    """
    /api/v1/foodservice/welcome GET
    """
    url = "/api/v1/foodservice/welcome"
    response = client.request(url=host + url, method='GET')
    return response.text


# def test_send_delivery(client: requests.Session, host: str):
#     """
#     /api/v1/foodservice/test_send_delivery GET
#     """
#     url = "/api/v1/foodservice/test_send_delivery"
#     response = client.request(url=host + url, method='GET', json=())
#     return response.json()


def find_all_food_order(client: requests.Session, host: str, headers: dict):
    """
    /api/v1/foodservice/orders GET
    """
    url = "/api/v1/foodservice/orders"
    response = client.request(url=host + url, method='GET', headers=headers)
    return from_dict(QueryAllMessage, response.json())


def create_food_order(client: requests.Session, food_order: FoodOrder, host: str, headers: dict):
    """
    /api/v1/foodservice/orders POST
    """
    url = "/api/v1/foodservice/orders"
    response = client.request(url=host + url, method='POST', json=asdict(food_order), headers=headers)
    return response.json()


def create_food_batches(client: requests.Session, food_order_list: List[FoodOrder], host: str, headers: dict):
    """
    /api/v1/foodservice/createOrderBatch POST
    """
    url = "/api/v1/foodservice/createOrderBatch"
    response = client.request(url=host + url, method='POST', json=[asdict(food_order) for food_order in food_order_list], headers=headers)
    return response.json()


def update_food_order(client: requests.Session, food_order: FoodOrder, host: str, headers: dict):
    """
    /api/v1/foodservice/orders PUT
    """
    url = "/api/v1/foodservice/orders"
    response = client.request(url=host + url, method='PUT', json=asdict(food_order), headers=headers)
    return response.json()


def delete_food_order(client: requests.Session, order_id: UUID, host: str, headers: dict):
    """
    /api/v1/foodservice/orders/{orderId} DELETE
    """
    url = f"/api/v1/foodservice/orders/{order_id}"
    response = client.request(url=host + url, method='DELETE', headers=headers)
    return response.json()


def find_food_order_by_order_id(client: requests.Session, orderId: str, host: str, headers: dict):
    """
    /api/v1/foodservice/orders/{orderId} GET
    """
    url = f"/api/v1/foodservice/orders/{orderId}"
    response = client.request(url=host + url, method='GET', headers=headers)
    return response.json()


def get_all_food(client: requests.Session, date: str, start_station: str, end_station: str, trip_id: str, host: str, headers: dict):
    """
    /api/v1/foodservice/foods/{date}/{startStation}/{endStation}/{tripId} GET
    """
    url = f"/api/v1/foodservice/foods/{date}/{start_station}/{end_station}/{trip_id}"
    response = client.request(url=host + url, method='GET', headers=headers)
    return response.json()