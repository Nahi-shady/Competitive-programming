class Solution(object):
    def findMaxLength(self, nums):
        count = 0
        prefix = {0:0}
        subarray = 0
        for i in range(len(nums)):
            print(i)
            if nums[i] == 0:
                count -= 1
            else:
                count += 1

            if count == 0:
                subarray = i+1
            elif count in prefix:
                subarray = max(i - prefix[count], subarray)
            else:
                prefix[count] = i
        
        print(prefix)
        return subarray