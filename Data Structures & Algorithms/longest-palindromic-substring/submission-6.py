class Solution:
    def longestPalindrome(self, s: str) -> str:
        # maxLen = 0
        # maxI,maxJ = -1, -1
        # for i in range(len(s)-1):
        #     for j in range(i+1, len(s)):
        #         if s[i:j+1] == s[i:j+1][::-1] :
        #             if j-i+1 > maxLen :
        #                 maxI = i
        #                 maxJ = j
        #                 maxLen = j-i+1
        # return s[maxI:maxJ+1]
        n = len(s)
        states = [[False] * n for _ in range(n)]
        maxI = 0
        maxJ = 0
        maxLen = 0 
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[j] == s[i] and ((j - i + 1) <= 3 or
                                    states[i + 1][j - 1]
                                    ) :
                    states[i][j] = True
                    if j - i + 1 > maxLen :
                        maxI = i 
                        maxJ = j
                        maxLen = j - i + 1 
        
        return s[maxI:maxJ+1]


        
        