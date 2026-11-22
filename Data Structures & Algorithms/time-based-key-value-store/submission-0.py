class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key] = self.store.get(key, []) + [(value, timestamp)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        li = self.store[key]
        low, high = 0, len(li)-1
        res = ""
        while low<=high:
            mid = low + (high-low)//2
            if li[mid][1] <= timestamp:
                res = li[mid][0]
                low = mid + 1
            else:
                high = mid-1
        return res