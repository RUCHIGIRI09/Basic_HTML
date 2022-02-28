class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        beg = 0
        end=(len(nums)-1)
        
        while beg<=end:
            
            mid=end + (beg - end)//2
            
            if nums[mid]== target:
                return mid
        
            elif nums[mid]>target:
                end=mid-1
            else:
                beg=mid+1
                
        return -1
