class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l, r = 0, len(letters)-1
        while l < r:
            mid = (l+r)//2
            print(mid)
            if letters[mid] > target:
                r = mid
            else:
                l = mid + 1

        return letters[r] if letters[-1] > target else letters[0]