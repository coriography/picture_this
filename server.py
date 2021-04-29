from flask import Flask, render_template
import jinja2
import os

app = Flask(__name__)
app.secret_key = os.environ["SECRET_KEY"]
app.jinja_env.undefined = jinja2.StrictUndefined

@app.route("/")
def index():
    """Return home page."""

    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")