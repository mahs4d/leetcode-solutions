class Solution:
    def __init__(self):
        self._combinations = []

    def _backtrack(self, candidates: list[int], combination: list[int], index: int, remaining: int):
        if remaining == 0:
            self._combinations.append(list(combination))
            return
        
        if index >= len(candidates):
            return
        
        if remaining < 0:
            return

        # Pick candidates[index]
        candidate = candidates[index]
        combination.append(candidate)
        self._backtrack(
            candidates=candidates,
            combination=combination,
            index=index,
            remaining=remaining - candidate,
        )
        combination.pop()
        self._backtrack(
            candidates=candidates,
            combination=combination,
            index=index+1,
            remaining=remaining,
        )

    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        self._backtrack(
            candidates=sorted(set(candidates)),
            combination=[],
            index=0,
            remaining=target,
        )
        return self._combinations
    


print(Solution().combinationSum([2,3,5], 8))