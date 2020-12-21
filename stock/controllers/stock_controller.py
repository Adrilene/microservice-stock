from flask import request, jsonify
from stock.services.stock_service import get_quantity, insert_product, update_product
from flask_restful import Resource
from stock import app, api
from random import randrange
import json


class StockQuantityController(Resource):
    def get(self, _id):
        product = get_quantity(_id)
        product = json.loads(product.to_json())
        return {"quantity": product["quantity"]}, 200

    def post(self, _id):
        update_product(request.form["quantity"], _id)
        return "OK", 200


class StockController(Resource):
    def post(self):
        data_json = {
            "product_id": request.form["product_id"],
            "quantity": request.form["quantity"],
        }
        insert_product(data_json)
        return "OK", 200


api.add_resource(StockQuantityController, "/stock/<_id>")
api.add_resource(StockController, "/stock")
