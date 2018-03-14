class Solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        length = len(cost)
        i = 0
        min_cost0, min_cost1 = cost[0], cost[1]
        for i in range(2, length):
            min_cost0, min_cost1 = min_cost1, min(min_cost0, min_cost1) + cost[i]

        return min(min_cost0, min_cost1)
