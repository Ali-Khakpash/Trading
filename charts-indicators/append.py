import datetime
import requests
import json
import time
import pandas as pd
import csv
from csv import DictWriter


def insert_row():
    r = requests.post('https://api.nobitex.ir/market/stats', json={"srcCurrency": "btc", "dstCurrency": "rls"})
    dics = json.loads(r.text)
    current_datetime = datetime.datetime.now()
    latest_price = dics['stats']['btc-rls']['latest']

    field_names = ['latest_price', 'current_datetime']
    dicts = {'latest_price': latest_price, 'current_datetime': current_datetime}

    with open('price_csv_list.csv', 'a') as f_object:
        dictwriter_object = DictWriter(f_object, fieldnames=field_names)
        dictwriter_object.writerow(dicts)
        f_object.close()


def remove_first_line():
    with open('price_csv_list.csv', 'r') as readFile:
        reader = csv.reader(readFile)
        data = list(reader)
        data.pop(1)

    with open('price_csv_list.csv', 'w') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(data)


while (True):
    prices = []
    data = pd.read_csv('price_csv_list.csv')
    prices.append(data['latest_price'])

    # if(len(prices[0]==15)):
    #     break
    # else:
    #     insert_row()
    #     time.sleep(7)

    if (len(prices[0]) == 15):
        break
    else:
        insert_row()
        time.sleep(300)

while(True):
      remove_first_line()
      insert_row()

      time.sleep(300)


# i = 0
# while (True):
#   if(i<15):
#       # remove_first_line()
#       # i = 0
#       r = requests.post('https://api.nobitex.ir/market/stats', json={"srcCurrency":"btc","dstCurrency":"rls"})
#       dics = json.loads(r.text)
#       current_datetime = datetime.datetime.now()
#       latest_price = dics['stats']['btc-rls']['latest']

#       field_names = ['latest_price', 'current_datetime']
#       dicts = {'latest_price':latest_price, 'current_datetime':current_datetime}

#       with open('price_csv_list.csv', 'a') as f_object:
#           dictwriter_object = DictWriter(f_object, fieldnames=field_names)
#           dictwriter_object.writerow(dicts)
#           f_object.close()

#       # price_csv_list = pd.DataFrame([[str(latest_price),str(current_datetime)]], columns=['latest_price','current_datetime'])
#       # price_csv_list.to_csv('price_csv_list.csv',mode='a', header=False, index=False)

#       time.sleep(300)
#       i+=1
#   else:
#       remove_first_line()
#       r = requests.post('https://api.nobitex.ir/market/stats', json={"srcCurrency":"btc","dstCurrency":"rls"})
#       dics = json.loads(r.text)
#       current_datetime = datetime.datetime.now()
#       latest_price = dics['stats']['btc-rls']['latest']

#       field_names = ['latest_price', 'current_datetime']
#       dicts = {'latest_price':latest_price, 'current_datetime':current_datetime}

#       with open('price_csv_list.csv', 'a') as f_object:
#           dictwriter_object = DictWriter(f_object, fieldnames=field_names)
#           dictwriter_object.writerow(dicts)
#           f_object.close()

#       # price_csv_list = pd.DataFrame([[str(latest_price),str(current_datetime)]], columns=['latest_price','current_datetime'])
#       # price_csv_list.to_csv('price_csv_list.csv',mode='a', header=False, index=False)

#       time.sleep(300)