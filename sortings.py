# bubble sort


def bubble_sort(nums):
    swapped = True
    while swapped:
        swapped = False
        a = range(len(nums) - 1)
        for i in range(len(nums) - 1):
            initial = nums[i]
            compare = nums[i + 1]
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True


random_list_of_nums = [5, 2, 1, 8, 4, 9, 7]
bubble_sort(random_list_of_nums)
print(random_list_of_nums)
