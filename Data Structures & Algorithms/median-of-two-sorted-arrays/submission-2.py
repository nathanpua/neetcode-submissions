class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        if len(B) < len(A):
            A, B = B, A
        
        total = len(A) + len(B)
        half = total // 2

        l, r = 0, len(A) - 1
        while True:
            m = l+(r-l)//2
            
            A_idx = m
            B_idx = half-m-2

            A_left = A[A_idx] if A_idx >= 0 else float('-inf')
            B_left = B[B_idx] if B_idx >= 0 else float('-inf')
            A_right = A[A_idx+1] if 0 <= (A_idx+1) < len(A) else float('inf')
            B_right = B[B_idx+1] if 0 <= (B_idx+1) < len(B) else float('inf')

            # valid
            if A_left <= B_right and B_left <= A_right:
                if total % 2:
                    return min(B_right, A_right)
                return (max(B_left,A_left) + min(A_right, B_right)) / 2

            elif A_left > B_right:
                # need more from B and less from A
                r = m-1
            else:
                # need more from A and less from B
                l = m+1