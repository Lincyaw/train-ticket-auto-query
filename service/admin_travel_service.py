import requests

def get_all_travels(client: requests.Session,host: str):
    url = "/api/v1/admintravelservice/admintravel"
    response = client.request(url=host + url, method='GET',
                              headers={"Accept": "*/*"})
    return response.json()

def add_travel(client: requests.Session,travel:dict,host: str):
    url = "/api/v1/admintravelservice/admintravel"
    response = client.request(url=host + url, method='POST',
                              headers={"Accept": "*/*"},json=travel)
    return response.json()

def update_travel(client: requests.Session,travel:dict,host: str):
    url = "/api/v1/admintravelservice/admintravel"
    response = client.request(url=host + url, method='PUT',json=travel)
    return response.json()

def delete_travel(client: requests.Session,tripId:str,host: str):
    url = f"/api/v1/admintravelservice/admintravel/{tripId}"
    response=client.request(url=host+url, method='DELETE')
    return response.json()

def get_welcome(client: requests.Session,host: str):
    url = "/api/v1/admintracelservice/welcome"
    response=client.request(url=host+url, method='GET',
                            headers={"Accept": "*/*"})
    return response.text