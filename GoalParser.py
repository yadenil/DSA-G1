class Solution:
    def interpret(self, command: str) -> str:
        word = ''
        i = 0
        while i < len(command):
            if command[i] == 'G':
                word += 'G'
                i += 1
            elif i+1 < len(command) and command[i+1] == 'a':
                word += 'al'
                i += 4
            else:
                word += 'o'
                i += 2
        return word 
