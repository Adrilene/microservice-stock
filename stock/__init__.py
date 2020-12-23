from flask import Flask
from flask_restful import Api
from flask_mongoengine import MongoEngine
from flask_cors import CORS


app = Flask(__name__)
app.config["MONGODB_SETTINGS"] = {
    "db": "stock",
    "host": "mongodb+srv://adrilene:arq2201@cluster0.a3msk.mongodb.net/test?authSource=admin&replicaSet=atlas-2nqljv-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true",
}
db = MongoEngine(app)
api = Api(app)
CORS(app)


from .models import stock_model
from .services import stock_service
from .controllers import stock_controller
