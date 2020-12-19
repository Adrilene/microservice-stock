from stock.models.stock_model import Stock


def get_quantity(_id):
    return Stock.objects(product_id=_id).first()


def insert_product(body: dict):
    product = Stock(**body)
    product.save()
    return str(product.id)
