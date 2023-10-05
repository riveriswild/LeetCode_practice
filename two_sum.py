"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice
nums = [2, 7, 11, 15]
target = 9
"""


class Solution:
    def twoSum(self, nums, target):
        prevMap = {}  # val: idx

        for idx, n in enumerate(nums):
            print(idx)
            print(n)
            print(prevMap)
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], idx]
            prevMap[n] = idx


nums = [2, 71, 11, 7, 15]
target = 9

solution = Solution()
s = solution.twoSum(nums, target)
print(s)
