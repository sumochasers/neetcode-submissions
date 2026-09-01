class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        s1_freq_list = list(s1)
        s2_left = 0
        s2_right = 0
        start_pos = 0 
        while s2_right < len(s2) and start_pos < len(s2) :
            print(s2[s2_right])
            if s2[s2_right] in s1_freq_list :
                s1_freq_list.remove(s2[s2_right])
            else :   
                s1_freq_list = list(s1)
                start_pos += 1
                s2_right = start_pos
                continue
            
            if len(s1_freq_list) == 0 :
                return True
            s2_right += 1

        return False    


        

            
        