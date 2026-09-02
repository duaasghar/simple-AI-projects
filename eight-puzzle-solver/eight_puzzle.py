"""
Task 2.2 - 8-Puzzle Problem
===========================
Classic sliding-tile puzzle: a 3x3 grid holds tiles numbered 1-8 and one
blank space ('E'). The goal is to reach the ordered configuration using
the fewest moves, solved here with A* search and a Manhattan-distance
heuristic.

Requires: pip install simpleai
"""

from simpleai.search import SearchProblem, astar

GOAL = "1-2-3\n4-5-6\n7-8-E"

# Solvable starting configuration (solution depth = 8 moves).
INITIAL = "1-4-2\n5-E-8\n3-6-7"


def list_to_string(input_list):
    return "\n".join(["-".join(row) for row in input_list])


def string_to_list(input_string):
    return [row.split("-") for row in input_string.split("\n")]


def get_location(rows, element):
    for i, row in enumerate(rows):
        for j, item in enumerate(row):
            if item == element:
                return i, j


# Cache the goal position of every tile so the heuristic can be computed
# in O(1) per tile.
_goal_rows = string_to_list(GOAL)
GOAL_POSITIONS = {tile: get_location(_goal_rows, tile) for tile in "12345678E"}


class PuzzleSolver(SearchProblem):
    """8-puzzle search problem, solved by sliding the blank tile."""

    def actions(self, cur_state):
        """Return the tile values that can legally slide into the blank."""
        rows = string_to_list(cur_state)
        row_empty, col_empty = get_location(rows, "E")

        actions = []
        if row_empty > 0:
            actions.append(rows[row_empty - 1][col_empty])
        if row_empty < 2:
            actions.append(rows[row_empty + 1][col_empty])
        if col_empty > 0:
            actions.append(rows[row_empty][col_empty - 1])
        if col_empty < 2:
            actions.append(rows[row_empty][col_empty + 1])
        return actions

    def result(self, state, action):
        """Swap the chosen tile with the blank space."""
        rows = string_to_list(state)
        row_empty, col_empty = get_location(rows, "E")
        row_new, col_new = get_location(rows, action)
        rows[row_empty][col_empty], rows[row_new][col_new] = (
            rows[row_new][col_new],
            rows[row_empty][col_empty],
        )
        return list_to_string(rows)

    def is_goal(self, state):
        return state == GOAL

    def heuristic(self, state):
        """Sum of Manhattan distances of every tile from its goal position."""
        rows = string_to_list(state)
        distance = 0
        for number in "12345678E":
            row_new, col_new = get_location(rows, number)
            row_goal, col_goal = GOAL_POSITIONS[number]
            distance += abs(row_new - row_goal) + abs(col_new - col_goal)
        return distance


def solve() -> None:
    result = astar(PuzzleSolver(INITIAL))

    for i, (action, state) in enumerate(result.path()):
        print()
        if action is None:
            print("Initial configuration")
        else:
            print("Step %s: After moving %s into the empty space" % (i, action))
        print(state)
    print("Goal achieved!")


if __name__ == "__main__":
    solve()
