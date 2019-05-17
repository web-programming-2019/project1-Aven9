import os

from flask import Flask, session, render_template, request
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))


@app.route("/")
def index():
    return render_template("index.html")

@app.route('/login', methods=["GET", "POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")
    if request.method == 'POST' and username and password:
        valid = db.execute("SELECT count(*) FROM users where (username = :username AND password = :password)",
                           {
                               "username": username,
                               "password": password
                           }).fetchone
        if valid is None:
            return "User does not exist or password is wrong"
        return render_template("main.html")

    return render_template("login.html")


@app.route('/signup', methods=["GET", "POST"])
def signup():
    username = request.form.get("username")
    password = request.form.get("password")
    if request.method == 'POST' and username and password:
        # insert user item in db
        db.execute("INSERT INTO users (username, password) VALUES (:username, :password)",
                   {
                       "username": username,
                       "password": password
                   })
        db.commit()
        print(f"username:{username}, password{password}")
        return render_template("login.html")
    return render_template("signup.html")
