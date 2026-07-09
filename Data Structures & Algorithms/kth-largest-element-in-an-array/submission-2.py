import random

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        k = len(nums) - k
        resIndex = 0
        left, right = 0, len(nums) - 1

        while left <= right:
            pivotIndex = random.randint(left, right)
            nums[right], nums[pivotIndex] = nums[pivotIndex], nums[right]
            pivot = nums[right]
            p = left

            for index in range(left, right):
                if nums[index] < pivot:
                    nums[p], nums[index] = nums[index], nums[p]
                    p += 1
            
            nums[p], nums[right] = nums[right], nums[p]

            if k < p:
                right = p - 1
            elif k > p:
                left = p + 1
            else:
                resIndex = p
                break

        return nums[resIndex]