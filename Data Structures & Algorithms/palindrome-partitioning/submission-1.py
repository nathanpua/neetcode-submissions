class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.res, self.cur = [], []

        def backtrack(i):
            # base case
            if i >= len(s):
                self.res.append(self.cur.copy())
                return

            for j in range(i, len(s)):
                if s[i:j+1] == s[i:j+1][::-1]:
                    self.cur.append(s[i:j+1])
                    backtrack(j+1)
                    self.cur.pop()
            
        backtrack(0)
        return self.res
        
        # print(s[0:0]) ''
        # print(s[0:1]) 'a'
        # print(s[0:2]) 'aa'
        # print(s[0:3]) 'aab'

            