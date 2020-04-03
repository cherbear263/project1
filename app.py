import os

from flask import Flask, session
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)
# hopefully set the environment to development

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config['TESTING'] = True
app.config['DATABASE_URI'] = 'postgres://pucjimybgpdojz:a419408594c2bd4c33f8bb923b3d43ad5bbd8a336e3f4db7187ad2a40176d809@ec2-52-71-85-210.compute-1.amazonaws.com:5432/d319rsbfd6sca5'
Session(app)

# Set up database

engine = create_engine(os.getenv('DATABASE_URI'))
db = scoped_session(sessionmaker(bind=engine))

# Check for environment variable
if not os.getenv("DATABASE_URI"):
    raise RuntimeError("DATABASE_URL is not set")


@app.route("/")
def index():
    return "Project 1: TODO"
