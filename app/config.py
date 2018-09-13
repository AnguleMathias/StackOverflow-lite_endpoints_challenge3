import os


class BaseConfig(object):
    """Common configurations"""
    TESTING = False
    DEBUG = False
    SECRET_KEY = os.getenv('SECRET_KEY') or "qwertyuiop"


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
}
