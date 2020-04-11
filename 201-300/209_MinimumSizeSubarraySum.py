"""
Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

Example: 

Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.
Follow up:
If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n). 

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-size-subarray-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# 双指针夹逼
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums:
            return 0
        pointer1, pointer2 = 0, 0
        total = 0
        nums_len = len(nums)
        minL = nums_len + 1
        while pointer1 < nums_len:
            if pointer2 < nums_len and total < s:
                total += nums[pointer2]
                pointer2 += 1
            else:
                total -= nums[pointer1]
                pointer1 += 1
            if total >= s:
                minL = min(minL, pointer2-pointer1)
        if minL == nums_len + 1:
            return 0
        return minL