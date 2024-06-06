import unittest
import requests
from faker import Faker
from service.verification_code_service import *
from service.test_utils import BASE_URL, headers
from tkinter import Image
from service.auth_service import DtoLoginUser, users_login

fake = Faker()


class TestVerificationCodeService(unittest.TestCase):
    def setUp(self):
        self.client = requests.Session()
        self.host = BASE_URL
        basic_auth_dto = DtoLoginUser(username='fdse_microservice',
                                      password='111111', verificationCode="123")
        token = users_login(self.client, basic_auth_dto, headers, BASE_URL)
        self.headers = {'Authorization': f'Bearer {token}'}

    def test_generate_verification_code(self):
        image_response = generate_verification_code(self.client, self.host, headers)
        print(image_response)
        # self.assertIsInstance(image, Image.Image)

    def test_verify_code(self):
        verifyCode = "123456"
        result = verify_code(self.client, verifyCode, self.host, headers)
        print(result)
        self.assertEquals(result, True)

    def test_end_to_end(self):
        image_response = generate_verification_code(self.client, self.host, headers)
        print(image_response)

        # Simulate user inputting the verification code
        verifyCode = "123456"

        result = verify_code(self.client, verifyCode, self.host, headers)
        print(result)
        self.assertEquals(result, True)


if __name__ == '__main__':
    unittest.main()