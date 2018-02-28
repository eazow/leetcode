class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        def compare(people1, people2):
            if people1[0] > people2[0]:
                return -1
            elif people1[0] < people2[0]:
                return 1

            if people1[1] > people2[1]:
                return 1
            elif people1[1] < people2[1]:
                return -1
            return 0

        persons = sorted(people, compare)
        queue = []
        for person in persons:
            queue.insert(person[1], person)

        return queue

assert Solution().reconstructQueue([[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]) == [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
assert Solution().reconstructQueue([[9,0],[7,0],[1,9],[3,0],[2,7],[5,3],[6,0],[3,4],[6,2],[5,2]]) == \
    [[3,0],[6,0],[7,0],[5,2],[3,4],[5,3],[6,2],[2,7],[9,0],[1,9]]