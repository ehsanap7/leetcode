from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        left = 0
        counter = 0
        multi = 1

        for right in range(len(nums)):
            multi *= nums[right]
            while left <= right and multi >= k:
                multi /= nums[left]
                left += 1

            counter += right - left + 1

        return counter


# Time Complexity: O(N)O(N)O(N), where NNN is the length of nums.
#
# Left can only be incremented at most N times.
#
# Space Complexity: O(1)O(1)O(1), the space used by prod, left, and ans.

if __name__ == '__main__':
    sol = Solution()
    nums = [10, 5, 2, 6]
    print(sol.numSubarrayProductLessThanK(nums, 100))
