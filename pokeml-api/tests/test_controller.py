import unittest
from src.controller import app


class MyTestCase(unittest.TestCase):
    def test_should_base_return_error_message_when_front_not_built(self):
        test_app = app.test_client()
        response = test_app.get('/')

        self.assertEqual(response.status_code, 404)
        self.assertIn(b'The front app has not been built. Please follow the README.', response.data)

    def test_health_route(self):
        test_app = app.test_client()
        response = test_app.get('/health')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(b'OK', response.data)
