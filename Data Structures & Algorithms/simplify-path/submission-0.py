class Solution:
    def simplifyPath(self, path: str) -> str:
        segments = path.split('/')

        res = []
        
        for entry in segments :
            if entry == '.' or entry == '':
                continue
            elif entry == '..':
                if res :
                    res.pop()
            else:
                res.append(entry)
        
        
        return '/' + '/'.join(res)