class Solution(object):
    def longestValidParentheses(self, s):
        """
        :param s: str
        :return: int
        """
        stack = []
        for i in range(len(s)):
            c = s[i]
            if c == "(":
                stack.append(i)
            elif c == ")":
                if len(stack) > 0 and s[stack[-1]] == "(":
                    stack.pop()
                else:
                    stack.append(i)

        if len(stack) == 0:
            max_length = len(s)
        else:
            max_length = stack[0]
            stack.append(len(s))
        i = 0
        while i + 1 < len(stack):
            max_length = max(max_length, stack[i+1] - stack[i] - 1)
            i += 1
        return max_length


print Solution().longestValidParentheses("((((()))))")
print Solution().longestValidParentheses(")()())")
print Solution().longestValidParentheses("()(()")
print Solution().longestValidParentheses("())")