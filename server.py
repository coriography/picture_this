from flask import Flask, render_template, request, flash, redirect, session
import jinja2
import os
from model import connect_to_db
import helpers

app = Flask(__name__) 
app.secret_key = os.environ["SECRET_KEY"] # use key exported from secrets.sh
app.jinja_env.undefined = jinja2.StrictUndefined # throw an error for an undefined Jinja var


##### * RENDER PAGES * #####

@app.route("/")
def go_home():
    """Return home page."""

    return render_template("home.html")

@app.route("/log_in")
def show_login():
    """Return login page."""

    return render_template("login.html")

@app.route("/my_board")
def show_my_board():
    """Return My Board page."""

    if 'user_id' in session:
        user = helpers.get_user_by_user_id(session['user_id'])
    else:
        user = None

    return render_template("my_board.html", user=user)

@app.route("/upload")
def show_upload_page():
    """Return Upload page."""

    if 'user_id' in session:
        user = helpers.get_user_by_user_id(session['user_id'])
    else:
        user = None

    return render_template("upload.html", user=user)

@app.route("/tags")
def show_tags_page():
    """Return Tags page."""

    if 'user_id' in session:
        user = helpers.get_user_by_user_id(session['user_id'])
    else:
        user = None

    return render_template("tags.html", user=user)


##### * API * #####

@app.route('/api/register_user', methods=['POST'])
def register_new_user():
    """Add a new user to the database."""
    
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    
    if helpers.check_username(username) == None and helpers.check_email(email) == None:
        user = helpers.register_user(username, email, password)
        flash(f'Account created!')
        return redirect('/log_in')
    else:
        flash('Try again with a different username and email!')
        return redirect('/')


@app.route('/api/log_in', methods=['POST'])
def log_in_user():
    """Log in existing user."""
    
    email = request.form['email']
    password = request.form['password']
    
    if helpers.check_email(email) == None:
        flash(f'Email doesn\'t exist in database!')
        return redirect('/log_in')
    else:
        user = helpers.check_email(email)
    
    if user.check_password(password):
        # session['user'] = user
        session['user_id'] = user.user_id
        session['username'] = user.username
        flash('Successfully logged in!')
        return render_template('/my_board.html', user=user)
    else:
        flash('Incorrect password!')
        return redirect('/log_in')

@app.route('/api/log_out')
def log_out():

    session.clear()
    flash('Logout successful.')
    return redirect('/')

@app.route('/api/upload', methods=['POST'])
def user_upload_from_form():

    url = request.form['url']
    notes = request.form['notes']
    user_id = session['user_id']
    if 'private' in request.form:
        private = True
    else:
        private = False
    tag_id = request.form['tag_id']

    helpers.upload_image(url, notes, user_id, private, tag_id)

    flash('Upload success message')

    return redirect('/my_board')

@app.route('/api/add_tag', methods=['POST'])
def add_tag_from_form():

    name = request.form['name']
    icon = request.form['icon']
    color = '#e0a356' # TODO: make this dynamic
    user_id = request.form['user_id']

    helpers.create_tag(name, icon, color, user_id)

    flash('Tag created successfully')

    if 'user_id' in session:
        user = helpers.get_user_by_user_id(session['user_id'])
    else:
        user = None

    return render_template("upload.html", user=user)


if __name__ == "__main__":
    connect_to_db(app)
    app.run(debug=True, host="0.0.0.0")