class TrieNode :
    def __init__(self):
        self.children = {}
        self.isWord = False

    def addWord(self, word):
        node = self
        
        for c in word :
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        
        node.isWord = True

class Solution:
    
    def __init__(self):
        self.res = set()
        self.visit = set()
    
    def dfs(self, r, c, node, word):
        
        if  (r < 0 or c < 0 or \
            r >= self.ROWS or c >= self.COLS or \
            (r, c) in self.visit or \
            self.board[r][c] not in node.children) :

            return False
        
        self.visit.add((r, c))
        node = node.children[self.board[r][c]]
        word += self.board[r][c]

        if node.isWord :
            self.res.add(word)
        
        self.dfs(r , c + 1, node, word)
        self.dfs(r , c - 1, node, word)
        self.dfs(r + 1 , c , node, word)
        self.dfs(r - 1 , c , node, word)
    
        self.visit.remove((r, c))



    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        root = TrieNode()
        for w in words :
            root.addWord(w)
        
        self.words = words
        self.board = board

        self.ROWS = len(board)
        self.COLS = len(board[0])

        for r in range(self.ROWS):
            for c in range(self.COLS):
                self.dfs(r, c, root, "")

        return list(self.res)

