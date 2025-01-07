class Solution(object):
    def stringMatching(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        a = []
        for w in words:
            for c in words:
                if c in w and not c == w:
                    a.append(c)
        return list(set(a))