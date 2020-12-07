import time

from flask import Flask
from celery import Celery

celery_flask = Flask(__name__)
celery_flask.config['CELERY_BROKER_URL'] = 'amqp://admin:admin@localhost/myvhost'
celery_flask.config['CELERY_RESULT_BACKEND'] = 'rpc://'

celery = Celery(celery_flask.name, broker=celery_flask.config['CELERY_BROKER_URL'])
celery.conf.update(celery_flask.config)


@celery.task
def send_async_email():
    with celery_flask.app_context():
        x = 0
        for i in range(5):
            time.sleep(3)
            x = x + i
        return x


@celery_flask.route('/')
def index():
    res = send_async_email.delay()
    return 'Ass'


if __name__ == '__main__':
    celery_flask.run(debug=True)
