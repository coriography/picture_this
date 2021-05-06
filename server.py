from flask import Flask, render_template
import jinja2
import os
from model import connect_to_db

app = Flask(__name__) 
app.secret_key = os.environ["SECRET_KEY"] # use key exported from secrets.sh
app.jinja_env.undefined = jinja2.StrictUndefined # throw an error for an undefined Jinja var

@app.route("/")
def go_home():
    """Return home page."""

    return render_template("home.html")

@app.route("/my_board")
def show_my_board():
    """Return My Board page."""

    return render_template("my_board.html")

@app.route("/upload")
def show_upload_page():
    """Return My Board page."""

    return render_template("upload.html")

if __name__ == "__main__":
    connect_to_db(app)
    app.run(debug=True, host="0.0.0.0")