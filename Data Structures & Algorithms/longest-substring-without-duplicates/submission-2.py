class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        res = 0
        cache = defaultdict(int)

        for r in range(len(s)):
            # Ensure that s[r] does not exist in cache (count = 0) slide window if it exists
            while cache[s[r]] > 0:
                cache[s[l]] -= 1
                l += 1

            # add current char to cache
            cache[s[r]] += 1

            # track the max window size seen
            res = max(res, (r-l)+1)

        return res