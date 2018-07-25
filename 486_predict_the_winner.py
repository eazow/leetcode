class Solution(object):
    def PredictTheWinner(self, nums):
        """
        :type: nums: List[int]
        :rtype: bool
        """
        return self.traverse(nums, 0, 0, True)

    def traverse(self, nums, score1, score2, first_turn):
            if len(nums) == 0:
                return score1 > score2
            if len(nums) == 1:
                if first_turn:
                    return score1 + nums[0] >= score2
                else:
                    return score1 >= score2 + nums[0]
            if first_turn:
                return self.traverse(nums[1:], score1 + nums[0], score2, False) or \
                       self.traverse(nums[:-1], score1 + nums[-1], score2, False)
            else:
                return self.traverse(nums[1:], score1, score2 + nums[0], True) and \
                       self.traverse(nums[:-1], score1, score2 + nums[-1], True)


assert Solution().PredictTheWinner([1, 5, 2]) is False
assert Solution().PredictTheWinner([1, 5, 233, 7]) is True
