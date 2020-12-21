from stock.models.stock_model import Stock
import json


def get_quantity(_id):
    return Stock.objects(product_id=_id).first()


def insert_product(body: dict):
    product = Stock(**body)
    product.save()
    return str(product.id)


def update_product(quantity, _id):
    product = get_quantity(_id)
    product = json.loads(product.to_json())
    qty = product['quantity'] - int(quantity)
    Stock.objects.get(product_id=_id).update(quantity=qty)