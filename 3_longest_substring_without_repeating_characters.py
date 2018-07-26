class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :param s: str
        :return: int
        """
        positions = {}
        longest_length = 0
        right = 0
        for left in range(len(s)):
            # right = left is redudant
            while right < len(s):
                position = positions.get(s[right])
                if position is not None and position >= left:
                    break
                else:
                    positions[s[right]] = right
                    longest_length = max(longest_length, right - left + 1)
                right += 1

        return longest_length


assert Solution().lengthOfLongestSubstring("abcabcbb") == 3
assert Solution().lengthOfLongestSubstring("bbbbb") == 1
assert Solution().lengthOfLongestSubstring("abcdaefg") == 7
assert Solution().lengthOfLongestSubstring("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789\
    !\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789\
    !\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789\
    !\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789\
    !\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ abcdefghijklmnopqrstuvwxyzABCD") == 95

