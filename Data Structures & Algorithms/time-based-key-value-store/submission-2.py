class TimeMap:

    def __init__(self):
        self.cache = defaultdict(dict)
        self.timecache = defaultdict(list)        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.cache[key][timestamp] = value
        self.timecache[key].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        times = self.timecache[key]
        l = 0
        r = len(times) - 1

        if not times or timestamp < times[l]: return ""

        while l <= r:
            m = l + (r-l) // 2

            if times[m] <= timestamp:
                l = m+1
                res = self.cache[key][times[m]]
            elif times[m] > timestamp:
                r = m - 1
            else:
                return self.cache[key][times[m]]

        return res
