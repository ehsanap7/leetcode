# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
from typing import List


class Solution:
    def reverseWords(self, s: str) -> str:
        left = 0
        right = 0

        list1 = list(s)
        list1.append(" ")

        while right < len(list1):

            if list1[right] == " ":
                target = right - 1
                while left < target:
                    list1[left], list1[target] = list1[target], list1[left]
                    left += 1
                    target -= 1
                right += 1
                left = right
            else:
                right += 1

        del list1[len(list1) - 1]
        return "".join(list1)


if __name__ == '__main__':
    sol = Solution()
    s = "God Ding"
    result = sol.reverseWords(s)
    print(result)
