import os

CACHE_TYPE = "RedisCache"
CACHE_DEFAULT_TIMEOUT = 300
CACHE_REDIS_URL = os.environ.get("REDISCLOUD_URL")
ENV = os.environ.get("FLASK_ENV", "production")
ES_URL = os.environ.get("ES_URL_PROD", "http://127.0.0.1:9200")
DEBUG = ENV == "development"
JSON_SORT_KEYS = False
SECRET_KEY = os.environ.get("SECRET_KEY")

# indexes
AUTHORS_INDEX = "authors-v7"
CONCEPTS_INDEX = "concepts-v5"
INSTITUTIONS_INDEX = "institutions-v4"
VENUES_INDEX = "venues-v5"
WORKS_INDEX = "works-v10-*,-*invalid-data"

EXTERNAL_ID_FIELDS = [
    "has_doi",
    "has_issn",
    "has_orcid",
    "has_ror",
    "has_wikidata",
]
