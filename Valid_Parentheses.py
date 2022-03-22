class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        parentheses = {'(':')', '{':'}','[':']'}
        stack = []
        for i in s:
            if i in parentheses:  
                stack.append(i)
            elif len(stack) == 0 or parentheses[stack.pop()] != i: 
                return False
        return len(stack) == 0 
	