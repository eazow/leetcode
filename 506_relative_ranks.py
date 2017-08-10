class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        numsStrs = []
        for i in range(len(nums)):
            numsStrs.append(str(nums[i])+'-'+str(i))

        numsStrs = sorted(numsStrs, lambda x,y: cmp(int(x.split("-")[0]), int(y.split("-")[0])))[::-1]
        ranks = [''] * len(nums)
        for i in range(len(numsStrs)):
            index = int(numsStrs[i].split("-")[1])
            if i == 0:
                ranks[index] = "Gold Medal"
            elif i == 1:
                ranks[index] = "Silver Medal"
            elif i == 2:
                ranks[index] = "Bronze Medal"
            else:
                ranks[index] = str(i+1)
        return ranks

assert Solution().findRelativeRanks([1, 2, 3, 4, 5]) == ["5", "4", "Bronze Medal", "Silver Medal", "Gold Medal"]
assert Solution().findRelativeRanks([10, 3, 8, 9, 4]) == ["Gold Medal", "5", "Bronze Medal", "Silver Medal", "4"]