class Solution:

    def max_subarray(self, nums: list) -> int:
        max_sum = nums[0]
        curr_sum = 0
        for num in nums:
            curr_sum = max(curr_sum + num, num)
            max_sum = max(max_sum, curr_sum)
        return max_sum


