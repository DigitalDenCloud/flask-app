import unittest
from application import application  # Assuming application.py contains your Flask app

class TestFlaskApp(unittest.TestCase):
    def setUp(self):
        self.app = application.test_client()  # Get a Flask test client
        self.app.testing = True

    def test_home(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)  # Ensure the home page is available
    
    def test_hello(self):
        response = self.app.get('/John')  # Assuming your app has a dynamic route like /<username>
        self.assertIn(b'Hello John!', response.data)  # Check if the response contains the expected greeting

if __name__ == '__main__':
    unittest.main()
