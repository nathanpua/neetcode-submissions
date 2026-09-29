class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        cache = {
            '2':['a','b','c'],
            '3':['d','e','f'],
            '4':['g','h','i'],
            '5':['j','k','l'],
            '6':['m','n','o'],
            '7':['p','q','r','s'],
            '8':['t','u','v'],
            '9':['w','x','y','z']
        }

        self.res, self.cur = [], []

        if len(digits) == 0: return self.res

        def backtrack(i):
            if i >= len(digits):
                self.res.append("".join(self.cur.copy()))
                return

            candidates = cache[digits[i]]

            for c in candidates:
                self.cur.append(c)
                backtrack(i+1)
                self.cur.pop()

        backtrack(0)
        return self.res
                
