class BaseConfig(object):
    """Common configurations"""
    TESTING = False
    DEBUG = False
    SECRET_KEY = "qwertyuiop"


class DevelopmentConfig(BaseConfig):
    """Development configurations"""
    DATABASE_URL = 'postgresql://postgres:mathias@localhost:5432/stackoverflow'
    DEBUG = True


class TestingConfig(BaseConfig):
    """Configurations for Testing, with a separate test database."""
    DATABASE_URL = 'postgresql://postgres:mathias@localhost:5432/stackoverflow_tests'
    TESTING = True
    DEBUG = True


class ProductionConfig(BaseConfig):
    """Production configurations"""
    DEBUG = False


app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}
