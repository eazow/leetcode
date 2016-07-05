class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        if input.isdigit():
            return [int(input)]
        nums = []
        for i, c in enumerate(input):
            if c in '+-*':
                nums1 = self.diffWaysToCompute(input[:i])
                nums2 = self.diffWaysToCompute(input[i+1:])
                for num1 in nums1:
                    for num2 in nums2:
                        if c == '*':
                            nums.append(num1*num2)
                        elif c == '+':
                            nums.append(num1+num2)
                        elif c == '-':
                            nums.append(num1-num2)
        return nums

assert Solution().diffWaysToCompute("2-1-1")==[2,0]
assert Solution().diffWaysToCompute("2*3-4*5")==[-34, -10, -14, -10, 10]
