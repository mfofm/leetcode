"""
Given an integer, write a function to determine if it is a power of two.

Example 1:
	Input: 1
	Output: true 
	Explanation: 20 = 1
Example 2:
	Input: 16
	Output: true
	Explanation: 24 = 16
Example 3:
	Input: 218
	Output: false
"""


# 通过位运算比较简单一点
class Solution:
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 1:
            return False
        return not(n & (n-1))