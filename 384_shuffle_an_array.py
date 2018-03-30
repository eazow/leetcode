import copy
import random

class Solution(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.nums

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        shuffle_nums = copy.copy(self.nums)
        for i in range(len(shuffle_nums)):
            j = random.randint(0, len(shuffle_nums) - 1)
            temp = shuffle_nums[i]
            shuffle_nums[i] = shuffle_nums[j]
            shuffle_nums[j] = temp
        return shuffle_nums



nums = [1, 2, 3]
obj = Solution(nums)
print obj.reset()
print obj.shuffle()
print obj.reset()