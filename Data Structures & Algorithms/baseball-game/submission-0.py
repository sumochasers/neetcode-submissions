class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res_stack = []
        for entry in operations :
            if entry == "+" :
                b = res_stack.pop()
                a = res_stack.pop()
                c = int(a) +  int(b) 
                res_stack.append(a)
                res_stack.append(b)
                res_stack.append(str(c))
            elif entry == 'C':
                res_stack.pop()
            elif entry == 'D' :
                a = res_stack[-1]
                a = 2 * int(a)
                res_stack.append(str(a))
            else :
                res_stack.append(entry)
        print(res_stack)
        res = 0
        for num in res_stack:
            res += int(num)
        
        return res
