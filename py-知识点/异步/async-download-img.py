from time import time

import aiohttp
import asyncio



async def download(s,u):
    print(u, time())
    async with s.get(u, verify_ssl=False) as r:
        c = await r.content.read()

        name = u.rsplit("/")[-1]

        with open(name, mode="wb") as f:
            f.write(c)


async def main():
    async with aiohttp.ClientSession() as s:
        ul = [
            "http://i2.hdslb.com/bfs/face/c89d1193fc8be86373ec8877082a63c607200c77.jpg",
            "https://i0.hdslb.com/bfs/article/3add111d66f493f10bb256d03e52800fd54f3c9a.jpg",
            "https://i0.hdslb.com/bfs/article/fac583b1e849cda74e6ee55319b4834a2d0de489.png"
        ]

        tasks = [asyncio.create_task(download(s,u)) for u in ul]

        await asyncio.wait(tasks)

if __name__ == '__main__':
    asyncio.run(main())