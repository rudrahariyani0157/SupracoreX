import time

for i in range(10, -1, -1):
    print(f"\r{i}", end="", flush=True)
    time.sleep(1)