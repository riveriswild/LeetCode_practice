# given an integer array nums, return true if any value appeard at least twice
# in the array and false if every element is distinct

nums = [1,2,3,1]
nums2 = [1,2,3,4]
nums3 = [1,1,1,2,2,3,2,3,4,2]

# class Solution:
#     def containsDuplicate(self, nums: list[int])-> bool:
#         sorted_nums = sorted(nums)
#         for ind in range(len(sorted_nums)-1): # to avoid trying to compare last num with nothing
#             nxt = ind + 1
#             if sorted_nums[ind] == sorted_nums[nxt]:
#                 return True
#         return False
# space O(n), time O(logn)
    
class Solution:
    def containsDuplicate(self, nums: list[int])-> bool:
        return False if len(set(nums)) == len(nums) else True
    