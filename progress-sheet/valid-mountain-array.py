class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False

        increasing = False
        decreasing = False

        for i in range(1, len(arr)):
            if decreasing:
                if arr[i-1] <= arr[i]:
                    return False
            else:
                if arr[i-1] > arr[i]:
                    decreasing = True
                elif arr[i-1] < arr[i]:
                    increasing = True
                else:
                    return False
                    
        return increasing and decreasing