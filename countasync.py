# countasync.py

import asyncio

async def count():
    while(True):
        print("One")
        print("Two")
        await asyncio.sleep(3)

async def fn1():
	print("Asshole")

async def main():
    await asyncio.gather(count(),fn1())

if __name__ == "__main__":
    import time
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")
