"""
We define the Perfect Number is a positive integer that is equal to the sum of all its positive divisors 
except itself.
Now, given an integer n, write a function that returns true when it is a perfect number and false when it is not.

Example:
	Input: 28
	Output: True
	Explanation: 28 = 1 + 2 + 4 + 7 + 14

Note: The input number n will not exceed 100,000,000. (1e8)
"""

# 偷懒的做法, 因为范围内符合要求的就这几个数
class Solution:
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        r_list = [6, 28, 496, 8128, 33550336]
        if num in r_list:
            return True
        else:
            return False