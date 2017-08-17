class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        result = []
        for i in range(12):
            for j in range(60):
                if bin(i).count("1") + bin(j).count("1") == num:
                    result.append("%d:%02d" % (i, j))
        return result

assert Solution().readBinaryWatch(1) == ["0:01", "0:02", "0:04", "0:08", "0:16", "0:32", "1:00", "2:00", "4:00", "8:00"]