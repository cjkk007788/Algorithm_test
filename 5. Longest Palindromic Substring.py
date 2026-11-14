class Solution:
    def longestPalindrome(self, s: str) -> str:

        if(len(s) == 0):
            return ""
        longest = ""
        for i in range(len(s)):
            for l,r in ((i,i),(i,i+1)):
                while(l>=0 and r<len(s) and s[l]==s[r]):
                    l -= 1
                    r += 1
                palindrome = s[l+1:r]
                if(len(palindrome) > len(longest)):
                    longest = palindrome

        return longest


if __name__ == "__main__":
    solution = Solution()
    # 테스트 케이스 1 ("aba"도 정답)
    print("Test 1:", solution.longestPalindrome("babad"))
    # 테스트 케이스 2
    print("Test 2:", solution.longestPalindrome("cbbd"))
    # 테스트 케이스 3 (한 글자)
    print("Test 3:", solution.longestPalindrome("a"))
    # 테스트 케이스 4 (빈 문자열)
    print("Test 4:", solution.longestPalindrome(""))
    # 테스트 케이스 5 (팰린드롬 없음)
    print("Test 5:", solution.longestPalindrome("ac"))
    # 테스트 케이스 6
    print("Test 6:", solution.longestPalindrome("forgeeksskeegfor"))