class Solution:
    def isPalindrome(self, x: int) -> bool:
        #Convert int to String then check if reverse is equal:
        numStr = str(x)
        if numStr[::-1] == numStr:
            return True
        return False
