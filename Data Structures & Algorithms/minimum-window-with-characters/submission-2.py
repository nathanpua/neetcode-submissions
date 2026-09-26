class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res, minlen = "", float('inf')
        t_cache = defaultdict(int)
        for i in range(len(t)):
            t_cache[t[i]] += 1
 
        l = 0
        s_cache = defaultdict(int)
        have, need = 0, len(t_cache)
        for r in range(len(s)):
            s_cache[s[r]] += 1

            if s[r] in t_cache and s_cache[s[r]] == t_cache[s[r]]:
                have += 1

            while have == need:
 
                if (r-l+1) < minlen:
                    minlen = (r-l+1)
                    res = s[l:r+1]
                s_cache[s[l]] -= 1
                if s[l] in t_cache and s_cache[s[l]] < t_cache[s[l]]:
                    have -= 1
                l += 1

        return res
