class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # use a queue to keep descending order
        queue = deque()
        res = []

        l = 0
        for r in range(len(nums)):
            # Maintain descending order. If we see a num larger than smallest,
            # pop out all smaller numbers, this will be the new max
            while queue and nums[r] > queue[-1]:
                queue.pop()
            queue.append(nums[r])
            # window size reached, add the max (queue[0]) to res. Check if this is the leftmost in window
            # if it is leftmost, its going to be removed from window. Remove from the queue
            if r-l+1 == k:
                maximum = queue[0]
                res.append(maximum)
                if nums[l] == maximum:
                    queue.popleft()
                l += 1

        return res