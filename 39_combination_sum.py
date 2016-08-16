class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type tatget: int
        :rtype List[List[int]]
        """
        nums = []
        returnLists = []
        sum = 0
        for i in range(len(candidates)):
            while True:
                if sum + candidates[i] > target:
                    if len(nums) > 0:
                        sum -= nums.pop()
                    break
                elif sum + candidates[i] == target:
                    newNums = nums[:]
                    newNums.append(candidates[i])
                    returnLists.append(newNums)
                    if len(nums) > 0:
                        sum -= nums.pop()
                    break
                else:
                    nums.append(candidates[i])
                    sum += candidates[i]

        return returnLists

print Solution().combinationSum([2,3,4], 7)
