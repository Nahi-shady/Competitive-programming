class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        ans = []
        def helper(l, arr, tot):
            if tot > target:
                return

            if tot == target:
                ans.append(arr.copy())
            
            for i in range(l, len(candidates)):
                arr.append(candidates[i])
                helper(i, arr, tot + candidates[i])
                arr.pop()

        helper(0, [], 0)

        return ans