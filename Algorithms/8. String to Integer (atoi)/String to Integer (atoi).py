class Solution:
    import re
    def myAtoi(self, s: str) -> int:
        #Edge case for empty string:
        if s == "":
            return 0
        #Get starting location for number, sign, and other chars:
        locNeg = loc.start() if (loc :=re.search(r'[+-]',  s)) else -1
        locNum = loc.start() if (loc :=re.search(r'\d',  s)) else -1
        locChar =loc.start() if (loc :=re.search(r'[^-\s]',  s)) else -1
        isNeg = False
        #If sign not immediately followed by a digit return 0:
        try:
            if locNeg > -1 and not s[locNeg+1].isdigit() and locNeg < locNum:
                return 0
        except:
            pass
        #If first character isn't a number then return 0:
        if locChar != -1 and not s[locChar].isdigit() and s[locChar]!="-" and s[locChar]!="+":
            return 0
        #Check if negative sign occurs before numbers:
        if locNeg > -1 and locNeg < locChar:
           isNeg = True
        numStr = ""
        #Add all numbers remaining until first non-digit:
        for i in range (locNum, len(s)):
            if s[i].isdigit():
                numStr += s[i]
            else:
                break
        num = 0
        #Convert num string into int:
        for x in numStr:
            num = num * 10 + (ord(x) - ord('0'))
        #Round to nearest int within range:
        if num > 2**31 -1:
            if isNeg:
                num = 2**31
            else:
                num = 2**31 -1
        #If necessary convert to negative:
        if isNeg:
            return -num
        return num
