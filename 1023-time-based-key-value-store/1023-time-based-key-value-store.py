from sortedcontainers import SortedDict
class TimeMap:
    # in linear this code causes TLE
    def __init__(self):
        self.key_val = defaultdict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        # if not in dict
        if key not in self.key_val:
            self.key_val[key] = SortedDict()
        
        self.key_val[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        # if key does not exist in dict
        if key not in self.key_val:
            return ""
        
        i = self.key_val[key].bisect_right(timestamp)

        if i == 0:
            return ""

        return self.key_val[key].peekitem(i-1)[1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)