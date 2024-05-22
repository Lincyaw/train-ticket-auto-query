from queries import Query
from utils import *
import logging

logger = logging.getLogger("autoquery-scenario")
highspeed_weights = {True: 60, False: 40}


def query_and_cancel(q: Query):
    if random_from_weighted(highspeed_weights):
        pairs = q.query_orders(types=tuple([0, 1]))
    else:
        pairs = q.query_orders(types=tuple([0, 1]), query_other=True)

    if not pairs:
        return

    # (orderId, tripId)
    pair = random_from_list(pairs)

    order_id = q.cancel_order(order_id=pair[0])
    if not order_id:
        return

    logger.info(f"{order_id} queried and canceled")


def query_and_collect(q: Query):
    if random_from_weighted(highspeed_weights):
        pairs = q.query_orders(types=tuple([1]))
    else:
        pairs = q.query_orders(types=tuple([1]), query_other=True)

    if not pairs:
        return

    # (orderId, tripId)
    pair = random_from_list(pairs)

    order_id = q.collect_order(order_id=pair[0])
    if not order_id:
        return

    logger.info(f"{order_id} queried and collected")


def query_and_execute(q: Query):
    if random_from_weighted(highspeed_weights):
        pairs = q.query_orders(types=tuple([1]))
    else:
        pairs = q.query_orders(types=tuple([1]), query_other=True)

    if not pairs:
        return

    # (orderId, tripId)
    pair = random_from_list(pairs)

    order_id = q.enter_station(order_id=pair[0])
    if not order_id:
        return

    logger.info(f"{order_id} queried and entered station")


def query_and_preserve(q: Query):
    start = ""
    end = ""
    trip_ids = []

    high_speed = random_from_weighted(highspeed_weights)
    if high_speed:
        start = "Shang Hai"
        end = "Su Zhou"
        high_speed_place_pair = (start, end)
        trip_ids = q.query_high_speed_ticket(place_pair=high_speed_place_pair)
    else:
        start = "Shang Hai"
        end = "Nan Jing"
        other_place_pair = (start, end)
        trip_ids = q.query_normal_ticket(place_pair=other_place_pair)

    _ = q.query_assurances()


    if trip_ids is None:
        trip_ids = []
    q.preserve(start, end, trip_ids, high_speed)


def query_and_consign(q: Query):
    # print("test point 1")
    if random_from_weighted(highspeed_weights):
        # print("test point 2")
        list = q.query_orders_all_info()
        # print("test point 3")
    else:
        # print("test point 4")
        list = q.query_orders_all_info(query_other=True)
        # print("test point 5")

    if not list:
        # print("test point 6")
        return
    
    # print("test point 7")

    # (orderId, tripId)
    res = random_from_list(list)
    # print("test point 7.25")
    order_id = q.put_consign(res)

    # print("test point 7.5")

    if not order_id:
        return

    # print("test point 8")
    logger.info(f"{order_id} queried and put consign")
    # print("test point completed")


def query_and_pay(q: Query):
    if random_from_weighted(highspeed_weights):
        pairs = q.query_orders(types=tuple([0, 1]))
    else:
        pairs = q.query_orders(types=tuple([0, 1]), query_other=True)

    if not pairs:
        return

    # (orderId, tripId)
    pair = random_from_list(pairs)
    order_id = q.pay_order(pair[0], pair[1])

    if not order_id:
        return

    logger.info(f"{order_id} queried and paid")


def query_and_rebook(q: Query):
    if random_from_weighted(highspeed_weights):
        pairs = q.query_orders(types=tuple([0, 1]))
    else:
        pairs = q.query_orders(types=tuple([0, 1]), query_other=True)

    if not pairs:
        return

    # (orderId, tripId)
    pair = random_from_list(pairs)

    order_id = q.cancel_order(order_id=pair[0])
    if not order_id:
        return

    q.rebook_ticket(pair[0], pair[1], pair[1])
    logger.info(f"{order_id} queried and rebooked")