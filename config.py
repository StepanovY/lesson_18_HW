class Config(object):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///movies.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True
    RESTX_JSON = {'ensure_ascii': False, 'indent': 4}
    # JSON_AS_ASCII = False
    JSON_SORT_KEYS = False
