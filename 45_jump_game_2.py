# -*- coding:utf-8 -*-

class Solution(object):
    def jump(self, nums):
        """
        :param nums: List[int]
        :return: int
        """
        if len(nums) == 1:
            return 0

        min_index = 0
        max_index = 0
        step = 0

        while max_index <= len(nums) - 1:
            min_index_ready = False
            for i in range(min_index, max_index + 1):
                num = nums[i]
                if not min_index_ready:
                    min_index = max_index + 1
                    min_index_ready = True

                # 对于index=0的2，可以跳到index=1, index=2
                # 对于index=1的3, 可以跳到2,3,4; 对于index=2的1，可以跳到3

                max_index = max(max_index, i + num)
                if max_index >= len(nums) - 1:
                    return step + 1

            step += 1

        return step


assert Solution().jump([0]) == 0
assert Solution().jump([2, 3, 1, 1, 4]) == 2
assert Solution().jump([2,2,1,3,1,1,1,1]) == 4