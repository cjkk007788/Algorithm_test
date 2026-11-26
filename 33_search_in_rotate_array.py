class Solution:
    def search(self, nums: list[int], target: int) -> int:

        n = len(nums)

        #find pivot --> mid를 큰것과 비교해서 방향이 사이에서 전환 되었는지 확인


        lo, hi = 0, n-1

        while lo < hi:
            mid = (lo + hi) // 2

            if nums[mid] > nums[hi]:
                lo = mid + 1
            else:
                hi = mid
        
        
        pivot = lo

        lo = 0, hi = n-1

        while lo <= hi:
            v = (lo + hi) //2 
            real = (v + pivot) % n

            if nums[real] ==target:
                return real
            elif nums[real]< target:
                lo = v + 1
            else:
                hi = v -1

        return - 1

