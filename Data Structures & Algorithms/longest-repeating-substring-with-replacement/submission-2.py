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

            # Window is invalid. slide until its valid
            # tracking max_frq allows invalid windows but cannot make the algorithm record a length larger than one that was achievable when maxf was accurate.
            while (r - l + 1) - max_frq > k:
                cache[s[l]] -= 1 
                l += 1

            # print(s[l:r+1])

            res = max(res, r-l+1)

        return res