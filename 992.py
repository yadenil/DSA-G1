class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        num = 0
        i, j = 0, k
        while j<=len(nums):
            unique = []
            for item in nums[i:j]:
                if item not in unique:
                    unique.append(item)
            if len(unique) == k:
                num += 1
                j += 1
            elif len(unique) < k:
                j+=1
            elif len(unique) > k:
                i += 1
                j = i+k
        return num
                
