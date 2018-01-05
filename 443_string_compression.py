class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        start = 0
        current = 1
        count = 1
        result = ""
        while current < len(chars):
            if chars[current] == chars[start]:
                count += 1
            else:
                result += chars[start]
                if count > 1:
                    result += str(count)
                start = current
                count = 1
            current += 1
        result += chars[start]
        if count > 1:
            result += str(count)

        i = 0
        while i < len(result):
            chars[i] = result[i]
            i += 1

        return len(result)

chars = ["a", "a", "b", "b", "c", "c", "c"]
assert Solution().compress(chars) == 6

assert chars == ["a", "2", "b", "2", "c", "3", "c"]
chars = ["a", "b"]
assert Solution().compress(["a", "b"]) == 2
assert chars == ["a", "b"]