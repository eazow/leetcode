class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type tatget: int
        :rtype List[List[int]]
        """
        nums = []
        indexes = []
        returnLists = []
        sum = 0
        i = 0
        candidates.sort()
        while True:
            while i >= len(candidates):
                if len(nums) == 0:
                    return returnLists
                sum -= nums.pop()
                i = indexes.pop()+1
            if sum + candidates[i] < target:
                nums.append(candidates[i])
                indexes.append(i)
                sum += candidates[i]
            elif sum + candidates[i] > target:
                if len(nums) > 0:
                    sum -= nums.pop()
                    i = indexes.pop()+1
                else:
                    return returnLists
            elif sum + candidates[i] == target:
                newNums = nums[:]
                newNums.append(candidates[i])
                returnLists.append(newNums)
                if len(nums) > 0:
                    sum -= nums.pop()
                    i = indexes.pop()+1
                else:
                    i += 1

    def combination_sum(self, candidates, target):
        self.result_nums = []
        candidates.sort()
        self.dfs(candidates, 0, target, [])
        return self.result_nums

    def dfs(self, nums, start_index, target, temp_nums):
        i = start_index
        while i < len(nums):
            num = nums[i]
            if num == target:
                self.result_nums.append(temp_nums.append(num))
                print self.result_nums
                break
            elif num < target:
                temp_nums.append(num)
                self.dfs(nums, i, target-num, temp_nums[:])
            else:
                return
            i += 1



# assert Solution().combinationSum([2, 3, 4], 7) == [[2, 2, 3], [3, 4]]
# assert Solution().combinationSum([2, 3, 6, 7], 7) == [[2, 2, 3], [7]]
# assert Solution().combinationSum([2], 1) == []


print Solution().combination_sum([2, 3, 4], 7)
