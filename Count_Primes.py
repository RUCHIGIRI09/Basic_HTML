class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        val = [0] * n
        count = 0
        for num in range(2, n):
            if val[num]: continue
            count += 1
            val[num*num:n:num] = [1] * ((n - 1) // num - num + 1)
        return count