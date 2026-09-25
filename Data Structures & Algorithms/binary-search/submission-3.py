class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + (r-l) // 2

            if nums[m] > target:
                # need smaller 
                r = m - 1
            elif nums[m] < target:
                # need larger
                l = m + 1
            else:
                return m

        return -1