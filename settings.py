import os

ENV = os.environ.get("FLASK_ENV", "production")
ES_URL = os.environ.get("ES_URL_PROD")
DEBUG = ENV == "development"
SECRET_KEY = os.environ.get("SECRET_KEY")
