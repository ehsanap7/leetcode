from typing import List


class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        left = 0
        right = 0

        list1 = list(word)

        while right < len(list1):

            if list1[right] == ch:
                while left < right:
                    list1[left], list1[right] = list1[right], list1[left]
                    left += 1
                    right -= 1
                return "".join(list1)

            right += 1

        return "".join(list1)


if __name__ == '__main__':
    sol = Solution()
    result = sol.reversePrefix("abcdefd", "d")
    print(result)
