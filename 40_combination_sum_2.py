# -*- coding:utf-8 -*-
import copy


class Solution(object):
    def __init__(self):
        self.result = []
        self.result_set = set()

    def combinationSum2(self, candidates, target):
        """
        :param candidates: List[int]
        :param target: int
        :return: List[List[int]]
        """
        candidates.sort()
        self.traverse(candidates, target, [])
        return self.result

    def traverse(self, candidates, target, nums):
        if target == 0:
            nums_token = "_".join(map(str, nums))
            if nums_token not in self.result_set:
                self.result.append(nums)
                self.result_set.add(nums_token)

        elif target > 0:
            for i in range(len(candidates)):
                if target >= candidates[i]:
                    traverse_nums = copy.deepcopy(nums)
                    traverse_nums.append(candidates[i])
                    self.traverse(candidates[i + 1:len(candidates)], target - candidates[i], traverse_nums)
                else:
                    break


Solution().combinationSum2([10, 1, 2, 7, 6, 1, 5], 8)