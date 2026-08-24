import time
import asyncio , aiohttp

async def main():
    sites = [
        "https://www.jpython.org",
        "https://realpython.com/courses/creating-dice-roll-application/"
    ] * 80

    start_time = time.perf_counter()
    await download_all_sites(sites)
    duration = time.perf_counter() - start_time

    print(f"Downloaded {len(sites)} sites in {duration:.2f} seconds")

async def download_all_sites(sites):
    async with aiohttp.ClientSession() as session:
        tasks = [download_site(url , session) for url in sites]
        await asyncio.gather(*tasks , return_exceptions= True)

async def download_site(url, session):
    async with session.get(url) as response:
        print(f"Read {len(await response.read())} bytes from {url}")

if __name__ == "__main__":
    asyncio.run(main())