"""
Count the number of segments in a string, where a segment is defined to be a contiguous sequence of non-space characters.

Please note that the string does not contain any non-printable characters.

Example:

Input: "Hello, my name is John"
Output: 5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/number-of-segments-in-a-string
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# 虽然简洁，但是运行效果不太理想，而且题目中的单词非常规意义的单词，你如：" , , , , a, eaefa"的预期结果是6。
class Solution:
    def countSegments(self, s: str) -> int:
        return len(s.split())
