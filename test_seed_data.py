from model import *

def test_user():
    """Creates test user in test database"""

    test_user = User(username='Guppy', email='guppy@thecat.com', password_hashed=User.get_hash('badpw'))
    db.session.add(test_user)
    db.session.commit()