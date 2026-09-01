class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        
        #Sliding window

        t_freq = Counter(t)
        w_freq = {}
        
        need = len(t_freq)
        have = 0

        l = 0 
        min_length = 999999999
        min_ptr = [-1,-1]
        for r in range(len(s)):
            
            w_freq[s[r]] = 1 + w_freq.get(s[r], 0)
            
            if s[r] in t_freq and w_freq[s[r]] == t_freq[s[r]]:
                have += 1
            
            while have == need :
                if (r-l+1) < min_length :
                    min_ptr[0] = l
                    min_ptr[1] = r
                    min_length = r-l+1
                
                w_freq[s[l]] -= 1
                if s[l] in t_freq and w_freq[s[l]] < t_freq[s[l]]:
                    have -= 1
                l += 1
        
        if min_ptr[1] != -1 :
            return s[min_ptr[0]:min_ptr[1]+1]
        else:
            return ""



            


        
        # Brute force 
        # min_start_pos = -1
        # min_end_pos = -1
        # min_length = 9999999
        # for i in range(len(s)):
        #     start_pos = -1
        #     final_pos = -1
        #     freq = Counter(t)
        #     for j in range(i,len(s)):
        #         if s[j] in freq :
        #             if start_pos == -1 :
        #                start_pos = j 
        #             freq[s[j]] -= 1
        #             if freq[s[j]] == 0 :
        #                 freq.pop(s[j])
        #             if not freq :
        #                 final_pos = j
        #                 if min_length > (final_pos - start_pos + 1) :
        #                     min_length = final_pos - start_pos + 1
        #                     min_start_pos = start_pos
        #                     min_end_pos = final_pos
        #                 break
        
        # if min_end_pos != -1 :
        #     return s[min_start_pos : min_end_pos +1]
        # else :
        #     return ""


        
        # brute force with same
        # last_min = 99999999
        # min_fpos = -1
        # min_lpos = -1
        # for j in range(len(s)):
        #     t_pos = 0
        #     f_pos = -1
        #     l_pos = -1
        #     count = 0
        #     for i in range(j,len(s)):
        #         if s[i] == t[t_pos]:
        #             if f_pos == -1 :
        #                 f_pos = i
        #             count += 1
        #             if count == len(t):
        #                 l_pos = i
        #                 if  last_min > (l_pos-f_pos+1) :
        #                     last_min = l_pos-f_pos+1
        #                     min_fpos = f_pos
        #                     min_lpos = l_pos
        #                 break
        #             t_pos += 1
        
        # if min_lpos != -1 :
        #     return s[min_fpos:min_lpos+1]
        # else :
        #     return ""
            




            
        