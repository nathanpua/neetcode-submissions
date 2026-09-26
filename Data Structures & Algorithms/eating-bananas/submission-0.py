class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        search space: [1, max(piles)]
        """

        l, r = 1, max(piles)

        while l < r:
            m  = l + (r-l) // 2

            time = sum(math.ceil(p / m) for p in piles)

            if time > h:
                # m is not a possible candidate, we need a faster rate
                l = m + 1
            else: # time <= h
                # m is possible, try to find a slower rate
                r = m

        return l
