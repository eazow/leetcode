class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "0"
        map = ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"]
        hex = ""
        for i in range(8):
            hex = map[num & 0xf] + hex
            num = num >> 4

        return hex.lstrip("0")

assert Solution().toHex(-1) == "ffffffff"
assert Solution().toHex(26) == "1a"