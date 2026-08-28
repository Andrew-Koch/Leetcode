class Solution:
    def reverse(self, x: int) -> int:
        #Convert to string and check if int is negative:
        intStr = str(x)
        negInt = False
        #Remove leading negative:
        if intStr[0] == "-":
            intStr = intStr[1:]
            negInt = True
        #Reverse int:
        intStr = intStr[::-1]
        x = int(intStr)
        #Make int negative again if applicable:
        if negInt:
            x = -x
        #If int outside 32-bit int range return 0: 
        if x <= -2**31 or x >= 2**31:
            return 0
        return x
