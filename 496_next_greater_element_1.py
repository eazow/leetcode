class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        for findNum in findNums:
            numsCount = len(nums)
            i = 0
            equalFlag = False
            while i < numsCount:
                if equalFlag:
                    if findNum < nums[i]:
                        result.append(nums[i])
                        break;
                    else:
                        i += 1
                else:
                    if findNum == nums[i]:
                        equalFlag = True
                    i += 1
            if i == numsCount:
                result.append(-1)

        return result

assert Solution().nextGreaterElement([4,1,2], [1,3,4,2]) == [-1,3,-1]
assert Solution().nextGreaterElement([2,4], [1,2,3,4]) == [3,-1]