from typing import List
import requests
from dataclasses import dataclass, asdict
from service.common import *
from uuid import UUID

@dataclass
class Food(DataclassInstance):
    foodName: str
    price: float

@dataclass
class FoodDeliveryOrder(DataclassInstance):
    id: str
    stationFoodStoreId: str
    foodList: List[Food]
    tripId: str
    seatNo: int
    createdTime: str
    deliveryTime: str
    deliveryFee: float


@dataclass
class TripOrderInfo(DataclassInstance):
    pass


@dataclass
class SeatInfo(DataclassInstance):
    pass


@dataclass
class DeliveryInfo(DataclassInstance):
    pass


def home(client: requests.Session, host: str):
    """
    /api/v1/fooddeliveryservice/welcome GET
    """
    url = "/api/v1/fooddeliveryservice/welcome"
    response = client.request(url=host + url, method='GET')
    return response.text


def create_food_delivery_order(client: requests.Session, fd: FoodDeliveryOrder, host: str, headers: dict):
    """
    /api/v1/fooddeliveryservice/orders POST
    """
    url = "/api/v1/fooddeliveryservice/orders"
    response = client.request(url=host + url, method='POST', json=asdict(fd), headers=headers)
    return response.json()


def delete_food_delivery_order(client: requests.Session, order_id: UUID, host: str, headers: dict):
    """
    /api/v1/fooddeliveryservice/orders/d/{orderId} DELETE
    """
    url = f"/api/v1/fooddeliveryservice/orders/d/{order_id}"
    response = client.request(url=host + url, method='DELETE', headers=headers)
    return response.json()


def get_food_delivery_order_by_id(client: requests.Session, order_id: UUID, host: str, headers: dict):
    """
    /api/v1/fooddeliveryservice/orders/{orderId} GET
    """
    url = f"/api/v1/fooddeliveryservice/orders/{order_id}"
    response = client.request(url=host + url, method='GET', headers=headers)
    return from_dict(FoodDeliveryOrder, response.json())


def get_all_food_delivery_orders(client: requests.Session, host: str, headers: dict):
    """
    /api/v1/fooddeliveryservice/orders/all GET
    """
    url = "/api/v1/fooddeliveryservice/orders/all"
    response = client.request(url=host + url, method='GET', headers=headers)
    return response.json()


def get_food_delivery_order_by_store_id(client: requests.Session, store_id: UUID, host: str, headers: dict):
    """
    /api/v1/fooddeliveryservice/orders/store/{storeId} GET
    """
    url = f"/api/v1/fooddeliveryservice/orders/store/{store_id}"
    response = client.request(url=host + url, method='GET', headers=headers)
    return response.json()


def update_trip_id(client: requests.Session, trip_order_info: TripOrderInfo, host: str, headers: dict):
    """
    /api/v1/fooddeliveryservice/orders/tripid PUT
    """
    url = "/api/v1/fooddeliveryservice/orders/tripid"
    response = client.request(url=host + url, method='PUT', json=asdict(trip_order_info), headers=headers)
    return from_dict(TripOrderInfo, response.json())


def update_seat_no(client: requests.Session, seat_info: SeatInfo, host: str, headers: dict):
    """
    /api/v1/fooddeliveryservice/orders/seatno PUT
    """
    url = "/api/v1/fooddeliveryservice/orders/seatno"
    response = client.request(url=host + url, method='PUT', json=asdict(seat_info), headers=headers)
    return from_dict(SeatInfo, response.json())


def update_delivery_time(client: requests.Session, delivery_info: DeliveryInfo, host: str, headers: dict):
    """
    /api/v1/fooddeliveryservice/orders/dtime PUT
    """
    url = "/api/v1/fooddeliveryservice/orders/dtime"
    response = client.request(url=host + url, method='PUT', json=asdict(delivery_info), headers=headers)
    return from_dict(DeliveryInfo, response.json())