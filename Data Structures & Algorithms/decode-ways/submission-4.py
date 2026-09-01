class Solution:
    
    def getCountDfs(self, i, s, cache):
        if i == len(s):
            return 1
        if s[i] == '0':
            return 0
        if i in cache :
            return cache[i]
        
        totalCount = self.getCountDfs(i+1, s, cache)
        if i + 1 < len(s) :
            if s[i] == '1' or (s[i] == '2' and (s[i + 1] in "0123456")) :
                totalCount += self.getCountDfs(i + 2, s, cache) 
        cache[i] = totalCount
        return cache[i]


    def numDecodings(self, s: str) -> int:
        cache = {}
        return self.getCountDfs(0, s, cache)
        