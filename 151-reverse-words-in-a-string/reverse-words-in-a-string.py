import re
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.strip()
        s = re.sub(" +", " ", s)
        words = s.split(" ")
        words.reverse()
        return " ".join(words)