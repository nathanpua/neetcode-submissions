class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = []

        def dfs(cur, i):
            # base case: idx exceeds length (index error)
            if i > len(nums):
                return

            # add cur to result (possible candidate)
            self.res.append(cur.copy())

            # iterate over indexes so we dont add back previous nums
            for j in range(i, len(nums)):
                # add cur idx to cur array and call dfs on next index
                cur.append(nums[j])
                dfs(cur, j+1)
                cur.pop()

        dfs([], 0)

        return self.res
