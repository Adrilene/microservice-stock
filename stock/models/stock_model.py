from stock import db
from datetime import datetime


class Stock(db.Document):
    meta = {"collection": "stock"}
    product_id = db.StringField(required=True)
    quantity = db.IntField(required=True)
    created_at = db.DateTimeField(default=datetime.utcnow(), required=False)
