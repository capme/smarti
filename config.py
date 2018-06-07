import os
from dotenv import load_dotenv

# i'll load my .env here for first time
dotenv_file = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_file)


class Config:
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    DEBUG = False
    SECRET_KEY = os.getenv('SECRET_KEY') or 'imyoursecretkey'
    API_KEY = os.getenv('API_KEY')

    TOKEN_EXPIRY = int(os.getenv('TOKEN_EXPIRY'))
    CHANNEL_TOKEN_EXPIRY = int(os.getenv('CHANNEL_TOKEN_EXPIRY'))

    BUNDLE_ERRORS = True

    REDIS_HOST = os.getenv('REDIS_HOST')

    LOGGING_LEVEL = 'INFO'
    LOGGING_BACKUP_COUNT = 1
    LOGGING_FORMAT = '%(asctime)s - local.%(levelname)s - %(module)s ' \
                     '- %(funcName)s - %(message)s'

    LOGENTRIES_TOKEN = os.getenv('LOGENTRIES_TOKEN')
    CACHE_TYPE = 'redis'
    CACHE_KEY_PREFIX = 'valkyrie_magento'


class TestingConfig(Config):
    TESTING = True


class LocalConfig(Config):
    DEBUG = True


class StagingConfig(Config):
    DEBUG = False

    LOGGING_FORMAT = '%(asctime)s - staging.%(levelname)s - %(funcName)s ' \
                     '- %(module)s - %(message)s'


class ProductionConfig(Config):
    DEBUG = False

    LOGGING_FORMAT = '%(asctime)s - production.%(levelname)s - %(funcName)s ' \
                     '- %(module)s - %(message)s'


config = {
    'local': LocalConfig,
    'testing': TestingConfig,
    'staging': StagingConfig,
    'production': ProductionConfig,
}
