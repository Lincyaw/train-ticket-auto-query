import requests


def get_all_orders(client: requests.Session, host: str):
    url="/api/v1/adminorderservice/adminorder"
    response=client.request(url=host+url, method='GET',
                            headers={"Accept": "*/*"})
    return response.json()


def add_order(client: requests.Session, order: dict, host: str):
    url="/api/v1/adminorderservice/adminorder"
    response=client.request(url=host+url, method='POST',
                            headers={"Accept": "*/*"}, json=order)
    return response.json()


def update_order(client: requests.Session, order: dict, host: str):
    url="/api/v1/adminorderservice/adminorder"
    response=client.request(url=host+url, method='PUT', json=order)
    return response.json()


def delete_order(client: requests.Session, orderId: str, trainNumber: str, host: str):
    url=f"/api/v1/adminorderservice/adminorder/{orderId}/{trainNumber}"
    response=client.request(url=host+url, method='DELETE')
    return response.json()


def get_welcome(client: requests.Session, host: str):
    url="/api/v1/adminorderservice/welcome"
    response=client.request(url=host+url, method='GET',
                            headers={"Accept": "*/*"})
    return response.text
