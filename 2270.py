from typing import List


class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        prefix = [nums[0]]
        for i in range(1, len(nums)):
            prefix.append(nums[i] + prefix[-1])
        count_result = 0
        for i in range(0, len(nums) - 1):
            if prefix[i] >= prefix[- 1] - prefix[i]:
                count_result += 1
        return count_result


if __name__ == '__main__':
    sol = Solution()
    nums = [10, 4, -8, 7]
    result = sol.waysToSplitArray(nums)
    print(result)
