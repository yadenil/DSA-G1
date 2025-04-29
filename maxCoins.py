class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        coins = 0
        piles.sort(reverse=True)
        n = len(piles) // 3
        for i in range (1, 2*n, 2):
            coins+= piles[i]
        return coins
