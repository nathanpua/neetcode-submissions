class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = []

        def dfs(cur, i):
            if i > len(nums):
                return

            self.res.append(cur.copy())

            for j in range(i, len(nums)):
                cur.append(nums[j])
                dfs(cur, j+1)
                cur.pop()

        dfs([], 0)

        return self.res
