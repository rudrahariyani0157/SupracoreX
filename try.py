import time

for i in range(100, -1, -1):
    print(f"\r{i:03d}", end="", flush=True)
    time.sleep(1)

print()