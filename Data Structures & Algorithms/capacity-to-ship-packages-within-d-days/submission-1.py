class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        '''
        1, 2, 3, 4, 4, 5
        1, 5
        2, 4
        4, 3
        '''

        def can_ship(weight : int) -> bool :
            ships = 1
            max_weight = weight
            
            for w in weights :
                if max_weight - w < 0 :
                    ships += 1
                    max_weight = weight
                max_weight -= w
            
            if ships <= days :
                return True
            
            return False
        
        l = max(weights) 
        r = sum(weights) 
        ans = -1
        while l <= r :
            m = (l + r) // 2
            if can_ship(m):
                ans = m
                r = m - 1
            else :
                l = m + 1 
        
        return ans
