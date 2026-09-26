class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        tortoise and hare algo
        """

        # l, r are pointers (slow and fast)
        slow, fast = 0, 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            # find cycle
            if slow == fast: break

        # reset to zero (start) then iterate at same pace
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow