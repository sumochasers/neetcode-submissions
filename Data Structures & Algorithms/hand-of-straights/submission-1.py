class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        # if len(hand) % groupSize != 0 :
        #     return False

        # hand.sort()
        # while hand :
        #     start = hand.pop(0)
        #     for i in range(groupSize-1):
        #         next = start+1
        #         if next not in hand :
        #             return False
        #         hand.remove(next)
        #         start = next 
        
        # return True  
        
        '''
        11223344
        12345678
        '''

        if len(hand) % groupSize :
            return False
        
        hand.sort()

        freq = Counter(hand)
        for num in hand :
            if freq[num] :
                for targetNum in range(num, num + groupSize):
                    if not freq[targetNum]:
                        return False
                    freq[targetNum] -= 1
        return True
                


        
            
                

        