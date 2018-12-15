"""
Given two binary strings, return their sum (also a binary string).
The input strings are both non-empty and contains only characters 1 or 0.

Example 1:
	Input: a = "11", b = "1"
	Output: "100"
Example 2:
	Input: a = "1010", b = "1011"
	Output: "10101"
"""

class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a, b = int('0b' + a, 2), int('0b' + b, 2)
        return bin(a + b)[2:]
