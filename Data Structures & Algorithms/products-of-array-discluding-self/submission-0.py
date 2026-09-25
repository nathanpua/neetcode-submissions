class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = nums.copy()
        for i in range(1, len(pre)):
            pre[i] = pre[i-1] * nums[i]
        pre = [1] + pre

        post = nums.copy()
        for i in range(len(nums) - 2, -1, -1):
            post[i] = nums[i] * post[i+1]
        post.append(1)
        
        out = [1] * len(nums)
        for i in range(len(out)):
            out[i] = pre[i] * post[i+1]
        return out