# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
from typing import List


# Complexity Analysis
#
# Time complexity: O(n)
# where n is the length of the input array.
# This is because we use a single loop that iterates over the entire array to calculate the running sum.
#
# Space complexity: O(1)
# since we don't use any additional space to find the running sum.
# Note that we do not take into consideration the space occupied by the output array.

class Solution:
    def minStartValues(self, nums: List[int]) -> int:
        nums.insert(0, 0)
        result = 0
        for i in range(1, len(nums)):
            nums[i] = nums[i] + nums[i - 1]
            result = min(result, nums[i])
        return 1 - result


if __name__ == '__main__':
    sol = Solution()
    nums = [-3, 2, -3, 4, 2]
    result = sol.minStartValues(nums)
    print(result)
