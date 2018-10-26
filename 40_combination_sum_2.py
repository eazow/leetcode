# -*- coding:utf-8 -*-

class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :param candidates: List[int]
        :param target: int
        :return: List[List[int]]
        """
        candidates.sort()
        self.result = []
        self.traverse(candidates, target)

    def traverse(self, candidates, target):
        if target == 0:
            print self.result
            self.result = []

        elif target > 0:
            for i in range(len(candidates)):
                self.result.append(candidates[i])
                print candidates[0:i] + candidates[i + 1:len(candidates)], target - candidates[i]
                self.traverse(candidates[0:i] + candidates[i + 1:len(candidates)], target - candidates[i])
        else:
            self.result = []


Solution().combinationSum2([10, 1, 2, 7, 6, 1, 5], 8)