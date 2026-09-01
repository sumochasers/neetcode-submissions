'''

["10","6","9","3","+","-11","*","/","*","17","+","5","+"]

10 6 9 3 + -11 * / * 17 + 5 +

10 6 9 3 +
10 6 12 -11 *
10 6 -132 /

10 0 *
0 17 +
17 5 +
22






Division edge case - truncate towards zero

if operand == operation pop 2 values - Do the operation
else
    apppend the value

'''
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        result = []


        for operand in tokens :
            if operand == '*' or operand == '/' or operand == '+' or operand == '-' :
                operand2 = int(result.pop())
                operand1 = int(result.pop())
                if operand == '+' :
                    result.append(operand1+operand2)
                if operand == '-' :
                    result.append(operand1-operand2)
                if operand == '*' :
                    result.append(operand1*operand2)
                if operand == '/' :
                    res = int(operand1 / operand2)
                    result.append(res)

            else :
                result.append(int(operand))
            print(result)
        return result[0]
        