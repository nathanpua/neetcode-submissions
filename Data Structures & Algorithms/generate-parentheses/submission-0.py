class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.res = []
        self.cur = []
        def backtrack(o, c):
            if c == n:
                self.res.append("".join(self.cur.copy()))
                return
            
            
            
            if o > c:
                if o < n:
                    self.cur.append('(')
                    backtrack(o+1, c) 
                    self.cur.pop()

                self.cur.append(')')
                backtrack(o, c+1)
                self.cur.pop()
            
            else:
                self.cur.append('(')
                backtrack(o+1, c)
                self.cur.pop()

        backtrack(0, 0)

        return self.res                