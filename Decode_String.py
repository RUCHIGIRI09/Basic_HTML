class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        string = []
        
        for i in range(len(s)):
            if s[i] != ']':
                string.append(s[i])
            else:
                sub_string = ''
                
                while string[-1] != '[':
                    
                    sub_string = string.pop() + sub_string
                string.pop()
                
                k= ''
                while string and string[-1].isdigit():
                    
                    k = string.pop() + k
                string.append(int(k) * sub_string)
                
        return "".join(string)
                    
    