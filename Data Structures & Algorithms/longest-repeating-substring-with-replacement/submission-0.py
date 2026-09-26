class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        valid window -> window_size - max frq <= k

        slide window while invalid
        """

        l = 0
        res = 0
        cache = defaultdict(int)

        max_frq = 0
        for r in range(len(s)):
            cache[s[r]] += 1
            max_frq = max(max_frq, cache[s[r]])

            while (r - l + 1) - max_frq > k:
                cache[s[l]] -= 1 
                l += 1

            res = max(res, r-l+1)

        return res