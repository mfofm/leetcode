"""
Given a positive integer num, write a function which returns True if num is a perfect 
square else False.

Note: Do not use any built-in library function such as sqrt.

Example 1:
	Input: 16
	Output: true
Example 2:
	Input: 14
	Output: false
"""


# 二分法
class Solution:
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        low = 1
        high = num
        while low <= high:
            mid = (low + high) // 2
            if mid**2 == num:
                return True
            if mid**2 > num:
                high = mid - 1
            else:
                low = mid + 1
        return False