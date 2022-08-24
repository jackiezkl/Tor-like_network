import time

begin = time.perf_counter()
time.sleep(3)
end = time.perf_counter()
print(f"{end - begin:0.6f}")
