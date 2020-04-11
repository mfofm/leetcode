"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of 
the non-zero elements.

Example:
  Input: [0,1,0,3,12]
  Output: [1,3,12,0,0]
  
Note:
  You must do this in-place without making a copy of the array.
  Minimize the total number of operations.
"""


# 比较暴力
class Solution1:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in range(0, len(nums)):
            if nums[i] == 0:
                nums.remove(0)
                nums.append(0)

# 双指针，原地操作
class Solution2:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        head = 0
        cnt = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[head] = nums[i]
                head += 1
            else:
                cnt += 1
        for j in range(head, len(nums)):
            nums[j] = 0
