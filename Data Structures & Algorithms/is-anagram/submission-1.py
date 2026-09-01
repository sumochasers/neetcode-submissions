class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        frequency_arr = [0] * 26
        for i in range(len(t)):

            frequency_arr[ord(s[i]) - ord('a')] +=1
            frequency_arr[ord(t[i]) - ord('a')] -=1

        for i in frequency_arr :
            if i != 0 :
                return False
        
        return True




        

        