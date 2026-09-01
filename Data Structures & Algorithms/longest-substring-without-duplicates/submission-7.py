'''
    xzyzxy
    

    xxxx

'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        visited = set()
        l = 0 
        max_len = 0
        
        for r in range(len(s)):   # 0 1 2 3
            if s[r] in visited :
                while s[r] in visited :
                    visited.remove(s[l])
                    l += 1
            
            visited.add(s[r])
            max_len = max(max_len, r-l+1)
        
        return  max_len   




        
        #brute force
        max_length = 1 if len(s) > 0 else 0
        for i in range(0,len(s)): # O(n)
            visited = set()
            visited.add(s[i])
            length = 1
            
            for j in range(i+1,len(s)): # O(n2)
                if s[j] in visited :
                    break
                else :
                    length += 1 
                    print(length)
                    visited.add(s[j])  
                    max_length = max(length,max_length)    
        
        return  max_length     

        