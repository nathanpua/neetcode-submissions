class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        count = sorted(count.items(), key = lambda x: x[1], reverse=True)
        return [num for num, freq in count[:k]]