"""
A self-dividing number is a number that is divisible by every digit it contains.
For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, 
and 128 % 8 == 0.
Also, a self-dividing number is not allowed to contain the digit zero.
Given a lower and upper number bound, output a list of every possible self dividing 
number, including the bounds if possible.

Example 1:
	Input: 
	left = 1, right = 22
	Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]

Note:
	The boundaries of each input argument are 1 <= left <= right <= 10000.
"""


class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        rlist = []
        for i in range(left, (right+1)):
            i_str = str(i)
            if '0' not in i_str:
                i_len = len(i_str)
                str_temp = ''
                for x in range(i_len):
                    if (i % int(i_str[x])) != 0:
                        str_temp += 'f'
                    else:
                        str_temp += 't'
                if str_temp.find('f') == -1:
                    rlist.append(i)   
        return rlist