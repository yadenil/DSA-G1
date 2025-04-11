class Solution:
    def freqAlphabets(self, s: str) -> str:
        i = 0
        word = ''
        while i < len(s):
            if i+2 < len(s) and s[i+2] == '#':
                le = chr(int(s[i:i+2]) + 96)
                word += le
                i += 3
            else:
                le = chr(int(s[i]) + 96)
                word += le
                i += 1
        return word
