class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if n < k:
            return None
        nums = []
        num = 1
        numsList = []
        while num<=n:
            nums.append(num)
            if len(nums) == k:
                newNums = nums[:]
                numsList.append(newNums)
                num = nums.pop()
                if num == n and nums:
                    num = nums.pop()
            elif num+k-len(nums) > n:
                nums.pop()
                if nums: 
                    num = nums.pop()
            num += 1
        return numsList
 
assert Solution().combine(4,2) == [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
#Solution().combine(20,16)