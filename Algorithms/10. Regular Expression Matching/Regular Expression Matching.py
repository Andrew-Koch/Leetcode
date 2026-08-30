class Solution:
    import re
    def isMatch(self, s: str, p: str) -> bool:
        #If regex matches entire string return true:
        try:
            if re.search(p, s).group() == s:
                return True
        except:
            pass
        return False