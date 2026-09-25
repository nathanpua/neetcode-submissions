class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cache = {}
        for i in range(len(s)):
            cache[s[i]] = cache.get(s[i],0) + 1
        for j in range(len(t)):
            cache[t[j]] = cache.get(t[j], 0) - 1
            if cache[t[j]] == 0: del cache[t[j]]
        return len(cache) == 0