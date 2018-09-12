class BaseConfig(object):
    """Common configurations"""
    TESTING = False
    DEBUG = False
    SECRET_KEY = "qwertyuiop"


class ProductionConfig(BaseConfig):
    DATABASE_URL = 'postgres://krqfsehkasavsb:acb637aceb4536a2b1eb13d145cb75efb6b421764ec3112217a6004d2ce0e4ed@ec2-54' \
                   '-83-4-76.compute-1.amazonaws.com:5432/d3mh07tcck40nj '
    DEBUG = True


class DevelopmentConfig(BaseConfig):
    DATABASE_URL = 'postgresql://postgres:postgres@localhost:5432/stackoverflow_tests'
    DEBUG = True


class TestingConfig(BaseConfig):
    """Configurations for Testing, with a separate test database."""
    DATABASE_URL = 'postgresql://postgres:postgres@localhost:5432/stackoverflow_tests'
    TESTING = True
    DEBUG = True


app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}
