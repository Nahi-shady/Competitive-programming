class Solution(object):
    def runningSum(self, nums):
        store = [nums[0],]
        for i in range(1, len(nums)):
            store.append(nums[i]+store[i-1])
        return store