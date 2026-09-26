class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        s1_len = len(s1)
        s1_counts = defaultdict(int)
        for i in range(len(s1)):
            s1_counts[s1[i]] += 1

        s2_counts = defaultdict(int)

        for r in range(len(s2)):
            s2_counts[s2[r]] += 1
            if r-l+1 == s1_len:
                print(s1_counts)
                print(s2_counts)
                if s1_counts == s2_counts:
                    return True
                s2_counts[s2[l]] -= 1
                if s2_counts[s2[l]] == 0: del s2_counts[s2[l]]
                l += 1

        return False
            