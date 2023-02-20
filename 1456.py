from typing import List


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        count = 0
        vowel_letters = ['a', 'e', 'i', 'o', 'u']

        for i in range(k):
            if s[i] in vowel_letters:
                count += 1

        ans = count

        for left in range(0, len(s) - k):
            if s[left] in vowel_letters:
                count -= 1
            if s[left + k] in vowel_letters:
                count += 1

            ans = max(ans, count)

        return ans


if __name__ == '__main__':
    sol = Solution()
    result = sol.maxVowels("weallloveyou", 7)
    print(result)
