class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        cache = defaultdict(list)

        for i in range(len(strs)):
            cache["".join(sorted(strs[i]))].append(strs[i])

        return list(cache.values())