class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m
        j = n-1
        while i < len(nums1):
            nums1[i] = nums2[j]
            j -=1
            i += 1
        nums1.sort()
