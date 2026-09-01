class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        # Brute force - Unintuitive
        r = len(temperatures) - 1
         
        res = [0] * len(temperatures)
        
        while r > 0 :

            current = temperatures[r]
            r2 = r -1
            day = 1
            while r2 >= 0 and temperatures[r2] < current   :
                res[r2] = day
                day += 1
                r2 -= 1
            r -=1     
    
        print(res)
        return res


