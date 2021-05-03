import server
import unittest

class serverTests(unittest.TestCase):
    """Tests for Picture This app."""

    def setUp(self):
        """Code to run before every test."""

        self.client = server.app.test_client() # test_client from Werkzeug library returns a "browser" to "run" app
        server.app.config['TESTING'] = True

    def test_homepage(self):
        """Does homepage load?"""

        result = self.client.get("/")
        self.assertEqual(result.status_code, 200)
        self.assertIn(b"Welcome", result.data)

    def test_my_board(self):
        """Does My Board page load?"""

        result = self.client.get("/my_board")
        self.assertEqual(result.status_code, 200)
        self.assertIn(b"board", result.data)

if __name__ == "__main__":
    unittest.main(verbosity=2)