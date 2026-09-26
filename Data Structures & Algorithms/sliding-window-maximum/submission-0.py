class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # use a queue to keep descending order
        queue = deque()
        res = []

        l = 0
        for r in range(len(nums)):
            while queue and nums[r] > queue[-1]:
                queue.pop()
            queue.append(nums[r])
            if r-l+1 == k:
                maximum = queue[0]
                res.append(maximum)
                if nums[l] == maximum:
                    queue.popleft()
                l += 1

        return res