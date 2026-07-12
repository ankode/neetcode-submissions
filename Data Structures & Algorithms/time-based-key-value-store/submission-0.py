class TimeMap:

    def __init__(self):
        self.timemap = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timemap:
            self.timemap[key] = []
        self.timemap[key].append((timestamp,value))
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timemap:
            return ""

        left = 0
        ans = None
        right =  len(self.timemap[key]) - 1
        while left <= right:
            mid = left + (right - left) // 2
            time, val = self.timemap[key][mid]
            if time == timestamp:
                return val
            
            if  time < timestamp:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return  self.timemap[key][ans][1] if ans is not None else ""