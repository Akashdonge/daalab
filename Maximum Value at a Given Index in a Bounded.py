class Solution(object):
    def maxValue(self, n, index, maxSum):
        def test(a):
            b = max(a - index, 0)
            res = (a + b) * (a - b + 1) / 2
            b = max(a - ((n - 1) - index), 0)
            res += (a + b) * (a - b + 1) / 2
            return res - a

        maxSum -= n
        left, right = 0, maxSum
        while left < right:
            mid = (left + right + 1) / 2
            if test(mid) <= maxSum:
                left = mid
            else:
                right = mid - 1
        return left + 1
        """
        :type n: int
        :type index: int
        :type maxSum: int
        :rtype: int
        """
