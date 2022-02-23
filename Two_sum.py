class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res=[]
        #for i in range(0, len(nums)):
           # for j in range(i+1, len(nums)):
                #n = nums[i] + nums[j]
                #if n == target:
                   # res.append(i)
                    #res.append(j)
                  #  return res
        d= {}
        for i in range (0,len(nums)):
            b=nums[i]
            a=target-b
            if a in d:
                res.append(d[a])
                res.append(i)
                return res
            else:
                d[b]=i