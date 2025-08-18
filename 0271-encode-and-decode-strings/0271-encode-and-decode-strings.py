class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        encoded_str = ''
        for s in strs:
            encoded_str += s.replace('/', '//') + '/:'
        return encoded_str

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        decoded_strings = []
        curr_string = ""
        i = 0
        while i < len(s):
            if s[i: i + 2] == '/:':
                decoded_strings.append(curr_string)
                curr_string = ''
                i += 2
            elif s[i: i + 2] == '//':
                curr_string += '/'
                i += 2
            else:
                curr_string += s[i]
                i += 1
        return decoded_strings

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))