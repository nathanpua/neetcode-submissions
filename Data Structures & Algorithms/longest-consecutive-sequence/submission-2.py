class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        cache = defaultdict(int)
        res = 0

        for n in nums:
            cache[n] = 1

        for n in nums:
            if n-1 in cache:
                continue
            # n - 1 not in cache => it can be the start
            candidate = n
            cur = 0
            while candidate in cache:
                cur += 1
                candidate += 1
            res = max(res, cur)
        return res