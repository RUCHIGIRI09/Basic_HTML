roman ={'I':1 ,'V':5 , 'X':10 , 'L':50 , 'C':100 , 'D':500 , 'M':1000}
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        #roman ={'I':1 ,'V':5 , 'X':10 , 'L':50 , 'C':100 , 'D':500 , 'M':1000}
        #i=0
        sum=0
        #while i<len(s):
           # if i+1<len(s) and s[i:i+2] in roman:
            #    num +=roman[s[i:i+2]]
             #   i +=2
            #else:
             #   num +=roman[s[i]]
              #  i+=1
        for i in range(len(s)-1,-1,-1):
            num= roman[s[i]]
            if 3*num<sum:
                sum=sum-num
            else:
                sum=sum+num
        return sum