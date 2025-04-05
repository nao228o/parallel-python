from concurrent.futures import ThreadPoolExecutor, as_completed
import requests

def download_file(url):
    response = requests.get(url)
    return response.content

urls = [
    'https://www.google.com',
    'https://www.python.org',
    'https://www.github.com',
]

with ThreadPoolExecutor(max_workers=3) as executor:
    futures = [executor.submit(download_file, url) for url in urls]
    for future in as_completed(futures):
        print(future.result())
