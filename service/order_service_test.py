import uuid

import requests

from service import DataclassInstance
from service.order_service import *
from dataclasses import dataclass
from service.auth_service import users_login

BASE_URL="http://10.10.10.220:30604"

headers={
    'Proxy-Connection': 'keep-alive',
    'Accept': 'application/json',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
    'Content-Type': 'application/json',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Connection': 'keep-alive',
}


@dataclass
class DtoLoginUser(DataclassInstance):
    password: str
    username: str
    verificationCode: str


@dataclass
class DtoLoginUser(DataclassInstance):
    password: str
    username: str
    verificationCode: str


def test_get_all_orders():
    client=requests.Session()
    result=find_all_orders(client, BASE_URL)
    print(result['data'])
    assert result['msg']=='Success.'


def test_create_new_order():
    client=requests.Session()
    basic_auth_dto=DtoLoginUser(username='admin',
                                password='222222', verificationCode="123")
    token=users_login(client, basic_auth_dto, headers, BASE_URL)
    client.headers.update({'Authorization': f'Bearer {token}'})

    newOrder={
        "accountId": str(uuid.uuid4()),
        "boughtDate": "string",
        "coachNumber": 0,
        "contactsDocumentNumber": "string",
        "contactsName": "string",
        "differenceMoney": "string",
        "documentType": 0,
        "from": "string",
        "id": str(uuid.uuid4()),
        "price": "string",
        "seatClass": 0,
        "seatNumber": "string",
        "status": 0,
        "to": "string",
        "trainNumber": "string",
        "travelDate": "string",
        "travelTime": "string"
    }
    ret=create_new_order(client, newOrder, BASE_URL)
    assert ret['msg']=='Success'


def test_save_order_info():
    client=requests.Session()
    basic_auth_dto=DtoLoginUser(username='admin',
                                password='222222', verificationCode="123")
    token=users_login(client, basic_auth_dto, headers, BASE_URL)
    client.headers.update({'Authorization': f'Bearer {token}'})
    newOrder={
        "accountId": "string",
        "boughtDate": "string",
        "coachNumber": 0,
        "contactsDocumentNumber": "string",
        "contactsName": "string",
        "differenceMoney": "string",
        "documentType": 0,
        "from": "string",
        "id": '3ef1a6da-faa9-4591-8546-386c0925b6a9',
        "price": "string",
        "seatClass": 0,
        "seatNumber": "string",
        "status": 0,
        "to": "string",
        "trainNumber": "string",
        "travelDate": "string",
        "travelTime": "string"
    }
    ret=save_order_info(client, newOrder, BASE_URL)
    assert ret['msg']=='Success'


def test_add_create_new_order():
    client=requests.Session()
    basic_auth_dto=DtoLoginUser(username='admin',
                                password='222222', verificationCode="123")
    token=users_login(client, basic_auth_dto, headers, BASE_URL)
    client.headers.update({'Authorization': f'Bearer {token}'})

    newOrder={
        "accountId": str(uuid.uuid4()),
        "boughtDate": "string",
        "coachNumber": 0,
        "contactsDocumentNumber": "string",
        "contactsName": "string",
        "differenceMoney": "string",
        "documentType": 0,
        "from": "string",
        "id": "string",
        "price": "string",
        "seatClass": 0,
        "seatNumber": "string",
        "status": 0,
        "to": "string",
        "trainNumber": "string",
        "travelDate": "string",
        "travelTime": "string"
    }
    ret=add_create_new_order(client, newOrder, BASE_URL)
    assert ret['msg']=='Add new Order Success'


def test_update_order():
    client=requests.Session()
    basic_auth_dto=DtoLoginUser(username='admin',
                                password='222222', verificationCode="123")
    token=users_login(client, basic_auth_dto, headers, BASE_URL)
    client.headers.update({'Authorization': f'Bearer {token}'})
    newOrder={
        "accountId": "string",
        "boughtDate": "string",
        "coachNumber": 0,
        "contactsDocumentNumber": "string",
        "contactsName": "string",
        "differenceMoney": "string",
        "documentType": 0,
        "from": "string",
        "id": '053ba240-b71b-4ab8-97b2-2648dc6c9274',
        "price": "string",
        "seatClass": 0,
        "seatNumber": "string",
        "status": 0,
        "to": "string",
        "trainNumber": "string",
        "travelDate": "string",
        "travelTime": "string"
    }
    ret=update_order(client, newOrder, BASE_URL)
    assert ret['msg']=='Admin Update Order Success'


def test_pay_order():
    client=requests.Session()
    ret=pay_order(client, '053ba240-b71b-4ab8-97b2-2648dc6c9274', BASE_URL)
    assert ret['msg']=='Pay Order Success.'


def test_get_order_price():
    client=requests.Session()
    ret=get_order_price(client, '053ba240-b71b-4ab8-97b2-2648dc6c9274', BASE_URL)
    assert ret['msg']=='Success'


def test_query_orders():
    client=requests.Session()
    qi={
        "boughtDateEnd": "2020-11-12",
        "boughtDateStart": "2020-11-10",
        "enableBoughtDateQuery": True,
        "enableStateQuery": True,
        "enableTravelDateQuery": True,
        "loginId": '3ef1a6da-faa9-4591-8546-386c0925b6a9',
        "state": 1,
        "travelDateEnd": "2020-11-18",
        "travelDateStart": "2020-11-15"
    }
    ret=query_orders(client, qi, BASE_URL)
    assert ret['msg']=='Get order num'


def test_query_order_for_refresh():
    client=requests.Session()
    qi={
        "boughtDateEnd": "2020-11-12",
        "boughtDateStart": "2020-11-10",
        "enableBoughtDateQuery": True,
        "enableStateQuery": True,
        "enableTravelDateQuery": True,
        "loginId": '3ef1a6da-faa9-4591-8546-386c0925b6a9',
        "state": 1,
        "travelDateEnd": "2020-11-18",
        "travelDateStart": "2020-11-15"
    }
    ret=query_order_for_refresh(client, qi, BASE_URL)
    assert ret['msg']=='Query Orders For Refresh Success'


def test_security_info_check():
    client=requests.Session()
    checkDate='string'
    accountId='string'
    ret=security_info_check(client, checkDate, accountId, BASE_URL)
    assert ret['msg']=='Check Security Success . '


def test_modify_order():
    client=requests.Session()
    orderId='053ba240-b71b-4ab8-97b2-2648dc6c9274'
    status=1
    ret=modify_order(client, orderId, status, BASE_URL)
    print(ret)


def test_get_ticket_list_by_date_and_tripId():
    client=requests.Session()
    seat={
        "destStation": "shanghai",
        "seatType": 0,
        "startStation": "suzhou",
        "stations": [
            "string"
        ],
        "totalNum": 0,
        "trainNumber": "G123",
        "travelDate": "2020-12-14"
    }
    ret=get_ticket_list_by_date_and_tripId(client, seat, BASE_URL)
    print(ret)


def test_delete_order():
    client=requests.Session()
    orderId='6a5022b7-8109-400f-91aa-7d08fbb65a7d'
    ret=delete_order(client, orderId, BASE_URL)
    assert ret['msg']=='Delete Order Success'


def test_get_order_by_id():
    client=requests.Session()
    orderId='053ba240-b71b-4ab8-97b2-2648dc6c9274'
    ret=get_order_by_id(client, orderId, BASE_URL)
    assert ret['msg']=='Success.'


def test_calculate_sold_ticket():
    client=requests.Session()
    travelDate='string'
    trainNumber='string'
    ret=calculate_sold_ticket(client, travelDate, trainNumber, BASE_URL)
    assert ret['msg']=='Success'


def test_home():
    client=requests.Session()
    basic_auth_dto=DtoLoginUser(username='admin',
                                password='222222', verificationCode="123")
    token=users_login(client, basic_auth_dto, headers, BASE_URL)
    client.headers.update({'Authorization': f'Bearer {token}'})
    ret=home(client, BASE_URL)
    assert ret=='Welcome to [ Order Service ] !'
