class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height)-1
        maxWater=0
        while i != j:
            if height[i] < height[j]:
                maxWater = max(maxWater, (j-i) * height[i])
                i += 1
            else:
                maxWater = max(maxWater, (j-i) * height[j])
                j -= 1
        return maxWater
