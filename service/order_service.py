import requests


def find_all_orders(client: requests.Session, host: str):
    url="/api/v1/orderservice/order"
    response=client.request(url=host+url, method='GET',
                            headers={"Accept": "*/*"})
    return response.json()


def create_new_order(client: requests.Session, order: dict, host: str):
    url="/api/v1/orderservice/order"
    response=client.request(url=host+url, method='POST',
                            headers={"Accept": "*/*"}, json=order)
    return response.json()


def save_order_info(client: requests.Session, order: dict, host: str):
    url="/api/v1/orderservice/order"
    response=client.request(url=host+url, method='PUT', json=order)
    return response.json()


def add_create_new_order(client: requests.Session, order: dict, host: str):
    url="/api/v1/orderservice/order/admin"
    response=client.request(url=host+url, method='POST',
                            headers={"Accept": "*/*"}, json=order)
    return response.json()


def update_order(client: requests.Session, order: dict, host: str):
    url="/api/v1/orderservice/order/admin"
    response=client.request(url=host+url, method='PUT', json=order)
    return response.json()


def pay_order(client: requests.Session, orderId: str, host: str):
    url=f'/api/v1/orderservice/order/orderPay/{orderId}'
    response=client.request(url=host+url, method='GET')
    return response.json()


def get_order_price(client: requests.Session, orderId: str, host: str):
    url=f'/api/v1/orderservice/order/price/{orderId}'
    response=client.request(url=host+url, method='GET')
    return response.json()


# POST /api/v1/orderservice/order/queryqueryOrders
def query_orders(client: requests.Session, qi: dict, host: str):
    url='/api/v1/orderservice/order/query'
    response=client.request(url=host+url, method='POST', json=qi)
    return response.json()


def query_order_for_refresh(client: requests.Session, qi: dict, host: str):
    url='/api/v1/orderservice/order/refresh'
    response=client.request(url=host+url, method='POST', json=qi)
    return response.json()


def security_info_check(client: requests.Session, checkDate: str, accountId: str, host: str):
    url=f'/api/v1/orderservice/order/security/{checkDate}/{accountId}'
    response=client.request(url=host+url, method='GET')
    return response.json()


def modify_order(client: requests.Session, orderId: str, status: int, host: str):
    url=f'/api/v1/orderservice/order/status/{orderId}/{status}'
    response=client.request(url=host+url, method='GET')
    return response.json()


def get_ticket_list_by_date_and_tripId(client: requests.Session, seat: dict, host: str):
    url='/api/v1/orderservice/order/tickets'
    response=client.request(url=host+url, method='POST', json=seat)
    return response.json()


def delete_order(client: requests.Session, orderId: str, host: str):
    url=f'/api/v1/orderservice/order/{orderId}'
    response=client.request(url=host+url, method='DELETE')
    return response.json()


def get_order_by_id(client: requests.Session, orderId: str, host: str):
    url=f'/api/v1/orderservice/order/{orderId}'
    response=client.request(url=host+url, method='GET')
    return response.json()


def calculate_sold_ticket(client: requests.Session, travelDate: str, trainNumber: str, host: str):
    url=f'/api/v1/orderservice/order/{travelDate}/{trainNumber}'
    response=client.request(url=host+url, method='GET')
    return response.json()


def home(client: requests.Session, host: str):
    url='/api/v1/orderservice/welcome'
    response=client.request(url=host+url, method='GET')
    return response.text
