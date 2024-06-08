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
    assert result['msg'] == 'Travel Service Admin Query All Travel Success'

def test_add_travel():
    client = requests.Session()
    basic_auth_dto=DtoLoginUser(username='admin',
                                password='222222', verificationCode="123")
    token=users_login(client, basic_auth_dto, headers, BASE_URL)
    client.headers.update({'Authorization': f'Bearer {token}'})

    newTravel = {
        "endTime": "string",
        "loginId": "string",
        "routeId": "92708982-77af-4318-be25-57ccb0ff69ad",
        "startStationName": "nanjing",
        "startTime": "string",
        "stationsName": "shanghai",
        "terminalStationName": "shanghai",
        "trainTypeName": "GaoTieOne",
        "tripId": "G1236"
    }

    ret = add_travel(client,newTravel,BASE_URL)
    assert ret['msg'] == '[Admin add new travel]'

def test_update_travel():
    client = requests.Session()
    basic_auth_dto=DtoLoginUser(username='admin',
                                password='222222', verificationCode="123")
    token=users_login(client, basic_auth_dto, headers, BASE_URL)
    client.headers.update({'Authorization': f'Bearer {token}'})
    newTravel = {
        "endTime": "string",
        "loginId": "string",
        "routeId": "92708982-77af-4318-be25-57ccb0ff69ad",
        "startStationName": "nanjing",
        "startTime": "string",
        "stationsName": "shanghai",
        "terminalStationName": "shanghai",
        "trainTypeName": "GaoTieOne",
        "tripId": "G1236"
    }

    ret = update_travel(client,newTravel,BASE_URL)
    assert ret['msg'] == 'Update trip:G1236'

def test_delete_travel():
    travelId='G1236'
    client=requests.Session()
    basic_auth_dto=DtoLoginUser(username='admin',
                                password='222222', verificationCode="123")
    token=users_login(client, basic_auth_dto, headers, BASE_URL)
    client.headers.update({'Authorization': f'Bearer {token}'})
    ret = delete_travel(client,travelId,BASE_URL)
    assert ret['msg'] == 'Delete trip:G1236.'

def test_get_welcome():
    client=requests.Session()
    basic_auth_dto=DtoLoginUser(username='admin',
                                password='222222', verificationCode="123")
    token=users_login(client, basic_auth_dto, headers, BASE_URL)
    client.headers.update({'Authorization': f'Bearer {token}'})
    ret = get_welcome(client,BASE_URL)
    assert ret == 'Welcome to [ AdminTravel Service ] !'

def test_whole_chain():
    # welcome
    client = requests.Session()
    basic_auth_dto = DtoLoginUser(username='admin',
                                  password='222222', verificationCode="123")
    token = users_login(client, basic_auth_dto, headers, BASE_URL)
    client.headers.update({'Authorization': f'Bearer {token}'})
    ret = get_welcome(client, BASE_URL)
    assert ret == 'Welcome to [ AdminTravel Service ] !'
    # add
    newTravel = {
        "endTime": "string",
        "loginId": "string",
        "routeId": "92708982-77af-4318-be25-57ccb0ff69ad",
        "startStationName": "nanjing",
        "startTime": "string",
        "stationsName": "shanghai",
        "terminalStationName": "shanghai",
        "trainTypeName": "GaoTieOne",
        "tripId": "G1236"
    }
    ret = add_travel(client, newTravel, BASE_URL)
    assert ret['msg'] == '[Admin add new travel]'
    # update
    ret = update_travel(client, newTravel, BASE_URL)
    assert ret['msg'] == 'Update trip:G1236'
    # delete
    ret = delete_travel(client, 'G1236', BASE_URL)
    assert ret['msg'] == 'Delete trip:G1236.'
