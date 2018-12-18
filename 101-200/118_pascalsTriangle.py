"""
Given a non-negative integer numRows, 
generate the first numRows of Pascal's triangle.

Example:
	Input: 5
	Output:
	[
	     [1],
	    [1,1],
	   [1,2,1],
	  [1,3,3,1],
	 [1,4,6,4,1]
	]
"""


class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        triangle = []
        for i in range(numRows):
            row = [1 for _ in range(i+1)]
            if i > 1:
                prev_row = triangle[-1]
                for j in range(1, len(row) - 1):
                    row[j] = prev_row[j-1] + prev_row[j]
            triangle.append(row)
        return triangle