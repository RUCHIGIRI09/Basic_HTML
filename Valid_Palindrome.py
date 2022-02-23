class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s=s.lower()
        str=''
        for i in s:
            if i.isalnum():
                str += i
        return str == str[: : -1]
        