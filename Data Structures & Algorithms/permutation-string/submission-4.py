class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # cache s1 in a hashmap with char : count
        s1_len = len(s1)
        s1_counts = defaultdict(int)
        for i in range(len(s1)):
            s1_counts[s1[i]] += 1
        
        # cache s2 in a hashmap with char : count
        s2_counts = defaultdict(int)
        
        l = 0
        for r in range(len(s2)):
            # maintain a sliding window with window size of len(s1)
            s2_counts[s2[r]] += 1
            if r-l+1 == s1_len:

                # return true if both hashmaps same
                if s1_counts == s2_counts:
                    return True

                # track window and s2 cache
                s2_counts[s2[l]] -= 1
                if s2_counts[s2[l]] == 0: del s2_counts[s2[l]]
                l += 1

        return False
            