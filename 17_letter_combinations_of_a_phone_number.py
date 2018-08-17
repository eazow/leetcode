class Solution(object):
    def __init__(self):
        self.digit_chars_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

    def letterCombinations(self, digits):
        """
        :param digits: str
        :return: List[str]
        """
        if len(digits) == 0:
            return []
        elif len(digits) == 1:
            return list(self.digit_chars_map.get(digits[0]))
        else:
            combinations = []
            for i in self.digit_chars_map.get(digits[0]):
                for j in self.letterCombinations(digits[1:]):
                    combinations.append(i + j)

        return combinations


assert Solution().letterCombinations("") == []
assert Solution().letterCombinations("23") == ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]