class Solution:

    def encode(self, strs: List[str]) -> str:

        res = ""
        delimiter = "#"
        for val in strs :
            count = len(val)
            res += str(count)+delimiter+val

        print(res)
        return res    

    def decode(self, s: str) -> List[str]:
        
        ptr = 0
        res = []
        while ptr < len(s) :
            
            length_str = ""
            
            while s[ptr] != '#':
                length_str += s[ptr]
                ptr = ptr+1

            length = int(length_str)
            start = ptr+1
            end = ptr+length+1
            word = s[ start : end]
            print(word)
            res.append(word)
            ptr = end

        print("final", res)
        return res    


       
        
            


