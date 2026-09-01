class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

       
        def getTimeTaken(rate):
            total_time = 0
            
            for pile in piles :
                
                split_per_pile = (pile//rate) + (1 if (pile%rate) !=0 else 0) 
                time_taken =  split_per_pile 
                total_time += time_taken
            
            return  total_time   

        '''
        max_value = max(piles)
        
        for rate in range(1,max_value+1):
            
            total_time = getTimetaken(rate)
            
            if total_time <= h  :
                print(rate) 
                return rate 
        '''

        left = 1
        right = max(piles) 
        last_best_rate = -1
        
        while left <= right :
            
            mid = (left + right) // 2
            
            print("Mid - ", mid)
            time_taken = getTimeTaken(mid)
            print("Time taken - ",time_taken)
            
            iscompleted = False
            if time_taken <= h :
                iscompleted = True
                last_best_rate = mid

            if iscompleted :
                right = mid - 1
            else :
                left = mid + 1    

        
        return last_best_rate

                 

           
        
          
        