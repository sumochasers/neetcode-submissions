class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        
        change  : dict[int, int]= {5:0,
        10 : 0,
        20 : 0}
        
        def is_available(balance):

            while balance > 0 :
                if change[20] and balance >= 20 :
                    change[20] -= 1
                    balance -= 20
                elif change[10] and balance >= 10 :
                    change[10] -= 1
                    balance-= 10
                elif change[5] and balance >= 5 :
                    change[5] -= 1
                    balance -= 5
                else : 
                    return False
            return True
            

        for bill in bills :
            balance = bill - 5
            if not is_available(balance):
                return False
            change[bill] += 1 
        return True
            
        