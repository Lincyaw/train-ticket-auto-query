import requests
from typing import List, Dict
from dataclasses import dataclass, asdict
from requests.structures import CaseInsensitiveDict
from service.common import *


@dataclass
class Seat(DataclassInstance):
    travelDate: str


@dataclass
class QueryInfo(DataclassInstance):
    loginId: str


@dataclass
class Order(DataclassInstance):
    id: str
    from_station: str
    # from_station: str = field(metadata={"json_key": "from"})
    to: str
    travelDate: str

    @staticmethod
    def from_dict(obj: Any) -> 'Order':
        _id = obj.get("id")
        _from = obj.get("from")
        _to = obj.get("to")
        _travelDate = obj.get("travelDate")
        return Order(_id, _from, _to, _travelDate)


def home(client: requests.Session, host: str):
    url = f"{host}/api/v1/orderOtherService/welcome"
    response = client.request(method="GET", url=url)
    return response.text


def get_sold_tickets(client: requests.Session, host: str, seat_request: Seat, headers: CaseInsensitiveDict[str]) -> \
List[str]:
    url = f"{host}/api/v1/orderOtherService/orderOther/tickets"
    response = client.request(method="POST", url=url, json=asdict(seat_request), headers=headers)
    return response.json()


def create_new_order(client: requests.Session, host: str, order: Order, headers: CaseInsensitiveDict[str]) -> bool:
    url = f"{host}/api/v1/orderOtherService/orderOther"
    response = client.request(method="POST", url=url, json=asdict(order), headers=headers)
    return response.json()


def add_new_order(client: requests.Session, host: str, order: Order, headers: CaseInsensitiveDict[str]) -> bool:
    url = f"{host}/api/v1/orderOtherService/orderOther/admin"
    response = client.request(method="POST", url=url, json=asdict(order), headers=headers)
    return response.json()


def query_orders(client: requests.Session, host: str, qi: QueryInfo, headers: CaseInsensitiveDict[str]) -> List[Order]:
    url = f"{host}/api/v1/orderOtherService/orderOther/query"
    response = client.request(method="POST", url=url, json=asdict(qi), headers=headers)
    return [Order.from_dict(item) for item in response.json()]


def query_orders_for_refresh(client: requests.Session, host: str, qi: QueryInfo, headers: CaseInsensitiveDict[str]) -> \
List[Order]:
    url = f"{host}/api/v1/orderOtherService/orderOther/refresh"
    response = client.request(method="POST", url=url, json=asdict(qi), headers=headers)
    return [Order.from_dict(item) for item in response.json()]


def calculate_sold_ticket(client: requests.Session, host: str, travel_date: str, train_number: str,
                          headers: CaseInsensitiveDict[str]) -> int:
    url = f"{host}/api/v1/orderOtherService/orderOther/{travel_date}/{train_number}"
    response = client.request(method="GET", url=url, headers=headers)
    return response.json()


def get_order_price(client: requests.Session, host: str, order_id: str, headers: CaseInsensitiveDict[str]) -> float:
    url = f"{host}/api/v1/orderOtherService/orderOther/price/{order_id}"
    response = client.request(method="GET", url=url, headers=headers)
    return response.json()


def pay_order(client: requests.Session, host: str, order_id: str, headers: CaseInsensitiveDict[str]) -> bool:
    url = f"{host}/api/v1/orderOtherService/orderOther/orderPay/{order_id}"
    response = client.request(method="GET", url=url, headers=headers)
    return response.json()


def get_order_by_id(client: requests.Session, host: str, order_id: str, headers: CaseInsensitiveDict[str]) -> Order:
    url = f"{host}/api/v1/orderOtherService/orderOther/{order_id}"
    response = client.request(method="GET", url=url, headers=headers)
    return Order.from_dict(response.json())


def modify_order(client: requests.Session, host: str, order_id: str, status: int,
                 headers: CaseInsensitiveDict[str]) -> bool:
    url = f"{host}/api/v1/orderOtherService/orderOther/status/{order_id}/{status}"
    response = client.request(method="GET", url=url, headers=headers)
    return response.json()


def security_info_check(client: requests.Session, host: str, check_date: str, account_id: str,
                        headers: CaseInsensitiveDict[str]) -> Dict:
    url = f"{host}/api/v1/orderOtherService/orderOther/security/{check_date}/{account_id}"
    response = client.request(method="GET", url=url, headers=headers)
    return response.json()


def save_order_info(client: requests.Session, host: str, order_info: Order, headers: CaseInsensitiveDict[str]) -> bool:
    url = f"{host}/api/v1/orderOtherService/orderOther"
    response = client.request(method="PUT", url=url, json=asdict(order_info), headers=headers)
    return response.json()


def update_order(client: requests.Session, host: str, order: Order, headers: CaseInsensitiveDict[str]) -> bool:
    url = f"{host}/api/v1/orderOtherService/orderOther/admin"
    response = client.request(method="PUT", url=url, json=asdict(order), headers=headers)
    return response.json()


def delete_order(client: requests.Session, host: str, order_id: str, headers: CaseInsensitiveDict[str]) -> bool:
    url = f"{host}/api/v1/orderOtherService/orderOther/{order_id}"
    response = client.request(method="DELETE", url=url, headers=headers)
    return response.json()


def find_all_order(client: requests.Session, host: str, headers: CaseInsensitiveDict[str]) -> List[Order]:
    url = f"{host}/api/v1/orderOtherService/orderOther"
    response = client.request(method="GET", url=url, headers=headers)
    return [Order.from_dict(item) for item in response.json()]
