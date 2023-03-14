class Solution(object):
    def pivotIndex(self, nums):
        total_sum = sum(nums)  # sum of all num in array
        left_sum = 0.0  # sum of all num from left side

        for i in range(len(nums)):
            if left_sum == total_sum - left_sum - nums[i]: # decrementing and checking left to right 
                return i
            left_sum += nums[i] #incrementing the value to check values 

        return -1 # if no pivot print -1