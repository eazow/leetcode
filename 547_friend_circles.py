class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        if len(M) == 1:
            return 1

        num_set_map = {}
        for j in range(len(M)):
            for i in range(j):
                if M[i][j] == 1:
                    if i in num_set_map:
                        nums_set_i = num_set_map[i]
                        nums_set_i.add(i)
                        nums_set_i.add(j)
                        if j in num_set_map:
                            nums_set_j = num_set_map[j]
                            nums_set = nums_set_i | nums_set_j

                            for num in nums_set:
                                num_set_map[num] = nums_set
                        else:
                            num_set_map[j] = nums_set_i
                    else:
                        nums_set = set([i, j])
                        num_set_map[i] = nums_set
                        num_set_map[j] = nums_set
                else:
                    if i in num_set_map:
                        num_set_map[i].add(i)
                    else:
                        num_set_map[i] = set([i])
                    if j in num_set_map:
                        num_set_map[j].add(j)
                    else:
                        num_set_map[j] = set([j])

        statistic_set = set()
        for num, nums_set in num_set_map.items():
            statistic_set.add(tuple(nums_set))
        return len(statistic_set)

assert Solution().findCircleNum([[1, 1, 0], [1, 1, 0], [0, 0, 1]]) == 2
assert Solution().findCircleNum([[1, 1, 0], [1, 1, 1], [0, 1, 1]]) == 1
assert Solution().findCircleNum([[1,0,0,1], [0,1,1,0], [0,1,1,1], [1,0,1,1]]) == 1
assert Solution().findCircleNum([
    [1,1,0,0,0,0,0,1,0,0,0,0,0,0,0], [1,1,0,0,0,0,0,0,0,0,0,0,0,0,0], [0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,1,0,1,1,0,0,0,0,0,0,0,0], [0,0,0,0,1,0,0,0,0,1,1,0,0,0,0], [0,0,0,1,0,1,0,0,0,0,1,0,0,0,0],
    [0,0,0,1,0,0,1,0,1,0,0,0,0,1,0], [1,0,0,0,0,0,0,1,1,0,0,0,0,0,0], [0,0,0,0,0,0,1,1,1,0,0,0,0,1,0],
    [0,0,0,0,1,0,0,0,0,1,0,1,0,0,1], [0,0,0,0,1,1,0,0,0,0,1,1,0,0,0], [0,0,0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,1,0,0], [0,0,0,0,0,0,1,0,1,0,0,0,0,1,0], [0,0,0,0,0,0,0,0,0,1,0,0,0,0,1]
]) == 3