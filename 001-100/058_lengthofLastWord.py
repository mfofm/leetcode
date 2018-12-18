"""
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', 
return the length of last word in the string.
If the last word does not exist, return 0.

Note: 
	A word is defined as a character sequence consists of non-space 
	characters only.

Example:
	Input: "Hello World"
	Output: 5
"""


# 这一题存在疑惑, 感觉有点争议, 而且本地运行和提交结果不一致
class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        cnt, tail = 0, len(s) - 1
        while tail >= 0 and s[tail] == ' ':
            tail -= 1
        while tail >= 0 and s[tail] != ' ':
            cnt += 1
            tail -= 1
        return cnt