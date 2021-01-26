import pandas as pd
import numpy as np
import time


def calc_RSI(upPrices, downPrices):
    np_upPrices = np.array(upPrices)
    np_downPrices = np.array(downPrices)

    AvgUp = np.sum(np_upPrices) / 15
    AvgDw = np.sum(np_downPrices) / 15

    RS = AvgUp / AvgDw

    RSI = 100 - (100 / (1 + RS))

    print(RSI)


# def load_csv():
#     prices = []
#     data = pd.read_csv('price_csv_list.csv')
#     prices.append(data['latest_price'])
#
#     return prices

prices = []
data = pd.read_csv('price_csv_list.csv')
prices.append(data['latest_price'])



#  Loop to hold up and down price movements
while True:
    prices = []
    data = pd.read_csv('price_csv_list.csv')
    prices.append(data['latest_price'])

    upPrices = []
    downPrices = []

    if len(prices[0]) == 15:
        i = 0
        while i < 15:
            if i != 0:
                if (prices[0][i] - prices[0][i - 1]) > 0:
                    upPrices.append(prices[0][i])
                elif (prices[0][i] - prices[0][i - 1]) < 0:
                    downPrices.append(prices[0][i])
            if i == 14:
                calc_RSI(upPrices, downPrices)
                time.sleep(305)

            i += 1




# print(len(prices[0]))


# i = 0
# upPrices=[]
# downPrices=[]
# #  Loop to hold up and down price movements
# while i < len(prices[0]):
#     if i != 0:
#         if (prices[0][i]-prices[0][i-1])>0:
#             upPrices.append(prices[0][i])
#         elif(prices[0][i]-prices[0][i-1])<0:
#             downPrices.append(prices[0][i])
#     if(i==14):
#       calc_RSI(upPrices,downPrices)
#       time.sleep(26)
#       i=-1
#     i += 1


# # print("upPrices:",upPrices)
# # print("RSI:",RSI)
