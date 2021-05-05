from model import User, db

def register_user(username, email, password):
    user = User(
        username=username, 
        email=email, 
        password_hashed=User.get_hash(password))
    db.session.add(user)
    db.session.commit()

    return user