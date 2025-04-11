class Solution:
    def similarPairs(self, words: List[str]) -> int:
        pairs = 0
        n = len(words)

        for i in range(n):
            set_i = set(words[i])
            for j in range(i+1, n):
                set_j = set(words[j])
                if set_j == set_i:
                    pairs += 1
            i += 1
        return pairs
