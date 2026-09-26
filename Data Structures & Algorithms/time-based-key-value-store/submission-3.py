class TimeMap:

    def __init__(self):
        self.cache = defaultdict(dict)
        self.timecache = defaultdict(list)        

    def set(self, key: str, value: str, timestamp: int) -> None:
        # for each key, store timestamp : value
        self.cache[key][timestamp] = value
        # store all timestamps for each key sequentially => ensures sorted property
        self.timecache[key].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        times = self.timecache[key]
        # search space is each keys array of times. Goal is to find the value at each timestamp or the next previous time if does not exist
        l = 0
        r = len(times) - 1

        # edge case: no times or timestamp smaller than the smallest time => return empty string
        if not times or timestamp < times[l]: return res

        while l <= r:
            m = l + (r-l) // 2

            # this is a valid result since time <= timestamp, so we update res here
            if times[m] <= timestamp:
                l = m + 1
                res = self.cache[key][times[m]]
            # invalid time since > timestamp. search LHS
            elif times[m] > timestamp:
                r = m - 1
            else:
                return self.cache[key][times[m]]

        return res
