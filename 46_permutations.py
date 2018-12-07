class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return_lists = [[]]
        for num in nums:
            new_lists = []
            for return_list in return_lists:
                for i in range(len(return_list) + 1):
                    new_list = return_list[:i] + [num] + return_list[i:]
                    new_lists.append(new_list)
                    return_lists = new_lists
        return return_lists


assert Solution().permute([1, 2, 3]) == [[3, 2, 1], [2, 3, 1], [2, 1, 3], [3, 1, 2], [1, 3, 2], [1, 2, 3]]
