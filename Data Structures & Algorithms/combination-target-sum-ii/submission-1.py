class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.res = []
        candidates.sort()

        def dfs(cur, target, last):
            # base case
            if target == 0:
                self.res.append(cur.copy())
                return

            for i in range(last, len(candidates)):
                # skip this index if its num is same as prev num, to avoid duplicates
                if i > last and candidates[i] == candidates[i - 1]: continue

                # candidate is invalid
                if target - candidates[i] < 0:
                    continue
                cur.append(candidates[i])
                dfs(cur, target-candidates[i], i+1)
                cur.pop()
                

        dfs([], target, 0)
        return self.res