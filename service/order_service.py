import requests
from dataclasses import dataclass, asdict
from service.common import *


@dataclass
class Order(DataclassInstance):
    id: str
    from_: str
    to: str
    travelDate: str


@dataclass
class OrderInfo(DataclassInstance):
    loginId: str
    travelDateStart: str
    travelDateEnd: str
    boughtDateStart: str
    boughtDateEnd: str
    state: int
    enableTravelDateQuery: bool
    enableBoughtDateQuery: bool
    enableStateQuery: bool


@dataclass
class Seat(DataclassInstance):
    travelDate: str


def home(client: requests.Session, host: str):
    """
    /api/v1/orderservice/welcome GET
    """
    url = "/api/v1/orderservice/welcome"
    response = client.request(url=host + url, method='GET')
    return response.text


def get_sold_tickets(client: requests.Session, seat_request: Seat, host: str, headers: dict):
    """
    /api/v1/orderservice/order/tickets POST
    """
    url = "/api/v1/orderservice/order/tickets"
    response = client.request(url=host + url, method='POST', json=asdict(seat_request), headers=headers)
    return response.json()


def create_new_order(client: requests.Session, order: Order, host: str, headers: dict):
    """
    /api/v1/orderservice/order POST
    """
    url = "/api/v1/orderservice/order"
    response = client.request(url=host + url, method='POST', json=asdict(order), headers=headers)
    return response.json()


def add_new_order(client: requests.Session, order: Order, host: str, headers: dict):
    """
    /api/v1/orderservice/order/admin POST
    """
    url = "/api/v1/orderservice/order/admin"
    response = client.request(url=host + url, method='POST', json=asdict(order), headers=headers)
    return response.json()


def query_orders(client: requests.Session, qi: OrderInfo, host: str, headers: dict):
    """
    /api/v1/orderservice/order/query POST
    """
    url = "/api/v1/orderservice/order/query"
    response = client.request(url=host + url, method='POST', json=asdict(qi), headers=headers)
    return response.json()


def query_orders_for_refresh(client: requests.Session, qi: OrderInfo, host: str, headers: dict):
    """
    /api/v1/orderservice/order/refresh POST
    """
    url = "/api/v1/orderservice/order/refresh"
    response = client.request(url=host + url, method='POST', json=asdict(qi), headers=headers)
    return response.json()


def calculate_sold_ticket(client: requests.Session, travel_date: str, train_number: str, host: str, headers: dict):
    """
    /api/v1/orderservice/order/{travelDate}/{trainNumber} GET
    """
    url = f"/api/v1/orderservice/order/{travel_date}/{train_number}"
    response = client.request(url=host + url, method='GET', headers=headers)
    return response.json()


def get_order_price(client: requests.Session, order_id: str, host: str, headers: dict):
    """
    /api/v1/orderservice/order/price/{orderId} GET
    """
    url = f"/api/v1/orderservice/order/price/{order_id}"
    response = client.request(url=host + url, method='GET', headers=headers)
    return response.json()


def pay_order(client: requests.Session, order_id: str, host: str, headers: dict):
    """
    /api/v1/orderservice/order/orderPay/{orderId} GET
    """
    url = f"/api/v1/orderservice/order/orderPay/{order_id}"
    response = client.request(url=host + url, method='GET', headers=headers)
    return response.json()


def get_order_by_id(client: requests.Session, order_id: str, host: str, headers: dict):
    """
    /api/v1/orderservice/order/{orderId} GET
    """
    url = f"/api/v1/orderservice/order/{order_id}"
    response = client.request(url=host + url, method='GET', headers=headers)
    return response.json()


def modify_order(client: requests.Session, order_id: str, status: int, host: str, headers: dict):
    """
    /api/v1/orderservice/order/status/{orderId}/{status} GET
    """
    url = f"/api/v1/orderservice/order/status/{order_id}/{status}"
    response = client.request(url=host + url, method='GET', headers=headers)
    return response.json()


def security_info_check(client: requests.Session, check_date: str, account_id: str, host: str, headers: dict):
    """
    /api/v1/orderservice/order/security/{checkDate}/{accountId} GET
    """
    url = f"/api/v1/orderservice/order/security/{check_date}/{account_id}"
    response = client.request(url=host + url, method='GET', headers=headers)
    return response.json()


def save_order_info(client: requests.Session, order_info: Order, host: str, headers: dict):
    """
    /api/v1/orderservice/order PUT
    """
    url = "/api/v1/orderservice/order"
    response = client.request(url=host + url, method='PUT', json=asdict(order_info), headers=headers)
    return response.json()


def update_order(client: requests.Session, order: Order, host: str, headers: dict):
    """
    /api/v1/orderservice/order/admin PUT
    """
    url = "/api/v1/orderservice/order/admin"
    response = client.request(url=host + url, method='PUT', json=asdict(order), headers=headers)
    return response.json()


def delete_order(client: requests.Session, order_id: str, host: str, headers: dict):
    """
    /api/v1/orderservice/order/{orderId} DELETE
    """
    url = f"/api/v1/orderservice/order/{order_id}"
    response = client.request(url=host + url, method='DELETE', headers=headers)
    return response.json()


def find_all_order(client: requests.Session, host: str, headers: dict):
    """
    /api/v1/orderservice/order GET
    """
    url = "/api/v1/orderservice/order"
    response = client.request(url=host + url, method='GET', headers=headers)
    return response.json()
