class Solution(object):
    def __init__(self):
        self.results = []

    def permuteUnique(self, nums):
        """
        :param nums: List[int]
        :return: List[List[int]]
        """
        nums.sort()
        used = [False] * len(nums)
        result = []

        self.dfs(nums, result, used)

        return self.results

    def dfs(self, nums, result, used):
        if len(result) == len(nums):
            self.results.append(result[:])

        for i in xrange(len(nums)):
            if not used[i]:
                # 如果相邻2个num相同，则前一个num没有使用时，后一个也不能使用，避免重复
                if i > 0 and (not used[i-1]) and (nums[i-1] == nums[i]):
                    continue
                result.append(nums[i])
                used[i] = True
                self.dfs(nums, result, used)
                used[i] = False
                result.pop()


assert Solution().permuteUnique([1, 1, 2]) == [[1, 1, 2], [1, 2, 1], [2, 1, 1]]