class Solution:

    def encode(self, strs: List[str]) -> str:
        
        res = ""
        for word in strs :
            res += str(len(word)) + "#" + word  
       
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        5#Hello5#World
        res = []
        i = 0
        while i < len(s) :
            j = i
            while s[j] != '#' :
                j += 1
            length = int("".join(s[i:j]))
            start = j + 1
            end = start + length
            res.append(s[start:end])
            i = end 
        print(res)
        return res 




