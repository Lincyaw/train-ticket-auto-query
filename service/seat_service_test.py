import unittest
from service.seat_service import *
from service.auth_service import DtoLoginUser, users_login
from service.test_utils import BASE_URL, headers
from faker import Faker

fake = Faker()


class TestSeatService(unittest.TestCase):
    def setUp(self):
        self.client = requests.Session()
        self.host = BASE_URL
        basic_auth_dto = DtoLoginUser(username='fdse_microservice',
                                      password='111111', verificationCode="123")
        token = users_login(self.client, basic_auth_dto, headers, BASE_URL)
        self.headers = {'Authorization': f'Bearer {token}'}

    def tearDown(self):
        self.client.close()

    def test_home(self):
        response = home(self.client, self.host)
        self.assertIsInstance(response, str)

    def test_distribute_seat(self):
        seat_request = Seat(travelDate=fake.date(), trainNumber=fake.word(), seatType=fake.word())
        response = distribute_seat(self.client, seat_request, self.host, self.headers)
        self.assertIsInstance(response, dict)

    def test_get_left_ticket_of_interval(self):
        seat_request = Seat(travelDate=fake.date(), trainNumber=fake.word(), seatType=fake.word())
        response = get_left_ticket_of_interval(self.client, seat_request, self.host, self.headers)
        self.assertIsInstance(response, dict)

    def test_end_to_end(self):
        # Step 1: Distribute seat
        distribute_request = Seat(travelDate=fake.date(), trainNumber=fake.word(), seatType=fake.word())
        distribute_response = distribute_seat(self.client, distribute_request, self.host, self.headers)
        self.assertIsInstance(distribute_response, dict)

        # Step 2: Get left ticket of interval
        left_ticket_request = Seat(travelDate=distribute_request.travelDate,
                                   trainNumber=distribute_request.trainNumber,
                                   seatType=distribute_request.seatType)
        left_ticket_response = get_left_ticket_of_interval(self.client, left_ticket_request, self.host, self.headers)
        self.assertIsInstance(left_ticket_response, dict)

        # Step 3: Verify the left ticket count
        self.assertGreaterEqual(left_ticket_response['count'], 0)


if __name__ == '__main__':
    unittest.main()
