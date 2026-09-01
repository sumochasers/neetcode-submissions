class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        
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