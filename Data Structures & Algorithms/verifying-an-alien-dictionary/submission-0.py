class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:

        order_index : dict[str, int] = {ch : i for i, ch in enumerate(order)}
        
        return words == sorted(words, key = lambda x : [order_index[c] for c in x])
        