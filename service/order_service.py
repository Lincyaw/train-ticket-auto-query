import requests

def find_all_orders(client: requests.Session,host: str):
    url = "/api/v1/orderservice/order"
    response = client.request(url=host + url, method='GET',
                              headers={"Accept": "*/*"})
    return response.json()

def create_new_order(client: requests.Session,order:dict,host: str):
    url = "/api/v1/orderservice/order"
    response = client.request(url=host + url, method='POST',
                              headers={"Accept": "*/*"},json=order)
    return response.json()

def save_order_info(client: requests.Session,order:dict,host: str):
    url = "/api/v1/orderservice/order"
    response = client.request(url=host + url, method='PUT',json=order)
    return response.json()

def add_create_new_order(client: requests.Session,order:dict,host: str):
    url = "/api/v1/orderservice/order/admin"
    response = client.request(url=host + url, method='POST',
                              headers={"Accept": "*/*"},json=order)
    return response.json()

def update_order(client: requests.Session,order:dict,host: str):
    url = "/api/v1/orderservice/order/admin"
    response = client.request(url=host + url, method='PUT',json=order)
    return response.json()

def pay_order(client: requests.Session,orderId:str,host: str):
    url = f'/api/v1/orderservice/order/orderPay/{orderId}'
    response=client.request(url=host+url, method='GET')
    return response.json()

def get_order_price(client: requests.Session,orderId:str,host: str):
    url=f'/api/v1/orderservice/order/price/{orderId}'
    response=client.request(url=host+url, method='GET')
    return response.json()

# POST /api/v1/orderservice/order/queryqueryOrders
def query_orders(client: requests.Session,qi:dict,host: str):
    url = '/api/v1/orderservice/order/query'
    response=client.request(url=host+url, method='POST')
    return response.json()
