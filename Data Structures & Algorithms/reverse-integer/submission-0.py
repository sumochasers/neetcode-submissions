class Solution:
    def reverse(self, x: int) -> int:
        org = x
        val = abs(x)
        num = int(str(val)[::-1])

        if org < 0 :
            num *= -1
        if num < -(1 << 31) or num >= (1 << 31) :
            return 0
        
        return num
        