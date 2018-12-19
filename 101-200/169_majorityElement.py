"""
Given an array of size n, find the majority element. The majority element is the element that appears 
more than ⌊ n/2 ⌋ times.
You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:
	Input: [3,2,3]
	Output: 3
Example 2:
	Input: [2,2,1,1,1,2,2]
	Output: 2
"""

class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return nums[(len(nums) // 2)]

    def majorityElement2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num = set(nums)
        max_count = 0
        for i in num:
            if nums.count(i) > max_count:
                max_count = nums.count(i)
        for i in num:
            if nums.count(i) == max_count:
                return i