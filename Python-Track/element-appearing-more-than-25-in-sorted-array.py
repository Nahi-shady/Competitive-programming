class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        count = 0
        quarter = 0.25*len(arr)
        same_number = arr[0]

        for i in range(len(arr)):
            if arr[i] == same_number:
                count += 1
                if count > quarter:
                    return arr[i]
            else:
                count = 1
                same_number = arr[i]