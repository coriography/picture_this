from server import app
from model import db, connect_to_db
import unittest
import test_seed_data

class serverTests(unittest.TestCase):
    """Tests for Picture This app."""

    def setUp(self):
        """Code to run before every test."""

        self.client = app.test_client() # test_client from Werkzeug library returns a "browser" to "run" app
        app.config['TESTING'] = True

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

    def test_upload_page(self):
        """Does Upload page load?"""

        result = self.client.get("/upload")
        self.assertEqual(result.status_code, 200)
        self.assertIn(b"upload", result.data)


class TestDb(unittest.TestCase):
    """Tests database"""

    def setUp(self):
        """Code to run before every test."""

        self.client = app.test_client()
        app.config['TESTING'] = True

        connect_to_db(app, db_uri='postgresql:///pt')

        db.create_all()
        test_seed_data.test_all()
        ####### ** see test_seed_data.py for test_data helper functions ** #######

    def test_homepage(self):
        """Can I add everything to my db?"""

        result = self.client.get('/')
        self.assertEqual(result.status_code, 200)
        self.assertIn(b"Welcome", result.data)

    def tearDown(self):
        """Code to run after every test"""

        db.session.remove()
        db.drop_all()
        db.engine.dispose()


if __name__ == "__main__":
    unittest.main(verbosity=2)