class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []

        def dfs(cur):
            # base case
            if len(cur) == len(nums):
                self.res.append(cur.copy())
                return 

            for n in nums:
                if n not in cur:
                    cur.append(n)
                    dfs(cur)
                    cur.pop()

            
        dfs([])
        return self.res