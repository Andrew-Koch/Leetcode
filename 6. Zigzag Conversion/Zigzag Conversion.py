class Solution:
    def convert(self, s: str, numRows: int) -> str:
        #Edge case for single row:
        if numRows == 1:
            return s
        #Create array to store rows and int/bool to traverse:
        arrRows = numRows * [""]
        row, ascbool = 1, True
        #Add str values to array:
        for x in (s[1:]):
            arrRows[row] += x
            #Swap directions:
            if row == 0 or row == numRows-1:
                ascbool = not ascbool
            if ascbool:
                row += 1
            else:
                row -= 1
        #Return flattened array:
        return s[0] + "".join(arrRows)
