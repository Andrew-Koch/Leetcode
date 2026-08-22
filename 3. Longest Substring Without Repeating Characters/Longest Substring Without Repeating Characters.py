class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1
        substr = ""
        subcount = 1
        longest = 0
        #for each idx find max substr length:
        for i, x in enumerate(s[:-1]):
            substr = x
            subcount = 1
            for y in s[i+1:]:
                #If char y already in substring set new longest string length:
                if y in substr:
                    if subcount > longest:
                        longest = subcount
                    break
                #If char y not in substring set new substring length:
                else:
                    substr += y
                    subcount += 1
                    if subcount > longest:
                        longest = subcount
            #If no repeating digits 
            if longest == 0:
                longest = subcount     
        return longest
