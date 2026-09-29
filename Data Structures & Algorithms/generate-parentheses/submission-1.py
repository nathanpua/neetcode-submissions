class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.res = []
        self.cur = []
        def backtrack(o, c):
            if c == n:
                self.res.append("".join(self.cur.copy()))
                return
            
            # 1. If o > c, can choose o if less than n, can also choose c
            if o > c:
                if o < n:
                    self.cur.append('(')
                    backtrack(o+1, c) 
                    self.cur.pop()

                self.cur.append(')')
                backtrack(o, c+1)
                self.cur.pop()
            # if o == c, must choose opened here
            else:
                self.cur.append('(')
                backtrack(o+1, c)
                self.cur.pop()

        backtrack(0, 0)

        return self.res                