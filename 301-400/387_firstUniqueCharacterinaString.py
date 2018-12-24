"""
Given a string, find the first non-repeating character in it and return it's index. 
If it doesn't exist, return -1.

Examples:
	s = "leetcode"
	return 0.
	s = "loveleetcode",
	return 2.

Note: You may assume the string contain only lowercase letters.
"""


class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = collections.Counter(s)
        for i in range(len(s)):            
            if dic[s[i]] == 1:
                return i        
        return -1