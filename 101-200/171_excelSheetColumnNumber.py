"""
Given a column title as appear in an Excel sheet, return its corresponding column number.
For example:
    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
    ...

Example 1:
	Input: "A"
	Output: 1
Example 2:
	Input: "AB"
	Output: 28
Example 3:
	Input: "ZY"
	Output: 701
"""

class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        temp_str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        s_len = len(s)
        rnum = 0
        for i in range(s_len):
            rnum += (temp_str.find(s[i]) + 1) *(26 ** (s_len - 1 - i)) 
        return rnum