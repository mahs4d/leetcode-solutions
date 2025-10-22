class Solution:
    def __init__(self):
        self.cache = {}

    def minDistance(self, word1: str, word2: str) -> int:
        if len(word2) == 0:
            return len(word1)
        
        if len(word1) == 0:
            return len(word2)

        if (word1, word2) in self.cache:
            return self.cache[(word1, word2)]

        distances = []
        # edit or keep
        distances.append(
            (1 if word1[0] != word2[0] else 0) + self.minDistance(word1[1:], word2[1:])
        )
        
        # delete
        if len(word1) > 0:
            distances.append(
                1 + self.minDistance(word1[1:], word2)
            )
        
        # add
        if len(word2) > 0:
            distances.append(
                1 + self.minDistance(word1, word2[1:])
            )
        
        value = min(distances)
        self.cache[(word1, word2)] = value
        return value