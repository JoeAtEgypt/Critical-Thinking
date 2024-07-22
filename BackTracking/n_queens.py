from template import *
from typing import List


class Solution:
    def is_valid_state(self, state, n):
        # check if it is a valid solution
        return n == len(state)

    def get_candidates(self, state, n):
        if not state:
            return range(n)

        positions = len(state)
        candidates = set(range(n))

        for row, col in enumerate(state):
            candidates.discard(col)

            dist = positions - row

            candidates.discard(col + dist)
            candidates.discard(col - dist)

        return candidates

    def state_to_str(self, state, n):
        # ex: [1, 3, 0, 2]
        # to: [".Q..", "...Q", "Q...", "..Q."]
        strs = []
        for index in state:
            s = "." * index + "Q" + "." * (n - index - 1)
            strs.append(s)
        return strs

    def search(self, state, solutions, n):
        if self.is_valid_state(state, n):
            solutions.append(self.state_to_str(state, n))
            return

        for candidate in self.get_candidates(state, n):
            state.append(candidate)
            self.search(state, solutions, n)
            state.pop()

    def solveNQueens(self, n: int) -> List[List[str]]:
        solutions = []
        state = []
        self.search(state, solutions, n)
        return solutions


n = int(input())
sol = Solution().solveNQueens(n)
print(sol)
