from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ans = 0

        count = 0

        for i in range(len(gain)):
            count += gain[i]
            ans = max(ans, count)

        return ans


if __name__ == '__main__':
    sol = Solution()
    result = sol.largestAltitude(
        [44, 32, -9, 52, 23, -50, 50, 33, -84, 47, -14, 84, 36, -62, 37, 81, -36, -85, -39, 67, -63, 64, -47, 95, 91,
         -40, 65, 67, 92, -28, 97, 100, 81])
    print(result)
