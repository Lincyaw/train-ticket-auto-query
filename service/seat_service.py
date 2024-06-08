from typing import List
import requests
from dataclasses import dataclass, asdict
from service.common import *


@dataclass
class Seat(DataclassInstance):
    travelDate: str
    trainNumber: str
    destStation: str
    seatType: int
    totalNum: int
    stations: List


def home(client: requests.Session, host: str):
    """
    /api/v1/seatservice/welcome GET
    """
    url = "/api/v1/seatservice/welcome"
    response = client.request(url=host + url, method='GET')
    return response.text


def distribute_seat(client: requests.Session, seat_request: Seat, host: str, headers: dict):
    """
    /api/v1/seatservice/seats POST
    """
    url = "/api/v1/seatservice/seats"
    response = client.request(url=host + url, method='POST', json=asdict(seat_request), headers=headers)
    return response.json()


def get_left_ticket_of_interval(client: requests.Session, seat_request: Seat, host: str, headers: dict):
    """
    /api/v1/seatservice/seats/left_tickets POST
    """
    url = "/api/v1/seatservice/seats/left_tickets"
    response = client.request(url=host + url, method='POST', json=asdict(seat_request), headers=headers)
    return response.json()