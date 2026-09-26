class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        res = 0
        cache = defaultdict(int)

        for r in range(len(s)):
            while cache[s[r]] > 0:
                cache[s[l]] -= 1
                if cache[s[l]] == 0: del cache[s[l]]
                l += 1
            cache[s[r]] += 1
            res = max(res, (r-l)+1)

        return res