class Solution(object):
    def groupAnagrams(self, strs):
        """
        :param strs: List[str]
        :return: List[List[str]]
        """
        str_map = {}
        for temp_str in strs:
            temp_list = list(temp_str)
            temp_list.sort()
            convert_str = "".join(temp_list)
            if convert_str not in str_map:
                str_map[convert_str] = list()
            str_map.get(convert_str).append(temp_str)

        return str_map.values()


assert Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) == [
                                                                                   ['tan', 'nat'],
                                                                                   ['bat'],
                                                                                   ['eat', 'tea', 'ate']
                                                                               ]
