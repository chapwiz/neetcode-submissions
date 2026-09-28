class Solution:
    def isValid(self, s: str) -> bool:
        brackets = []
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }

        for c in s:
            if c in '({[':
                brackets.append(c)
            else:
                if brackets and brackets[-1] == closeToOpen[c]:
                    brackets.pop()
                else:
                    return False
        
        if not brackets:
            return True
        else:
            return False