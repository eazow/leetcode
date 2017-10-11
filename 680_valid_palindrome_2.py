class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                def is_palindrome(s, left, right):
                    while left < right:
                        if s[left] == s[right]:
                            left += 1
                            right -= 1
                        else:
                            return False
                    return True

                return is_palindrome(s, left+1, right) or is_palindrome(s, left, right-1)
        return True

assert Solution().validPalindrome("aba") == True
assert Solution().validPalindrome("abca") == True
assert Solution().validPalindrome("abcda") == False