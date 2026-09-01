class Solution:
    '''
        XYYX and k = 2
        {X,Y}
        


    
    '''
    
    def characterReplacement(self, s: str, k: int) -> int:
        
        l = 0 
        r = 0
        freq = {}
        res = 0
        maxf = 0
        while r < len(s):
            freq[s[r]] = 1 + freq.get(s[r],0)
            maxf = max(maxf,freq[s[r]])
            
            while (r-l+1) - maxf > k :
                freq[s[l]] -= 1 
                l += 1 
            
            res = max(res,r-l+1)   
            r += 1 
        
        return res        

        

        '''
        #Brute Force
        res = 0 
        for i in range(len(s)):  # 0 1 2 3 
            freq = {}
            maxf = 0
            for j in range(i,len(s)): # 0 1 2 3
               freq[s[j]] = 1 + freq.get(s[j],0)
               maxf = max(maxf,freq[s[j]])
               if ((j-i+1) - maxf) <= k :
                    res = max(res,j-i+1) 

        return res
        '''

        


          

       


        