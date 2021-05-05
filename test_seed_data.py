from model import *
from datetime import datetime, timezone
from helpers import *

def test_all():
    test_user()
    test_image()
    test_tag()

def test_user():
    """Creates test user in test database"""

    register_user('Guppy', 'guppy@thecat.com', 'badpw')


def test_image():
    """Creates test image in test database"""

    test_img = Image(
        url='https://s.keepmeme.com/files/en_posts/20200822/cc83fa3c7f8f8d04b3cdb12d65d57101confused-cat-with-a-lot-of-question-marks.jpg', 
        notes='this cat is CONFUSE', 
        private=False,
        time=datetime.now(timezone.utc),
        user_id=1,
        tag_id=None)
    db.session.add(test_img)
    db.session.commit()


def test_tag():
    """Creates test tag in test database"""

    test_tag = Tag(
        name='honey badgers', 
        icon='fas fa-badger-honey',
        hex_code='#FFC0CB',
        user_id=1)
    db.session.add(test_tag)
    db.session.commit()