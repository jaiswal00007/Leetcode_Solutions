class Solution(object):
    def minEnd(self, n, x):
        """
        :type n: int
        :type x: int
        :rtype: int
        """
        mxbit = n.bit_length() + x.bit_length()
        k = n - 1
        index = 0

        for i in range(mxbit):
            if x >> i & 1 == 0:
                if k >> index & 1:
                    x |= 1 << i
                index += 1

        return x
            
