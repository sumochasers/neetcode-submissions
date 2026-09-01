class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrome(s):
            left = 0
            right = len(s) - 1

            while left < right :
                if s[left] != s[right] :
                    return False
                left += 1
                right -= 1
            return True
        
        left = 0
        right = len(s) - 1

        while left < right :
            if s[left] != s[right] :
                return is_palindrome(s[left:right]) or            is_palindrome(s[left+1:right+1])
            left += 1
            right -= 1
        
        return True


