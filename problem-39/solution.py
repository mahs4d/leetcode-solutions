class Solution:
    def __init__(self):
        self._cache = {}

    def _get_combinations(self, candidates: list[int], target: int) -> list[list[int]]:
        if target in self._cache:
            return self._cache[target]
        
        if target == 0:
            return [[]]

        if target < 0:
            return []
        
        result = []
        for candidate in candidates:
            combinations = self._get_combinations(
                candidates=candidates,
                target=target - candidate
            )
            for combination in combinations:
                result.append(combination + [candidate])
        
        self._cache[target] = result
        return result


    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        result = self._get_combinations(
            candidates=set(sorted(candidates, reverse=True)),
            target=target,
        )
        return [list(y) for y in set([tuple(sorted(x)) for x in result])]
