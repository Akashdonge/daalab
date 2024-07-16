class Solution(object):
    def numberOfPairs(self, nums1, nums2, diff):
        new_num = [a - b for i, (a, b) in enumerate(zip(nums1, nums2))]


        def rev(nums):
            if len(nums) == 1:
                return nums, 0
            mid = len(nums) // 2
            L = nums[:mid]
            R = nums[mid:]

            L, Lcnt = rev(L)
            R, Rcnt = rev(R)

            i = j = 0
            ans = Lcnt + Rcnt
            while i < len(L) and j < len(R):
                if L[i] <= R[j] + diff:
                    i += 1  
                    ans += len(R) - j
                else:
                    j +=1
            return sorted(L+R), ans
        
        return rev(new_num)[1]
                
