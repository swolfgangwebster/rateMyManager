#!/usr/bin/env python3

# Standard library imports

# Remote library imports
from flask import request
from flask_restful import Resource

# Local imports
from config import app, db, api
# Add your model imports
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Views go here!

@app.route('/')
def index():
    return '<h1>ProjectServer</h1>'


if __name__ == '__main__':
    engine = create_engine('sqlite:///instance/app.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    app.run(port=5555, debug=True)

