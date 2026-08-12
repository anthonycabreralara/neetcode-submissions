class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        
        for string in strs:
            encoded_string = encoded_string + str(len(string)) + "#" + string
        
        return encoded_string

    def decode(self, s: str) -> List[str]:
        index = 0
        decoded_string_list = []

        print(s)
        while index < len(s):
            string_length = ""
            while s[index] != "#":
                string_length = string_length + s[index]
                index = index + 1
            
            index = index + 1
            
            print(index)
            print(string_length)
            decoded_string_list.append(s[index:index+int(string_length)])
            print(decoded_string_list)
            index = index+int(string_length)

        return decoded_string_list
