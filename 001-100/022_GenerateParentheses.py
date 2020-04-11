"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/generate-parentheses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# 感觉花费时间不是很理想
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
            if n == 0:
                return [""]
            elif n == 1:
                return ["()"]
            elif n == 2:
                return ["()()", "(())"]
            result = []
            for i in range(n):
                j = n - 1 - i
                res1 = self.generateParenthesis(i)
                res2 = self.generateParenthesis(j)
                result.extend(["(%s)%s" % (p, q) for p in res1 for q in res2])
            return result