from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

        left = 0
        right = 0
        result = []

        while(left < m and right < n):
            if(nums1[left]<=nums2[right]):
                result.append(nums1[left])
                left = left + 1

            else:
                result.append(nums2[right])
                right = right + 1
        if(left<m):
            result = result + nums1[left:m]
        if(right<n):
            result = result + nums2[right:n]
        nums1[:] = result
            
