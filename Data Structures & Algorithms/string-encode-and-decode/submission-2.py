class Solution:

    def encode(self, strs: List[str]) -> str:
        # USE STR LENGTH AS A DELIMITER + '#
        # <length>#<string> for each string
        res = ""
        for s in strs:
            res += str(len(s))
            res += '#'
            res += s
        
        return res

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            j = i

            """length is everything before '#' """
            while s[j] != '#':
                j += 1
            length = int(s[i:j])

            """ i to i+length gives the string """
            i = j+1
            j = i+length
            res.append(s[i:j])
            i = j
        return res
            
