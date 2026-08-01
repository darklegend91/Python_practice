'''
Buy and Sell Stock
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
'''

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <=1:
            return 0

        maxProfit = 0
        buy_at = prices[0]
        sell_at = prices[1]

        for price in prices:
            if (buy_at >= price):
                buy_at = price

            maxProfit = max(maxProfit , (price - buy_at))

        return maxProfit