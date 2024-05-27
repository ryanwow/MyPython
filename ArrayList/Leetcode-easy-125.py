# https://leetcode.cn/problems/valid-palindrome/description/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        i, j = 0, len(s) - 1
        while i < j:
            if not (s[i].isdigit() or s[i].isalpha()):
                i += 1
                continue
            elif not (s[j].isdigit() or s[j].isalpha()):
                j -= 1
                continue
            elif s[i] != s[j]:
                return False
            else:
                i += 1
                j -= 1
        return True


if __name__ == '__main__':
    S = Solution()
    s = 'A man, a plan, a canal: Panama'
    result = S.isPalindrome(s)
    print(result)
