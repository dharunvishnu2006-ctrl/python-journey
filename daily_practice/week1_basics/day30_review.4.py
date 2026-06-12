import functools
import time

@functools.lru_cache(maxsize=100)
def get_ip_reputation(ip):
    print(f"Scanning {ip}...")
    time.sleep(1) 
    return f"{ip} — Reputation: MALICIOUS"
start = time.time()

print(get_ip_reputation("192.168.1.1"))
print(get_ip_reputation("192.168.1.1"))
print(get_ip_reputation("192.168.1.1"))
print(get_ip_reputation("10.0.0.1"))

end = time.time()
print(f"\nTotal time: {end - start:.2f} seconds")

print("Cache Info:", get_ip_reputation.cache_info())