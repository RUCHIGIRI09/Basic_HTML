class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        stack = []
        m = float('-inf')
        
        for i in nums[::-1]:
            if i < m:
                return True
            while stack and i > stack[-1]: 
                m = stack.pop()
            stack.append(i)
        return False