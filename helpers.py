from model import db, User, Image, Tag


##### * General queries * #####

def get_all_users():
    return User.query.all()

def get_user_by_user_id(user_id):
    return User.query.filter(User.user_id == user_id).first()


##### * User registration & login * #####

def check_username(username):
    """Check whether given username exists in users table."""
    return User.query.filter(User.username == username).first()

def check_email(email):
    """Check whether given email exists in users table."""
    return User.query.filter(User.email == email).first()

def register_user(username, email, password):
    """Add a user to the database."""
    user = User(
        username=username, 
        email=email, 
        password_hashed=User.get_hash(password))
    db.session.add(user)
    db.session.commit()

    return user


##### * Image upload and retrieval * #####

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

def get_images_by_user(user_id):
    return Image.query.filter(Image.user_id == user_id).all()
    

##### * Tags * #####

def create_tag(name, icon, hex_code, user_id):
    tag = Tag(
        name=name,
        icon=icon,
        hex_code=hex_code,
        user_id=user_id
    )
    db.session.add(tag)
    db.session.commit()

    return tag