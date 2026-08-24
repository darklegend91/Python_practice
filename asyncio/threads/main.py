# import threading , time

# max_count = 5000
# counter = 0
# lock = threading.Lock()

# def count_to(max_count):
#     global counter
    
#     for _ in range(max_count):
#         lock.acquire()
#         tmp = counter
#         tmp += 1
#         time.sleep(0.000001)
#         counter = tmp
#         lock.release()
        
# t1 = threading.Thread(target = count_to , args =(max_count, ))
# t2 = threading.Thread(target = count_to , args =(max_count, ))

# # Start threads
# t1.start()
# t2.start()

# # Wait threads to finish
# t1.join()
# t2.join()

# print(f"Counting done , reached {counter}")


import threading
import time

MAX_COUNT = 50000000
NUM_THREADS = 32
MS_PER_S = 1000


# Mock some CPU-heavy operation, i.e. simply count up to max_count.
def count_to(max_count):
    counter = 0
    for _ in range(int(max_count)):
        counter += 1

t_start = time.time()

# Create NUM_THREADS threads, append to list and start them.
threads = []
for _ in range(NUM_THREADS):
    t = threading.Thread(target=count_to, args=(MAX_COUNT / NUM_THREADS,))
    threads.append(t)
    t.start()

# Join all threads.
for t in threads:
    t.join()

print(f"Execution done, time elapsed [ms]: {(time.time() - t_start) * MS_PER_S}")