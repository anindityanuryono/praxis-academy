import asyncio

async def main():
    print('Hi ...')
    await asyncio.sleep(1)
    print('... Prais Academy!')

# Python 3.7+
asyncio.run(main())