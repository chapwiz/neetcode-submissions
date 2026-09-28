class Solution:
    def isPalindrome(self, s: str) -> bool:
        newS = ''.join(filter(str.isalnum, s))
        pt1 = 0
        pt2 = len(newS) - 1

        while pt1 < pt2:
            if newS[pt1].lower() != newS[pt2].lower():
                return False
            pt1 += 1
            pt2 -= 1
        
        return True