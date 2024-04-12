import os

CACHE_TYPE = "RedisCache"
CACHE_DEFAULT_TIMEOUT = 300
CACHE_REDIS_URL = os.environ.get("REDISCLOUD_URL")
ENV = os.environ.get("FLASK_ENV", "production")
ES_URL = os.environ.get("ES_URL_PROD", "http://elastic:testpass@127.0.0.1:9200")
DEBUG = ENV == "development"
JSON_SORT_KEYS = False
SECRET_KEY = os.environ.get("SECRET_KEY")

# indexes
AUTHORS_INDEX = "authors-v13"
AUTHORS_INDEX_OLD = "authors-v10"
CONCEPTS_INDEX = "concepts-v8"
CONTINENTS_INDEX = "continents-v1"
COUNTRIES_INDEX = "countries-v2"
DOMAINS_INDEX = "domains-v2"
FIELDS_INDEX = "fields-v2"
FUNDERS_INDEX = "funders-v3"
INSTITUTION_TYPES_INDEX = "institution-types-v1"
INSTITUTIONS_INDEX = "institutions-v8"
KEYWORDS_INDEX = "keywords-v1"
LANGUAGES_INDEX = "languages-v1"
LICENSES_INDEX = "licenses-v1"
PUBLISHERS_INDEX = "publishers-v4"
SDGS_INDEX = "sdgs-v2"
SOURCES_INDEX = "sources-v2"
SOURCE_TYPES_INDEX = "source-types-v1"
SUBFIELDS_INDEX = "subfields-v2"
TOPICS_INDEX = "topics-v4"
WORK_TYPES_INDEX = "work-types-v1"
WORKS_INDEX = "works-v23-*,-*invalid-data"
GROUPBY_VALUES_INDEX = "groupby_values"

DO_NOT_GROUP_BY = [
    "biblio.first_page",
    "biblio.last_page",
    "cited_by",
    "display_name",
    "doi",
    "ids.mag",
    "ids.pmid",
    "ids.pmcid",
    "mag",
    "pmid",
    "pmcid",
    "related_to",
]

EXTERNAL_ID_FIELDS = [
    "has_doi",
    "has_issn",
    "has_orcid",
    "has_pmid",
    "has_pmcid",
    "has_orcid",
    "has_ror",
    "has_wikidata",
    "primary_location.source.has_issn",
]

BOOLEAN_TEXT_FIELDS = [
    "has_abstract",
    "has_ngrams",
    "has_pdf_url",
    "has_raw_affiliation_string",
    "has_references",
]

CONTINENT_PARAMS = {
    "africa": "Q15",
    "antarctica": "Q51",
    "asia": "Q48",
    "europe": "Q46",
    "north_america": "Q49",
    "oceania": "Q55643",
    "south_america": "Q18",
}


CONTINENT_NAMES = [
    {"display_name": "Africa", "id": "Q15", "param": "africa"},
    {"display_name": "Antarctica", "id": "Q51", "param": "antarctica"},
    {"display_name": "Asia", "id": "Q48", "param": "asia"},
    {"display_name": "Europe", "id": "Q46", "param": "europe"},
    {"display_name": "North America", "id": "Q49", "param": "north_america"},
    {"display_name": "Oceania", "id": "Q55643", "param": "oceania"},
    {"display_name": "South America", "id": "Q18", "param": "south_america"},
]

VERSIONS = ["null", "acceptedVersion", "submittedVersion", "publishedVersion"]

MAX_IDS_IN_FILTER = 100
