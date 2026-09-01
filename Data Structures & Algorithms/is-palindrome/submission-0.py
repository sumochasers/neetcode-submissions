class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        start = 0
        end = len(s) - 1

        while end >= start :

            while s[start].isalnum() != True and start < end  :
                start += 1
            
            while s[end].isalnum() != True and end  > start :
                end -= 1
            
            if s[start].lower() != s[end].lower() :
                return False        
            
            start += 1
            end -=1

        return True

        
        '''
        alphanum_str = ""

        for ch in s :
            if ch.isalnum():
                alphanum_str += ch.lower()
        print(alphanum_str)

        return alphanum_str == alphanum_str[::-1]  '''  
        