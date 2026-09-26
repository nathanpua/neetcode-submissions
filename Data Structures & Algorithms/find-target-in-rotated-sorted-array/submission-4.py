class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        idea: upon splitting array into 2 halves, one side is guaranteed to be sorted
        If the num is within the sorted side , search that side
        else search the other side
        """

        l, r = 0, len(nums)-1

        while l <= r:
            m = l + (r-l) // 2

            if target == nums[m]: return m

            # RHS sorted
            elif nums[m] < nums[r]:
                # If target is in the sorted side
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
            # LHS is sorted
            else:
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1

        return -1