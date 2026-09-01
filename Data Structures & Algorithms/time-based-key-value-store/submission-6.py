class TimeMap:

    def __init__(self):
        self.valueByKey = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.valueByKey[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        targetList = self.valueByKey[key]
        print(targetList)
        if not targetList :
            return ""
        l, r = 0, len(targetList) - 1
        res = ""
        while l <= r :
            mid = ( l + r ) // 2
            midTimestamp = targetList[mid][1]
            if midTimestamp <= timestamp :
                res = targetList[mid][0]
                l = mid + 1
            else :
                r = mid - 1

        return res
        

        

