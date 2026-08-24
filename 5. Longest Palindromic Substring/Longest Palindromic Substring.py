class Solution:
    def longestPalindrome(self, s: str) -> str:
        #If string is single character return string:
        if len(s) == 1:
            return s
        longestpal = ""

        for i in range(1, len(s)-1):
            bothpal = False
            #If previous character identical to current character then pallindrome:
            if(s[i-1] == s[i]):
                currentpal = s[i-1] + s[i]
                prevpal = True
                try:
                    if(s[i-2] != s[i] and s[i+1] == s[i]):
                        currentpal += s[i+1]
                        bothpal = True
                except:
                    pass
            else:
                currentpal = s[i]
                prevpal = False
            repeatpal = currentpal
            #Check longest pallindrome possible for repeating digits:
            for j in range(i+1, len(s)):
                if s[j] == s[i]:
                    repeatpal += s[j]
                    #if bothpal ignore last repeating digit
                    if bothpal:
                        repeatpal = repeatpal[:-1]
                    #If new pallindrome is longest set
                    if len(repeatpal) > len(longestpal):
                        longestpal = repeatpal
                else:
                    break

            #For each element in array check longest surrounding palindrome:
            for j in range(1, i+1):
                #If previous and next character are identical palindrome is formed:
                try:
                    if not prevpal and s[i-j] == s[i+j]:
                        currentpal = s[i-j] + currentpal + s[i+j]
                    elif prevpal and not bothpal and s[i-j-1] == s[i+j]:
                        currentpal = s[i-j-1] + currentpal + s[i+j]
                        if (i-j-1 == -1):
                            currentpal.pop(0)
                    elif bothpal and s[i-j-1] == s[i+j+1]:
                        currentpal = s[i-j-1] + currentpal + s[i+j+1]
                        if (i-j-1 == -1):
                            currentpal.pop(0)
                    else:
                        break
                #If end of array reached then longest possible for current element found
                except:
                    break
                #If new pallindrome is longest set
                if len(currentpal) > len(longestpal):
                    longestpal = currentpal
        #Check for edge case of pallindrome with all identical characters
        currentpal = s[0]
        for i in range(1, len(s)):
            if(s[i] in currentpal):
                currentpal += s[i]
                if (len(currentpal) > len(longestpal)):
                    longestpal = currentpal
            else:
                break
            
        #If no pallindrome present return first character as pallindrome:
        if len(longestpal) == 0:
            longestpal = s[0]
        return longestpal
