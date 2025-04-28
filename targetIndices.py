class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        targetInd = []
        num = sorted(nums)
        for i in range(len(num)):
            if num[i] == target:
                targetInd.append(i)
        return targetInd
