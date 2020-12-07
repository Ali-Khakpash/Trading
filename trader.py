import time
import requests
from flask_mail import Mail, Message
from config import config

from flask import (Flask, render_template, make_response, request, after_this_request)

app = Flask(__name__, template_folder="templates")
app.config.from_object(config['development'])

from celery import Celery

celery = Celery('trader', backend=config['development'].CELERY_RESULT_BACKEND,
                broker=config['development'].CELERY_BROKER_URL)
# celery.conf.update(app.config.from_object(config['development']))
#celery.conf.update(app.config)

mail = Mail(app)


@app.route('/')
def hello():
    return render_template('alarm.html')


@app.route('/alarm', methods=['POST'])
def alarm():
    global above_price, below_price
    above_price = request.values.get('above-p')
    below_price = request.values.get('below-p')

    send_alarm_email.delay(above_price,below_price)

    return make_response(above_price)


@celery.task
def send_alarm_email(above_price,below_price):
    with app.app_context():
        doing = True
        above = True
        below = True

        while (doing):
            time.sleep(2)
            r = requests.get('https://api-pub.bitfinex.com/v2/tickers?symbols=tBTCUSD')
            res = r.json()
            global last_price
            last_price = res[0][7]

            if last_price and above_price and below_price:
                if above:
                    if last_price >= int(above_price):
                        msg = Message("Hello" + "BTC goes above" + above_price,
                                      sender="ali.khakpash@gmail.com",
                                      recipients=["enemyfront45@gmail.com"])
                        mail.send(msg)
                        above = False

                elif last_price <= int(below_price):
                    if below:
                        msg = Message("Hello" + "BTC goes below" + below_price,
                                      sender="ali.khakpash@gmail.com",
                                      recipients=["enemyfront45@gmail.com"])
                        mail.send(msg)
                        below = False

            if above==False and below==False:
               doing = False


if __name__ == '__main__':
    app.run()
