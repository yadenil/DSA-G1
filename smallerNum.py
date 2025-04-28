class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        num = sorted(nums)
        dicti = {}
        for i, e in enumerate(num):
            if e not in dicti:
                dicti[e]=i
        ans=[dicti[n] for n in nums]
        return ans
