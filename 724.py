from typing import List


# Given an array of integers nums, calculate the pivot index of this array.
#
# The pivot index is the index where the sum of all the numbers
# strictly to the left of the index is equal
# to the sum of all the numbers strictly to the index's right.
#
# If the index is on the left edge of the array,
# then the left sum is 0 because there are no elements to the left.
# This also applies to the right edge of the array.
#
# Return the leftmost pivot index. If no such index exists, return -1.from typing import List


def pivotIndex(nums: List[int]) -> int:
    before = 0
    nexts = sum(nums)
    for i in range(0, len(nums)):
        nexts -= nums[i]
        if before == nexts:
            return i
        before += nums[i]
    return -1

# Complexity Analysis
#
# Time Complexity: O(N), where NN is the length of nums.
#
# Space Complexity: O(1), the space used by before and nexts.

if __name__ == '__main__':
    nums = [1, 7, 3, 6, 5, 6]
    print(pivotIndex(nums))
