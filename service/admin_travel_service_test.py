import uuid

from service import DataclassInstance
from service.admin_travel_service import *
from dataclasses import dataclass
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

def test_get_all_travels():
    client=requests.Session()
    basic_auth_dto=DtoLoginUser(username='admin',
                                password='222222', verificationCode="123")
    token=users_login(client, basic_auth_dto, headers, BASE_URL)
    client.headers.update({'Authorization': f'Bearer {token}'})
    result = get_all_travels(client, BASE_URL)
    print(result['data'])
    assert result['msg'] == 'Travel Service Admin Query All Travel Success'

def test_add_order():
    client = requests.Session()
    basic_auth_dto=DtoLoginUser(username='admin',
                                password='222222', verificationCode="123")
    token=users_login(client, basic_auth_dto, headers, BASE_URL)
    client.headers.update({'Authorization': f'Bearer {token}'})

    newOrder = {
            "endTime": "string",
            "loginId": "string",
            "routeId": "string",
            "startStationName": "string",
            "startTime": "string",
            "stationsName": "string",
            "terminalStationName": "string",
            "trainTypeName": "string",
            "tripId": "string"
        }

    ret = add_travel(client,newOrder,BASE_URL)
    assert ret['msg'] == 'Success'

def test_update_travel():
    client = requests.Session()
    basic_auth_dto=DtoLoginUser(username='admin',
                                password='222222', verificationCode="123")
    token=users_login(client, basic_auth_dto, headers, BASE_URL)
    client.headers.update({'Authorization': f'Bearer {token}'})
    newTravel = {
                              "accountId": "4d2a46c7-71cb-4cf1-b5bb-b68406d9da6f",
                              "boughtDate": "string",
                              "coachNumber": 0,
                              "contactsDocumentNumber": "string",
                              "contactsName": "string",
                              "differenceMoney": "string",
                              "documentType": 0,
                              "from": "string",
                              "id": '76f5c408-0b16-48a4-9eb5-38693c7cd823',
                              "price": "string",
                              "seatClass": 0,
                              "seatNumber": "string",
                              "status": 0,
                              "to": "string",
                              "trainNumber": "string",
                              "travelDate": "string",
                              "travelTime": "string"
                            }
    ret = update_travel(client,newTravel,BASE_URL)
    assert ret['msg'] == 'Success'

def test_delete_travel():
    travelId='76f5c408-0b16-48a4-9eb5-38693c7cd823'
    client=requests.Session()
    basic_auth_dto=DtoLoginUser(username='admin',
                                password='222222', verificationCode="123")
    token=users_login(client, basic_auth_dto, headers, BASE_URL)
    client.headers.update({'Authorization': f'Bearer {token}'})
    ret = delete_travel(client,travelId,BASE_URL)
    print(ret)
    assert ret['msg'] == 'Delete Order Success'

def test_get_welcome():
    client=requests.Session()
    basic_auth_dto=DtoLoginUser(username='admin',
                                password='222222', verificationCode="123")
    token=users_login(client, basic_auth_dto, headers, BASE_URL)
    client.headers.update({'Authorization': f'Bearer {token}'})
    ret = get_welcome(client,BASE_URL)
    assert ret == 'Welcome to [Admin Order Service] !'