from typing import List


class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        ans = 0
        cur_cost = maxCost
        left = 0

        for right in range(len(s)):
            cur_cost -= abs(ord(s[right]) - ord(t[right]))

            while cur_cost < 0 and left < right:
                cur_cost += abs(ord(s[left]) - ord(t[left]))
                left += 1

            if 0 <= cur_cost <= maxCost:
                ans = max(ans, right - left + 1)

        return ans


if __name__ == '__main__':
    sol = Solution()
    result = sol.equalSubstring("abcd", "bcdf", 3)
    print(result)
