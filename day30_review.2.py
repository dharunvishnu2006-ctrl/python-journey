import threading
import time

def analyze_log(log_name):
    print(f"Analyzing {log_name}...")
    time.sleep(1)
    print(f"{log_name} — No threats found!")

start = time.perf_counter()

t1 = threading.Thread(target=analyze_log, args=("firewall.log",))
t2 = threading.Thread(target=analyze_log, args=("access.log",))
t3 = threading.Thread(target=analyze_log, args=("error.log",))

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

end = time.perf_counter()
print(f"All logs parsed in {end-start:.2f} seconds!")