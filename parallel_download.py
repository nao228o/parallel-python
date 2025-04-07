from concurrent.futures import ThreadPoolExecutor, as_completed, Future
import requests

def download_file(url) -> bytes | None:
    try:
        response: requests.Response = requests.get(url)
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
    futures: list[Future[bytes | None]] = [executor.submit(download_file, url) for url in urls]
    for future in as_completed(futures):
        result: bytes | None = future.result()
        if result:
            print(result)
        else:
            print("Failed to download")
