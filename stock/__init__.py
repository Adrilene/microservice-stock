from flask import Flask
from flask_restful import Api
from flask_mongoengine import MongoEngine
from flask_cors import CORS


app = Flask(__name__)
app.config["MONGODB_SETTINGS"] = {
    "db": "devices",
    "host": "mongodb://localhost/stock",
}
db = MongoEngine(app)
api = Api(app)
CORS(app)


from .models import stock_model
from .services import stock_service
from .controllers import stock_controller
