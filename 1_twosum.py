class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        
        for i in range(len(nums)):
            for j in range(i , len(nums)):
                if nums[i] + nums[j] == target:
                    result = [i,j]
                    return result


if __name__ == "__main__":
    solution = Solution()
    # 테스트 케이스 1 (정답: [0, 1])
    print("Test 1:", solution.twoSum([2, 7, 11, 15], 9))
    # 테스트 케이스 2 (정답: [1, 2])
    print("Test 2:", solution.twoSum([3, 2, 4], 6))
    # 테스트 케이스 3 (정답: [0, 1])
    print("Test 3:", solution.twoSum([3, 3], 6))