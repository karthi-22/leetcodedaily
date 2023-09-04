class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        n = len(costs)
        ice = 0
        while ice<n and costs[ice] <= coins:
            coins-=costs[ice]
            ice+=1
        return ice