from concurrent.futures import ThreadPoolExecutor, as_completed
import requests

def download_file(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # エラーが発生した場合に例外を発生させる
        return response.content
    except requests.exceptions.RequestException as e:
        print(f"Error downloading {url}: {e}")
        return None

urls = [
    'https://www.google.com',
    'https://www.python.org',
    'https://www.github.com',
]

with ThreadPoolExecutor(max_workers=3) as executor:
    futures = [executor.submit(download_file, url) for url in urls]
    for future in as_completed(futures):
        print(future.result())
