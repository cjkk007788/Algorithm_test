class Solution:
    def isPalindrome(self, x: int) -> bool:


        if x< 0:
            return False
        
        number_str = str(x)

        #뒤집는 코드
        number_str_reverse = number_str[::-1]
        return number_str == number_str_reverse

if __name__ == "__main__":
    sol = Solution()


    test_cases = [ 
        (121,True),
        (10,False),
        (-33,False),
        (13131,True),
    ]

    for test in test_cases:

        if(sol.isPalindrome(test[0])):
            print(f"{test[0]} is Palindrome")
        else:
            print(f"{test[0]} is not Palindrome")

