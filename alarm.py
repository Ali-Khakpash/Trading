# alarm.py

import asyncio
import requests

global last_price

async def count():
    while(True):
        r = requests.get('https://api-pub.bitfinex.com/v2/tickers?symbols=tBTCUSD')
        res = r.json()
        last_price = res[0][7]
        print(last_price)
        await asyncio.sleep(2)



async def fn1():
        if 'last_price' in globals():
            print('this is second fn'+str(last_price))

async def main():
    await asyncio.gather(fn1() , count())

if __name__ == "__main__":
    import time
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")
