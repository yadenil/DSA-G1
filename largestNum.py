class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare(a, b):
            if a+b > b+a:
                return -1
            else:
                return 1
        for i, n in enumerate(nums):
            nums[i] = str(n)
        
        nums = sorted(nums, key=cmp_to_key(compare))

        return str(int("".join(nums)))

        
