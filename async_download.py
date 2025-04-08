import asyncio
import aiohttp

async def download_file(url):
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url) as response:
                response.raise_for_status()
                return await response.read()
        except aiohttp.ClientError as e:
            print(f"Error downloading {url}: {e}")
            return None

urls = [
    'https://www.google.com',
    'https://www.python.org',
    'https://www.github.com',
]

async def main():
    tasks = [download_file(url) for url in urls]
    results = await asyncio.gather(*tasks)
    for result in results:
        if result:
            print(result)
        else:
            print("Failed to download")

if __name__ == "__main__":
    asyncio.run(main()) 