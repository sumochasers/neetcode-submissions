class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # String of characters
        # Example zxyzy
        #

        l,r = 0,0
        sequence_chars = set()
        length = 0
        while r < len (s)  :

            if s[r] in sequence_chars :
                
                while s[r] in sequence_chars :
                    sequence_chars.remove(s[l])
                    l += 1
            
            sequence_chars.add(s[r])
            length = max(length, r - l + 1)
            r += 1
            
        
        print(length)    
        return length









        