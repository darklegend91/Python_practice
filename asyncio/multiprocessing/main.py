# import time , multiprocessing , atexit
# from concurrent.futures import ProcessPoolExecutor

# import requests

# session : requests.Session

# def main():
#     sites  = [
#         "https://www.jpython.com",
#         "https://realpython.com/courses/creating-dice-roll-application"
#     ] * 80
    
#     start_time = time.perf_counter()
#     download_all_sites(sites)
#     duration = time.perf_counter()
#     print(f"Downloaded {len(sites)} sites in {duration} seconds")

# def download_all_sites(sites):
#     with ProcessPoolExecutor(initializer= init_process) as executor:
#         executor.map(doanload_site , sites)


# def doanload_site(url):
#     with session.get(url) as response:
#         name = multiprocessing.current_process().name
#         print(f"{name}:Read {len(response.content)} bytes from {url}")
        
# def init_process():
#     global session
#     session = requests.Session()
#     atexit.register(session.close)

# if __name__ == "__main__":
#     main()
import asyncio

def hello_world(loop):
    """A callback to print 'Hello World' and stop the event loop"""
    print('Hello World')
    loop.stop()

loop = asyncio.new_event_loop()

# Schedule a call to hello_world()
loop.call_soon(hello_world, loop)

# Blocking call interrupted by loop.stop()
try:
    loop.run_forever()
finally:
    loop.close()