class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for x in asteroids :
            stack.append(x)
            while len(stack) >= 2 and stack[-1] < 0 and stack[-2] > 0 :
                if abs(stack[-1]) > abs(stack[-2]) :
                    last = stack.pop()
                    stack.pop()
                    stack.append(last)
                elif abs(stack[-1]) == abs(stack[-2]):
                    stack.pop()
                    stack.pop()
                else :
                    stack.pop()
        
        return stack