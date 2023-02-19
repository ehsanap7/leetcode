from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans = 999999999999999
        total = 0
        left = 0

        for right in range(0, len(nums)):
            if nums[right] >= target:
                ans = 1
                break
            total += nums[right]
            while total >= target:
                ans = min(ans, right - left + 1)
                total -= nums[left]
                left += 1

        return 0 if ans == 999999999999999 else ans

if __name__ == '__main__':
    sol = Solution()
    result = sol.minSubArrayLen(7, [2, 3, 1, 2, 4, 3])
    print(result)
