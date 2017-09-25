class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        result = 0
        points = []
        for op in ops:
            if op == "D":
                point = points[-1] * 2
                result += point
                points.append(point)
            elif op == "+":
                point = points[-1] + points[-2]
                result += point
                points.append(point)
            elif op == "C":
                point = points.pop()
                result -= point
            else:
                result += int(op)
                points.append(int(op))
        return result

assert Solution().calPoints(["5", "2", "C", "D", "+"]) == 30
assert Solution().calPoints(["5","-2", "4", "C", "D", "9", "+", "+"]) == 27