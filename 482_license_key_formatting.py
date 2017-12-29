class Solution(object):
    def licenseKeyFormatting(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        s = "".join(s.split("-"))
        first = len(s) % k
        result = []
        if first:
            result = [s[0: first].upper()]

        i = first
        while i < len(s):
            result.append(s[i: i+k].upper())
            i += k

        return "-".join(result)

assert Solution().licenseKeyFormatting("5F3Z-2e-9-w", 4) == "5F3Z-2E9W"
assert Solution().licenseKeyFormatting("2-5g-3-J", 2) == "2-5G-3J"