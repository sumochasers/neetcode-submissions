class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        '''
        max_length = 0
        for l in range(len(s)):

            count = {}
            max_f = 0
            
            for r in range(l,len(s)):

                count[s[r]] = 1 + count.get(s[r],0)
                max_f = max(max_f, count[s[r]])
                if (r - l + 1) - max_f  <= k :
                    max_length = max(max_length,(r - l + 1))
     
        print(max_length)
        return max_length
        '''
        
        count = {}
        maxF = 0
        l = 0
        max_len = 0
        for r in range(len(s)):

            count[s[r]] = 1 + count.get(s[r],0)
            maxF = max(maxF,count[s[r]])

            while (r-l+1) - maxF > k :
                count[s[l]] = count[s[l]] - 1
                l += 1
            
            max_len  = max(r-l+1, max_len)
        
        print(max_len)
        return max_len    

