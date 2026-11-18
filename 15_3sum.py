##time excceds 
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:

        def merge_sort(array):

            if len(array) <= 1:
                return array
            mid = len(array)//2

            low_arr = merge_sort(array[:mid])
            high_arr = merge_sort(array[mid:])

            l = h = 0
            merge_array = []
            while l < len(low_arr) and h < len(high_arr):
                if low_arr[l] < high_arr[h]:
                    merge_array.append(low_arr[l])
                    l = l + 1
                else:
                    merge_array.append(high_arr[h])
                    h = h + 1

            merge_array = merge_array + low_arr[l:]
            merge_array = merge_array + high_arr[h:]

            return merge_array

        sorted_list = merge_sort(nums)


        def binary_search(target,low,high):

            while low<=high:
                mid = (low + high)//2

                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid -1
            
            return -1


        result = []

        nums = merge_sort(nums)
        n = len(nums)
        for i in range(n-2):
            if nums[i] > 0 :
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue

            for j in range(i+1,n-1):
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue
                target = -(nums[i] + nums[j])
                if binary_search(target,j+1,n-1) != -1:
                    result.append([nums[i],nums[j],target])
                
        return result


class Soultion2:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = []
        n = len(nums)

        for i in range(n-2):

            if nums[i] > 0:
                break

            if i > 0 and nums[i] == nums[i-1]:
                continue

            l = i + 1
            h = n-1

            while l < h:
                sum = nums[i] + nums[l] + nums[h]
                if sum < 0 :
                    l+=1
                elif sum > 0:
                    h -=1
                else:
                    result.append([nums[i],nums[l],nums[h]])
                    l = l + 1
                    h = h - 1

                    while l < h and nums[l] == nums[l-1]:
                        l = l + 1
                    while l < h and nums[h] == nums[h+1]:
                        h = h - 1
            return result
        
