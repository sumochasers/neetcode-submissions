class TreeNode :
    def __init__(self):
        self.children = {}
        self.is_word_end = False

class WordDictionary:

    def __init__(self):
        self.root = TreeNode()

    def addWord(self, word: str) -> None:
        node = self.root

        for ch in word :
            if ch not in node.children :
                node.children[ch] = TreeNode()
            node = node.children[ch]
        
        node.is_word_end = True

    def isFound(self, node, word):
        if not node :
            return False
        
        for index, ch in enumerate(word) :
            if ch == "." :
                for node in node.children.values():
                    if self.isFound(node, word[index + 1:]):
                        return True
                return False
            
            else :
                if ch not in node.children :
                    return False
                node = node.children[ch]
                
        return node.is_word_end
    
    def search(self, word: str) -> bool:
        
        return self.isFound(self.root, word)
