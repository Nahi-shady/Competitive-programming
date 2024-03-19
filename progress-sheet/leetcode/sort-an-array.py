class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def merge(left, right):
            n, m = 0, 0
            merged = []
            while n < len(left) and m < len(right):
                if left[n] <= right[m]:
                    merged.append(left[n])
                    n += 1
                else:
                    merged.append(right[m])
                    m += 1
            merged.extend(left[n:])
            merged.extend(right[m:])

            return merged
        
        def mergeSort(l, r):   
            if l == r:
                return [nums[r]]

            mid = (l+r) // 2
            left = mergeSort(l, mid)
            right = mergeSort(mid+1, r)

            return merge(left, right)


        return mergeSort(0, len(nums)-1)