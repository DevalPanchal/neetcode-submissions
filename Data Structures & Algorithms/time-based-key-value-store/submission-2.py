class TimeMap:

    def __init__(self):
        self.tmap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.tmap:
            self.tmap[key] = []
        self.tmap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        values = self.tmap[key] if key in self.tmap else []
        result = ""
        low = 0
        high = len(values) - 1

        while low <= high:
            mid = (low + high) // 2
            if values[mid][0] <= timestamp:
                result = values[mid][1]
                low = mid + 1
            else:
                high = mid - 1

        return result
        
