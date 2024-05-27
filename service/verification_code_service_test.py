import unittest
import requests
from faker import Faker
from service.verification_code_service import *
from service.test_utils import BASE_URL, headers as test_headers
from tkinter import Image

fake = Faker()


class TestVerificationCodeService(unittest.TestCase):
    def setUp(self):
        self.client = requests.Session()
        self.host = BASE_URL

    def test_generate_verification_code(self):
        image = generate_verification_code(self.client, self.host, test_headers)
        self.assertIsInstance(image, Image.Image)

    def test_verify_code(self):
        verify_code = fake.lexify(text='????')
        result = verify_code(self.client, verify_code, self.host, test_headers)
        self.assertIsInstance(result, VerifyCodeResult)

    def test_end_to_end(self):
        image = generate_verification_code(self.client, self.host, test_headers)
        self.assertIsInstance(image, Image.Image)

        # Simulate user inputting the verification code
        verify_code = fake.lexify(text='????')

        result = verify_code(self.client, verify_code, self.host, test_headers)
        self.assertIsInstance(result, VerifyCodeResult)


if __name__ == '__main__':
    unittest.main()