class BackTracking:

    def is_valid_state(self, state):
        # check if it is a valid solution
        return True

    def get_candidates(self, state):
        return []

    def search(self, state, solutions):
        if self.is_valid_state(state):
            solutions.append(state.copy())
            return

        for candidate in self.get_candidates(state):
            state.add(candidate)
            self.search(state, solutions)
            state.remove(candidate)

    def solve(self):
        solutions = []
        state = set()
        self.search(state, solutions)
        return solutions
