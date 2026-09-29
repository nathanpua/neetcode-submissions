class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        self.res = []

        def dfs(cur, target, last_idx):
            # base case
            if target == 0:
                self.res.append(cur.copy())
                return 

            for j in range(last_idx, len(nums)):
                if target - nums[j] >= 0:
                    cur.append(nums[j])
                    dfs(cur, target-nums[j], j)
                    cur.pop()

        dfs([], target, 0)
        return self.res