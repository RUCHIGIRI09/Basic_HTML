class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        index = 0
        val = len(nums)-1
        while index<= val:
            mid = (index+val)/2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                index = mid+1
            else:
                val = mid-1
        return index
            
        