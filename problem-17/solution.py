WORD_MAPPING = {
    2: [['a'], ['b'], ['c']],
    3: [['d'], ['e'], ['f']],
    4: [['g'], ['h'], ['i']],
    5: [['j'], ['k'], ['l']],
    6: [['m'], ['n'], ['o']],
    7: [['p'], ['q'], ['r'], ['s']],
    8: [['t'], ['u'], ['v']],
    9: [['w'], ['x'], ['y'], ['z']],
}

class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        combinations = self._get_combinations(digits)
        return ["".join(comb) for comb in combinations]

    def _get_combinations(self, digits: str) -> list[list[str]]:
        if len(digits) == 0:
            return []

        if len(digits) == 1:
            return WORD_MAPPING[int(digits[0])]

        next_combinations = self._get_combinations(digits[1:])
        combinations = []
        for next_combination in next_combinations:
            for w in WORD_MAPPING[int(digits[0])]:
                combinations.append(
                    w + next_combination
                )

        return combinations