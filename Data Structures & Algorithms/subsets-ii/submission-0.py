class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        nums.sort()

        self.cur = []
        def backtrack(i):
            if i > len(nums):
                return
            
            self.res.append(self.cur.copy())

            j = i
            while j < len(nums):
                self.cur.append(nums[j])
                backtrack(j+1)
                self.cur.pop()

                j += 1
                while j < len(nums) and nums[j] == nums[j-1]:
                    j += 1


        backtrack(0)

        return self.res
