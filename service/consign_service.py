import requests
from service.common import *
from dataclasses import dataclass, asdict, field
from dataclasses_json import dataclass_json, LetterCase, config
from datetime import datetime
from uuid import UUID


@dataclass
class Consign(DataclassInstance):
    id: str
    orderId: str
    accountId: str
    handleDate: str
    targetDate: str
    from_location: str = field(metadata=config(field_name="from"))
    # from_location: str
    to: str
    consignee: str
    phone: str
    weight: float
    isWithin: bool
    # private String id;        //id主键改成String类型的 自定义生成策略
    # private String orderId;   //这次托运关联订单
    # private String accountId;  //这次托运关联的账户
    #
    # private String handleDate;
    # private String targetDate;
    # private String from;
    # private String to;
    # private String consignee;
    # private String phone;
    # private double weight;
    # private boolean isWithin;


def welcome(client: requests.Session, host: str, headers: dict):
    """
    /api/v1/consignservice/welcome GET
    """
    url = "/api/v1/consignservice/welcome"
    response = client.request(url=host + url, method='GET', headers=headers)
    return response.text


def insert_consign(client: requests.Session, consign: Consign, host: str, headers: dict):
    """
    /api/v1/consignservice/consigns POST
    """
    url = "/api/v1/consignservice/consigns"
    response = client.request(url=host + url, method='POST', json=asdict(consign), headers=headers)
    return response.json()


def update_consign(client: requests.Session, consign: Consign, host: str, headers: dict):
    """
    /api/v1/consignservice/consigns PUT
    """
    url = "/api/v1/consignservice/consigns"
    response = client.request(url=host + url, method='PUT', json=asdict(consign), headers=headers)
    return response.json()


def find_by_account_id(client: requests.Session, id: str, host: str, headers: dict):
    """
    /api/v1/consignservice/consigns/account/{id} GET
    """
    url = f"/api/v1/consignservice/consigns/account/{id}"
    response = client.request(url=host + url, method='GET', headers=headers)
    # return from_dict(Consign, response.json())
    return response.json()


def find_by_order_id(client: requests.Session, id: str, host: str, headers: dict):
    """
    /api/v1/consignservice/consigns/order/{id} GET
    """
    url = f"/api/v1/consignservice/consigns/order/{id}"
    response = client.request(url=host + url, method='GET', headers=headers)
    # return from_dict(Consign, response.json())
    return response.json()


def find_by_consignee(client: requests.Session, consignee: str, host: str, headers: dict):
    """
    /api/v1/consignservice/consigns/{consignee} GET
    """
    url = f"/api/v1/consignservice/consigns/{consignee}"
    response = client.request(url=host + url, method='GET', headers=headers)
    # return from_dict(Consign, response.json())
    return response.json()
