import pandas as pd
import numpy as np
import time


def calc_RSI(upPrices,downPrices):
    np_upPrices = np.array(upPrices)
    np_downPrices = np.array(downPrices)

    AvgUp = np.sum(np_upPrices)/15
    AvgDw = np.sum(np_downPrices)/15

    RS = AvgUp/AvgDw

    RSI = 100 - (100/(1+RS))

    print(RSI)






prices = []
data = pd.read_csv('price_csv_list.csv')

prices.append(data['latest_price'])


# print(len(prices[0]))


# continue statement
i=-1
while(i<100):
    i+=1
    if(i<10):
        continue
    print(i)
    time.sleep(2)


# i = 0
# upPrices=[]
# downPrices=[]
# #  Loop to hold up and down price movements
# while (True):
#     if(len(prices[0])==15):
#         # if i != 0:
#         #     if (prices[0][i]-prices[0][i-1])>0:
#         #         upPrices.append(prices[0][i])
#         #     elif(prices[0][i]-prices[0][i-1])<0:
#         #         downPrices.append(prices[0][i])
#         # if(i==14):
#         #     calc_RSI(upPrices,downPrices)
#         #     time.sleep(8)
#         #     i=-1
#         # i+=1
#         print('ass')



# if(len(prices[0])==15):
#   print('ass')














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