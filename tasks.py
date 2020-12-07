# tasks.py celery application
import time

from celery import Celery

app = Celery('tasks', backend='rpc://', broker='amqp://admin:admin@localhost/myvhost')
app.conf.update(
    task_serializer='json',
    accept_content=['json'],  # Ignore other content
    result_serializer='json',
    timezone='Europe/Oslo',
    enable_utc=True,
    result_backend='rpc://',
    result_persistent=True
)


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # Calls test('hello') every 10 seconds.
    # sender.add_periodic_task(3.0, test.s, name='add every 10')
    sender.add_periodic_task(3.0, test, name='add every 10')


#
#
@app.on_after_configure.connect
def setup_periodic_tasks_multi(sender, **kwargs):
    # Calls test('hello') every 10 seconds.
    sender.add_periodic_task(2.0, p, name='add every 10')
    #sender.add_periodic_task(2.0, test, name='add every 10')


@app.task
def test():
    global x
    x = 10
    print("Pussy")


@app.task
def p():
    print('Ass')


@app.task
def pr1():
    return 'Asshole'

# @app.task
# def add(x, y):
#         return x * y
#
#
# @app.task
# def addit(x, y):
#     return x + y
