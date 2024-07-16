class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        inter = numRows-2
        res=''
        for row in range(numRows):
            if row == 0 or row == numRows-1:
                for i in range(row,len(s),numRows+inter):
                    res+=s[i]
            else:
                for i in range(row,len(s),numRows+inter):
                    a = numRows-row+(numRows-row-2)
                    if i+a < len(s):
                        res+=s[i]+s[i+a]
                    else:
                        res+=s[i]
        return res 
