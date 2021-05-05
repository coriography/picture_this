from model import db, User, Image, Tag

def register_user(username, email, password):
    user = User(
        username=username, 
        email=email, 
        password_hashed=User.get_hash(password))
    db.session.add(user)
    db.session.commit()

    return user

def upload_image(url, notes, user_id, private=False, tag_id=None):
    image = Image(
        url=url,
        notes=notes,
        user_id=user_id,
        private=private,
        tag_id=tag_id
    )
    db.session.add(image)
    db.session.commit()

    return image
