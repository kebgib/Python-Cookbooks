"""
A simple runtime calculation cookbook
So simple this file has no comments.
"""

from time import perf_counter
from time import sleep

start = perf_counter()
sleep(20)
end = perf_counter()


runtime = round(end - start)
runtime_mins, runtime_seconds = divmod(runtime, 60)

print(f"[*] Global runtime {runtime_mins} minutes {runtime_seconds} seconds")

