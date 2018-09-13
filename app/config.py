"""Configurations"""
import os


class BaseConfig(object):
    """Common configurations"""
    TESTING = False
    DEBUG = False
    SECRET_KEY = os.getenv('SECRET_KEY') or "qwertyuiop"


class DevelopmentConfig(BaseConfig):
    """Development configurations"""
    DEBUG = True


class TestingConfig(BaseConfig):
    """Configurations for Testing, with a separate test database."""
    TESTING = True
    DEBUG = True


app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
}
