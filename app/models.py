#database models
from . import db
from flask import json
from sqlalchemy import Numeric
from datetime import datetime, timedelta


class User(db.Model):
    __tablename__ = "user"

    id = db.Column(db.BigInteger, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    name = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(120), nullable=False)
    role = db.Column(db.String(80), nullable=True)
    admn_no = db.Column(db.String(20), unique=True, nullable=False)
    loans = db.relationship("Loan", backref="user", lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"

    loans = db.relationship(
        "Loan", backref="user", lazy=True
    )  # user can have multiple loans

    def details(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "admn_no": self.admn_no,  # Include admn_no in the dictionary
        }