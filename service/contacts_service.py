import requests
from service.common import *
from dataclasses import dataclass, asdict
from uuid import UUID


@dataclass
class Contacts(DataclassInstance):
    id: str
    accountId: str
    name: str
    documentType: int
    documentNumber: str
    phoneNumber: str


def welcome(client: requests.Session, host: str):
    """
    /api/v1/contactservice/contacts/welcome GET
    """
    url = "/api/v1/contactservice/contacts/welcome"
    response = client.request(url=host + url, method='GET')
    return response.text


def get_all_contacts(client: requests.Session, host: str, headers: dict):
    """
    /api/v1/contactservice/contacts GET
    """
    url = "/api/v1/contactservice/contacts"
    response = client.request(url=host + url, method='GET', headers=headers)
    return response.json()


def create_new_contacts(client: requests.Session, contacts: Contacts, host: str, headers: dict):
    """
    /api/v1/contactservice/contacts POST
    """
    url = "/api/v1/contactservice/contacts"
    response = client.request(url=host + url, method='POST', json=asdict(contacts), headers=headers)
    return response.json()


def create_new_contacts_admin(client: requests.Session, contacts: Contacts, host: str, headers: dict):
    """
    /api/v1/contactservice/contacts/admin POST
    """
    url = "/api/v1/contactservice/contacts/admin"
    response = client.request(url=host + url, method='POST', json=asdict(contacts), headers=headers)
    return response.json()


def delete_contacts(client: requests.Session, contactsId: str, host: str, headers: dict):
    """
    /api/v1/contactservice/contacts/{contactsId} DELETE
    """
    url = f"/api/v1/contactservice/contacts/{contactsId}"
    response = client.request(url=host + url, method='DELETE', headers=headers)
    return response.json()


def modify_contacts(client: requests.Session, contacts: Contacts, host: str, headers: dict):
    """
    /api/v1/contactservice/contacts PUT
    """
    url = "/api/v1/contactservice/contacts"
    response = client.request(url=host + url, method='PUT', json=asdict(contacts), headers=headers)
    return response.json()


def find_contacts_by_account_id(client: requests.Session, accountId: str, host: str, headers: dict):
    """
    /api/v1/contactservice/contacts/account/{accountId} GET
    """
    url = f"/api/v1/contactservice/contacts/account/{accountId}"
    response = client.request(url=host + url, method='GET', headers=headers)
    return response.json()


def get_contacts_by_contacts_id(client: requests.Session, id: str, host: str, headers: dict):
    """
    /api/v1/contactservice/contacts/{id} GET
    """
    url = f"/api/v1/contactservice/contacts/{id}"
    response = client.request(url=host + url, method='GET', headers=headers)
    return response.json()