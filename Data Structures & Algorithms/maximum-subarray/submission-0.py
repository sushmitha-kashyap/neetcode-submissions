#nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        currentSum = 0
        for n in nums:
            currentSum = max(currentSum, 0) + n
            maxSum = max(currentSum, maxSum)
        return maxSum
