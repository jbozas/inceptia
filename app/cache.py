import time


class SimpleCache:
    def __init__(self):
        self.cache = {}
        self.ttl = 60

    def set(self, key, value, ttl=None):
        expiry_time = time.time() + (ttl or self.ttl)
        self.cache[key] = {"value": value, "expiry": expiry_time, "time_requested": 1}

    def get(self, key):
        if key in self.cache:
            entry = self.cache[key]
            if entry["expiry"] is None or entry["expiry"] > time.time():
                self.cache[key]["time_requested"] += 1
                return entry["value"], entry["time_requested"]
            else:
                del self.cache[key]
        return None
