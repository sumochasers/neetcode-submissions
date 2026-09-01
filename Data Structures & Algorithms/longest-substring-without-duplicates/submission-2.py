'''
    zxyzxy
    

    xxxx

'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        max_length = 1 if len(s) > 0 else 0
        for i in range(0,len(s)):
            visited = set()
            visited.add(s[i])
            length = 1
            
            for j in range(i+1,len(s)):
                if s[j] in visited :
                    break
                else :
                    length += 1 
                    print(length)
                    visited.add(s[j])  
                    max_length = max(length,max_length)    
        
        return  max_length     

        