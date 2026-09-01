class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        if len(hand) % groupSize != 0 :
            return False

        hand.sort()
        while hand :
            start = hand.pop(0)
            for i in range(groupSize-1):
                next = start+1
                if next not in hand :
                    return False
                hand.remove(next)
                start = next 
        
        return True  
        
            
                

        