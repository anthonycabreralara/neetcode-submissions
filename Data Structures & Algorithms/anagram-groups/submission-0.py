class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_dict = {}
        

        for str in strs:
            sorted_str = ''.join(sorted(str))

            if sorted_str in str_dict:
                str_dict[sorted_str] += [str]
            else:
                str_dict[sorted_str] = [str]

        output = []
        for item in str_dict:
            output.append(str_dict[item])

        return output
        