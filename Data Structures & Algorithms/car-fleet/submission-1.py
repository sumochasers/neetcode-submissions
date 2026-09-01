class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        '''
        [[7,1],[4,2],[1,2],[0,1]]
        [3,3,4,10]
        '''
        posSpeedPairs = []
        for i in range(len(position)):
            posSpeedPairs.append([position[i], speed[i]])
        
        posSpeedPairs.sort(key=lambda x : x[0], reverse=True)

        monStack = []
        for pos,speed in posSpeedPairs :
            time = (target - pos) / speed
            if not monStack or time > monStack[-1] :
                monStack.append(time)
        
        return len(monStack)

            
        