from celery import Celery
from app import create_app
import os

app = create_app(os.getenv('FLASK_CONFIG') or 'local')
celery = Celery(
    app.import_name,
    backend=app.config['CELERY_RESULT_BACKEND'],
    broker=app.config['CELERY_BROKER_URL']
)
celery.conf.update(app.config)
celery.autodiscover_tasks(lambda: app.config['INSTALLED_APPS'])
