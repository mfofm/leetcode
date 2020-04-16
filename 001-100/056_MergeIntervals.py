"""
Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/merge-intervals
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

#排序加一次遍历，运行时空间上超过了100%的用户
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if intervals==[]:
            return intervals
        intervals.sort()
        res=[intervals[0]]
        for l,m in intervals[1:]:
            if l>res[-1][1]:
                res.append([l,m])
            else:
                res[-1][1]=max(m,res[-1][1])
        return res
