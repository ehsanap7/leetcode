from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        for right in range(len(nums)):
            k -= 1 - nums[right]
            if (k < 0):
                k += 1 - nums[left]
                left = left + 1
        return right - left + 1


# Complexity Analysis

# Time Complexity:
# O(N)O(N)O(N), where NNN is the number of elements in the array.
# In worst case we might end up visiting every element of array twice,
# once by left pointer and once by right pointer.
#
# Space Complexity: O(1)O(1)O(1). We do not use any extra space.

if __name__ == '__main__':
    sol = Solution()
    nums = [0, 0, 0, 1]
    result = sol.longestOnes(nums, 4)
    print(result)
