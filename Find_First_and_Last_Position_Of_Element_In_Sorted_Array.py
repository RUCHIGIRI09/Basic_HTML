class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def search(x): 
            first = len(nums)
            last = 0
            while last < first:
                mid = (last + first) // 2
                if nums[mid] < x:
                    last = mid+1
                else:
                    first = mid                    
            return last
        
        last = search(target)
        first = search(target+1)-1
        
        if last <= first:
            return [last, first]
                
        return [-1, -1]