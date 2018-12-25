"""
Given a List of words, return the words that can be typed using letters of alphabet on only one row's of 
American keyboard like the image below.

Example:
	Input: ["Hello", "Alaska", "Dad", "Peace"]
	Output: ["Alaska", "Dad"]
 
Note:
	You may use one character in the keyboard more than once.
	You may assume the input string will only contain letters of alphabet.
"""


class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        res=[]
        keyset=['qwertyuiop','asdfghjkl','zxcvbnm']
        for keys in keyset:
            for word in words:
                line=set(word.lower())
                if line.issubset(set(keys)):
                    res.append(word)
        return res