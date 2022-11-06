from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        head = 0
        tail = len(s) - 1
        while head < tail:
            s[head], s[tail] = s[tail], s[head]
            head += 1
            tail -= 1

# Complexity Analysis
#
# Time complexity : O(N)\mathcal{O}(N)O(N) to swap N/2N/2N/2 element.
#
# Space complexity : O(1)\mathcal{O}(1)O(1), it's a constant space solution.

if __name__ == '__main__':
    sol = Solution()
    nums = [1, 7, 3, 6, 5, 6]
    sol.reverseString(nums)
    print(nums)
