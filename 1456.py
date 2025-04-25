class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        count = float('-inf')
        i = 0
        j = k
        while j <= len(s):
            tempCount = 0
            for item in s[i:j]:
                if item in 'aeiou':
                    tempCount += 1
            count = max(count, tempCount)
            i += 1
            j += 1
        return count
