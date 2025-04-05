class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix=''
        strs.sort(key = lambda x: len(x))         
        for i in range(len(strs[0])):
            j = 1
            while j < len(strs):
                if strs[0][i] != strs[j][i]:
                    return prefix
                j += 1
            prefix += strs[0][i]
        return prefix
