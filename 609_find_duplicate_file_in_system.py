class Solution(object):
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        content_map = {}
        for path in paths:
            directory_files = path.split(" ")
            directory_path = directory_files[0]
            i = 1
            while i < len(directory_files):
                file = directory_files[i]
                file_name_content = file.split("(")
                file_name = file_name_content[0]
                file_content = file_name_content[1][:-1]

                file_path = directory_path + "/" + file_name
                if file_content not in content_map:
                    content_map[file_content] = []

                content_map[file_content].append(file_path)
                i += 1

        result = []
        for content, file_paths in content_map.items():
            if len(file_paths) > 1:
                result.append(file_paths)
        return result

assert Solution().findDuplicate(["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"]) \
    == [["root/a/1.txt","root/c/3.txt"], ["root/a/2.txt","root/c/d/4.txt","root/4.txt"]]
assert Solution().findDuplicate(["root/a 1.txt(abcd) 2.txt(efsfgh)","root/c 3.txt(abdfcd)","root/c/d 4.txt(efggdfh)"]) == []