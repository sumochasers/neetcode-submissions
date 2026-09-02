class Solution:
    def decodeString(self, s: str) -> str:
        
        num_stack = []
        string_stack = []
        
        num = 0 
        curr = ""
        
        for ch in s :
            if ch.isdigit():
                num = num * 10 + int(ch)
            elif ch == '[':
                num_stack.append(num)
                string_stack.append(curr)
                num = 0
                curr = ""
            elif ch == ']' :
                prev_num = num_stack.pop()
                prev_str = string_stack.pop()
                curr = prev_str + (prev_num * curr)
            else :
                curr += ch
        
        return curr

