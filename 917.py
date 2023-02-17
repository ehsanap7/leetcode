# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
from typing import List


class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        left = 0
        right = len(s) - 1

        list1 = list(s)

        while left < right:
            if list1[left].isalpha() and list1[right].isalpha():
                list1[left], list1[right] = list1[right], list1[left]
                left += 1
                right -= 1
            elif list1[left].isalpha():
                right -= 1
            elif list1[right].isalpha():
                left += 1
            else:
                left += 1
                right -= 1

        return "".join(list1)


if __name__ == '__main__':
    sol = Solution()
    s = "-S2,_"
    result = sol.reverseOnlyLetters(s)
    print(result)
