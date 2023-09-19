import unittest
from src.controller import app


class MyTestCase(unittest.TestCase):
    def test_hello_world(self):
        test_app = app.test_client()
        response = test_app.get('/')

        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Hello World !', response.data)
