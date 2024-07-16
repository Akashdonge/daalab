class Solution(object):
    def maxSumOfThreeSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(nums)
        if n < 3 * k:
            return []
        
        # Calculate the prefix sums for the subarray sums of length k
        subarray_sum = [0] * (n - k + 1)
        current_sum = sum(nums[:k])
        
        for i in range(n - k + 1):
            if i == 0:
                subarray_sum[i] = current_sum
            else:
                current_sum = current_sum - nums[i - 1] + nums[i + k - 1]
                subarray_sum[i] = current_sum

        # Find the best left and right max sums
        left_max = [0] * (n - k + 1)
        right_max = [0] * (n - k + 1)
        
        left_max_index = 0
        for i in range(n - k + 1):
            if subarray_sum[i] > subarray_sum[left_max_index]:
                left_max_index = i
            left_max[i] = left_max_index

        right_max_index = n - k
        for i in range(n - k, -1, -1):
            if subarray_sum[i] >= subarray_sum[right_max_index]:
                right_max_index = i
            right_max[i] = right_max_index

        # Find the maximum sum of three non-overlapping subarrays
        max_sum = 0
        result_indices = []

        for j in range(k, n - 2 * k + 1):
            left_index = left_max[j - k]
            right_index = right_max[j + k]
            current_sum = subarray_sum[left_index] + subarray_sum[j] + subarray_sum[right_index]
            
            if current_sum > max_sum:
                max_sum = current_sum
                result_indices = [left_index, j, right_index]

        return result_indices
