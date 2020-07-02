from .extensions import db


class Pizza(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    img_url = db.Column(db.String(50))
    price = db.Column(db.Float)
    description = db.Column(db.String)
