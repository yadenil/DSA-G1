class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        result = []

        for char in words[0]:
            found_in_all = True
            for i in range(1, len(words)):
                if char in words[i]:
                    words[i] = words[i].replace(char, '', 1)  
                else:
                    found_in_all = False
                    break
            if found_in_all:
                result.append(char)

        return result
