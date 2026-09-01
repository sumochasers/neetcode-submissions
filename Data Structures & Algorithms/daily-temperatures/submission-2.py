class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):

            while stack and stack[-1][1] < temp :
                last = stack.pop()
                no_days = i - last[0]
                res[last[0]] =  no_days
            
            stack.append((i, temp))
        
        return res 

        