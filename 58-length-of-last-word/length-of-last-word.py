class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        rev = s[::-1]
        rev = rev.strip()
        space = rev.find(" ")
        if not space == -1:
            return len(rev[:space])
        else:
            return len(rev)