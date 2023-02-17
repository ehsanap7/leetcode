from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        left = 0
        right = 0

        while right < len(nums):
            if nums[left] == 0:
                while right < len(nums) - 1 and nums[right] == 0:
                    right += 1
                nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right += 1
        return nums


if __name__ == '__main__':
    sol = Solution()
    s = [0]
    result = sol.moveZeroes(s)
    print(result)
