class Solution(object):
    def combinationSum3(self, k, n):
        nums = []
        num = 0
        sum = 0
        result = []
        while num < n:
            num += 1
            if num >= 10 and nums:
                num = nums.pop()
                sum -= num
                continue
            else:
                sum += num
            nums.append(num);
            if sum==n and len(nums)==k:
                newNums = nums[:]
                result.append(newNums)
                num = nums.pop()
                sum -= num
                num = nums.pop()
                sum -= num
            elif len(nums) == k or sum>n:
                num = nums.pop()
                sum -= num
                if num==n:
                    num = nums.pop()
                    sum -= num
        return result

assert Solution().combinationSum3(3, 9) == [[1,2,6],[1,3,5],[2,3,4]]
