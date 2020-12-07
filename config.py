class Config:
    MAIL_DEFAULT_SENDER = 'ali.khakpash@gmail.com'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USERNAME = 'ali.khakpash@gmail.com'
    MAIL_PASSWORD = '@Stalingerad1945'
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False


class DevelopmentConfig(Config):
    DEBUG = True
    CELERY_BROKER_URL = 'amqp://admin:admin@localhost/myvhost'
    CELERY_RESULT_BACKEND = 'rpc://'
    CELERY_IMPORTS = ("tasks",)


class TestingConfig(Config):
    TESTING = True


class ProductionConfig(Config):
    pass


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
