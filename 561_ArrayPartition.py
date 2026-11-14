class Solution:
    def arrayPairSum(self, nums: list[int]) -> int:
        nums.sort()
        print(nums)
        sum = 0
        for i in range(len(nums)):
            if(i%2==0):
                sum += nums[i]
        return sum

nums = [1,4,3,2]

soul = Solution()
result = soul.arrayPairSum(nums)

print(result)