class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        res = ""
        
        carry = 0
        
        a, b = a[::-1], b[::-1]
        for i in range(max(len(a),len(b))):
            dA =   int(a[i]) if  i < len(a) else 0
            dB =   int(b[i]) if  i < len(b) else 0
            total = dA + dB + carry
            remainder = total % 2
            res = str(remainder) + res
            carry = total // 2

        
        if carry :
            res = "1" + res
        
        return res

            
        
        




