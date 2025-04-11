class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums) - 1):
            if nums[i] == nums[i+1]:
                nums[i] = nums[i] * 2
                nums[i+1] = 0
                i += 2
            else: 
                i+=1
        result = [num for num in nums if num != 0]
        zeros = [0] * (len(nums) - len(result))
        return result + zeros
