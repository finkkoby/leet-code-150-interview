class Solution(object):
    def minOperations(self, boxes):
        """
        :type boxes: str
        :rtype: List[int]
        """
        a = []
        for i in range(0, len(boxes)):
            t = 0
            for j in range(0, len(boxes)):
                if boxes[j] == '1':
                    t += abs(j - i)
            a.append(t)
        return a