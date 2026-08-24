import threading
import time
import requests
from concurrent.futures import ThreadPoolExecutor

thread_local = threading.local()

def main():
    sites = [
        "https://www.jpython.org",
        "https://realpython.com/courses/creating-dice-roll-application/"
    ] * 80

    start_time = time.perf_counter()
    download_all_sites(sites)
    duration = time.perf_counter() - start_time

    print(f"Downloaded {len(sites)} sites in {duration:.2f} seconds")

def download_all_sites(sites):
    with ThreadPoolExecutor(max_workers= 5) as executor:
        executor.map(download_site , sites)
    # with requests.Session() as session:
    #     for url in sites:
    #         download_site(url, session)

def download_site(url, session):
    session = get_session_for_thread()
    with session.get(url) as response:
        print(f"Read {len(response.content)} bytes from {url}")

def get_session_for_thread():
    if not hasattr(thread_local , "session"):
        thread_local.session = requests.Session()
    return thread_local.session

if __name__ == "__main__":
    main()