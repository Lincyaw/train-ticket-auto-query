import requests
import uuid

from service.admin_order_service import *
from dataclasses import dataclass, asdict
from service.auth_service import users_login

BASE_URL = "http://10.10.10.220:31948"

headers = {
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

def test_get_all_orders():
    client=requests.Session()
    basic_auth_dto=DtoLoginUser(username='admin',
                                password='222222', verificationCode="123")
    token=users_login(client, basic_auth_dto, headers, BASE_URL)
    client.headers.update({'Authorization': f'Bearer {token}'})
    result = get_all_orders(client, BASE_URL)
    print(result['data'])
    assert result['msg'] == 'Get the orders successfully!'

def test_add_order():
    client = requests.Session()
    basic_auth_dto=DtoLoginUser(username='admin',
                                password='222222', verificationCode="123")
    token=users_login(client, basic_auth_dto, headers, BASE_URL)
    client.headers.update({'Authorization': f'Bearer {token}'})

    newOrder = {
                              "accountId": str(uuid.uuid4()),
                              "boughtDate": "string",
                              "coachNumber": 0,
                              "contactsDocumentNumber": "string",
                              "contactsName": "string",
                              "differenceMoney": "string",
                              "documentType": 0,
                              "from": "beijing",
                              "id": str(uuid.uuid4()),
                              "price": "string",
                              "seatClass": 0,
                              "seatNumber": "string",
                              "status": 0,
                              "to": "shanghai",
                              "trainNumber": "string",
                              "travelDate": "string",
                              "travelTime": "string"
                            }
    ret = add_order(client,newOrder,BASE_URL)
    assert ret['msg'] == 'Success'

def test_update_order():
    client = requests.Session()
    basic_auth_dto=DtoLoginUser(username='admin',
                                password='222222', verificationCode="123")
    token=users_login(client, basic_auth_dto, headers, BASE_URL)
    client.headers.update({'Authorization': f'Bearer {token}'})
    newOrder = {
        "boughtDate": "string",
        "coachNumber": 0,
        "contactsDocumentNumber": "string",
        "contactsName": "string",
        "differenceMoney": "string",
        "documentType": 0,
        "from": "string",
        "id": '3ddae130-38c1-4e8e-abee-11d83f87561f',
        "price": "string",
        "seatClass": 0,
        "seatNumber": "string",
        "status": 0,
        "to": "string",
        "trainNumber": "string",
        "travelDate": "string",
        "travelTime": "string"
                            }
    ret = update_order(client,newOrder,BASE_URL)
    assert ret['msg'] == 'Success'

def test_delete_order():
    orderID='e1cfc963-4324-47ee-9846-f0362df2861d'
    trainNumber='G1237'
    client=requests.Session()
    basic_auth_dto=DtoLoginUser(username='admin',
                                password='222222', verificationCode="123")
    token=users_login(client, basic_auth_dto, headers, BASE_URL)
    client.headers.update({'Authorization': f'Bearer {token}'})
    ret = delete_order(client,orderID,trainNumber,BASE_URL)
    assert ret['msg'] == 'Delete Order Success'

def test_get_welcome():
    client=requests.Session()
    basic_auth_dto=DtoLoginUser(username='admin',
                                password='222222', verificationCode="123")
    token=users_login(client, basic_auth_dto, headers, BASE_URL)
    client.headers.update({'Authorization': f'Bearer {token}'})
    ret = get_welcome(client,BASE_URL)
    assert ret == 'Welcome to [Admin Order Service] !'

def test_whole_chain():
    client=requests.Session()
    basic_auth_dto=DtoLoginUser(username='admin',
                                password='222222', verificationCode="123")
    token=users_login(client, basic_auth_dto, headers, BASE_URL)
    client.headers.update({'Authorization': f'Bearer {token}'})

    newOrderId = str(uuid.uuid4())

    newOrder = {
                              "accountId": str(uuid.uuid4()),
                              "boughtDate": "string",
                              "coachNumber": 0,
                              "contactsDocumentNumber": "string",
                              "contactsName": "string",
                              "differenceMoney": "string",
                              "documentType": 0,
                              "from": "string",
                              "id": newOrderId,
                              "price": "string",
                              "seatClass": 0,
                              "seatNumber": "string",
                              "status": 0,
                              "to": "string",
                              "trainNumber": "U23",
                              "travelDate": "string",
                              "travelTime": "string"
                            }

    ret = get_welcome(client,BASE_URL)
    assert ret == 'Welcome to [Admin Order Service] !'
    ret = add_order(client,newOrder,BASE_URL)
    assert ret['msg'] == 'Success'
    ret = update_order(client,newOrder,BASE_URL)
    assert ret['msg']=='Success'
    ret = delete_order(client,newOrderId,'U23',BASE_URL)
    assert ret['msg'] == 'Delete Order Success'
