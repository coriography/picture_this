# Picture This :heart_eyes: your virtual vision board

Picture This is a photo repository to store and categorize your favorite pics.


## Tech stack :books:  
* Python/Flask with Unittest and bcrypt
* SQL/PostgreSQL
* SQLAlchemy ORM
* Jinja (HTML templating)
* CSS/Bootstrap


## The database model :card_index_dividers:

![app screenshot](/static/img/model_pt_v1.png)


## How it works :desktop_computer:

Users can create an account with a username, email, and password - passwords are hashed and salted using Python's **bcrypt** module and added to the **PostgreSQL** database using **SQLAlchemy**. 

We are confident the database is set up proprerly because we ran our **Unittest** test suite before starting the server!

![app screenshot](/static/img/pt_img_register.png)

When a user logs in, their email and password are checked against the database with the help of **bcrypt**, then they are directed to their Board.

![app screenshot](/static/img/pt_gif_login.gif)

They can add new photos or tags, which will be committed to the database and rendered with Flask's **Jinja2** HTML templating.

![app screenshot](/static/img/pt_gif_tag.gif)

Don't forget to log out!


## Running this app :zap:

Requirements:
Python3
PostgreSQL

To run locally (Mac):

1. Clone this repository to your machine:

```
$ git clone https://github.com/coriography/picture_this
```

2. Create virtual environment:

```
$ python3 -m venv env
```

3. Activate your virtual environment:

```
$ source env/bin/activate
```

4. Install dependencies:

```
$ pip3 install -r requirements.txt
```

5. Set a secret key to run Flask by creating /secrets.sh in your root directory:

![app screenshot](/static/img/secret_key.png)

6. Add your key to your environmental variables:

```
$ source secrets.sh
```

7. Run tests:

```
$ python3 tests.py
```

8. Create database and populate the app with data:

```
$ python3 seed.py
```

9. Launch the server:

```
$ python3 server.py
```

10. Go to localhost:5000 in your browser

11. Create an account, or log in with existing account *guppy@thecat.com, badpw*


## What's next? :thinking:

1. add image hosting with Cloudinary API (see example of this in [Cello Tree](https://github.com/coriography/cello_tree))
2. add search, sort, and color customzation by tag
3. store "private" images in hidden folder
4. add click & drag arrangement of photos on My Board


## About the developer :woman_technologist:

Built by [Cori Lint](https://github.com/coriography), with the help of Guppy the cat. :cat:

*Cori is cellist-turned-software engineer with a knack for motivating and inspiring others. As her career has evolved from performance, to production, to web design, to software engineering, she has continued to seek growth and creative solutions. Cori brings to the tech industry leadership abilities, persistence, focus, empathy, and good judgment, along with a strong set of technical skills and prior experience in web development. She is a Summa Cum Laude graduate of the University of Michigan, and an active member of Artists Who Code, an online community that advocates for creative professionals in the tech industry.*

Contact Cori on [LinkedIn](https://www.linkedin.com/in/cori-lint/)