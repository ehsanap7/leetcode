from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)
        head = 0
        i = len(nums) - 1
        tail = len(nums) - 1
        while (head <= tail):
            if abs(nums[head]) > abs(nums[tail]):
                result[i] = nums[head] * nums[head]
                head += 1
            else:
                result[i] = nums[tail] * nums[tail]
                tail -= 1
            i -= 1
        return result

# Complexity Analysis
#
# Time Complexity: O(N)O(N)O(N), where NNN is the length of A.
#
# Space Complexity: O(N)O(N)O(N) if you take output into account and O(1)O(1)O(1) otherwise.


if __name__ == '__main__':
    sol = Solution()
    nums = [-4, -1, 0, 3, 10]
    print(sol.sortedSquares(nums))
