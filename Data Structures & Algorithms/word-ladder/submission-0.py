class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList :
            return 0
        
        adjList = defaultdict(list)
        wordList.append(beginWord)

        for word in wordList :
            for j in range(len(word)):
                pattern = word[:j] + '*' + word[j + 1: ]
                adjList[pattern].append(word)
        
        visit = set([beginWord])
        q = deque([beginWord])
        res = 1
        
        while q :
            for _ in range(len(q)):
                word = q.popleft()
                if word == endWord :
                    return res
                
                for j in range(len(word)):
                    pattern = word[:j] + '*' + word[j + 1 :]

                    for neiW in adjList[pattern]:
                        if neiW not in visit :
                            visit.add(neiW)
                            q.append(neiW)
            res += 1
        
        return 0
