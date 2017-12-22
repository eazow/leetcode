class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        prev = 0
        cur = 1
        s_len = len(s)
        count = 1
        counts = []
        while cur < s_len:
            if s[prev] == s[cur]:
                count += 1
                prev += 1
                cur += 1
            else:
                counts.append(count)
                prev = cur
                cur += 1
                count = 1
        counts.append(count)

        cur = 1
        result = 0
        while cur < len(counts):
            result += min(counts[cur - 1], counts[cur])
            cur += 1
        return result

assert Solution().countBinarySubstrings("00110011") == 6
assert Solution().countBinarySubstrings("0110001111") == 6
