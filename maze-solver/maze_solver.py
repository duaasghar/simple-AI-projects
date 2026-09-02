"""
Task 2.3 - Maze Solver
======================
An ASCII maze is solved with A* search, navigating from a start cell ('o')
to a goal cell ('x') while avoiding walls ('#').

Requires: pip install simpleai
"""

import math
from simpleai.search import SearchProblem, astar

MAP = """
##############################
#         #              #   #
# ####    ########       #   #
#  o #    #              #   #
#    ###     ####   ######   #
#         ####      #        #
#            #  #   #   #### #
#     ######    #       # x  #
#        #      #            #
##############################
"""
MAP = [list(row) for row in MAP.split("\n") if row]

COSTS = {
    "up": 1.0,
    "down": 1.0,
    "left": 1.0,
    "right": 1.0,
}


class Maze(SearchProblem):
    """Grid-based maze search problem."""

    def __init__(self, board):
        self.board = board
        self.goal = (0, 0)
        for y in range(len(self.board)):
            for x in range(len(self.board[y])):
                if self.board[y][x].lower() == "o":
                    self.initial = (x, y)
                elif self.board[y][x].lower() == "x":
                    self.goal = (x, y)

        super(Maze, self).__init__(initial_state=self.initial)

    def actions(self, state):
        actions = []
        for action in list(COSTS.keys()):
            newx, newy = self.result(state, action)
            if self.board[newy][newx] != "#":
                actions.append(action)
        return actions

    def result(self, state, action):
        x, y = state
        if "up" in action:
            y -= 1
        if "down" in action:
            y += 1
        if "left" in action:
            x -= 1
        if "right" in action:
            x += 1
        return (x, y)

    def is_goal(self, state):
        return state == self.goal

    def cost(self, state, action, state2):
        return COSTS[action]

    def heuristic(self, state):
        """Straight-line (Euclidean) distance to the goal."""
        x, y = state
        gx, gy = self.goal
        return math.sqrt((x - gx) ** 2 + (y - gy) ** 2)


def solve() -> None:
    problem = Maze(MAP)
    result = astar(problem, graph_search=True)

    path = [x[1] for x in result.path()]
    for y in range(len(MAP)):
        for x in range(len(MAP[y])):
            print("." if (x, y) in path[1:-1] else MAP[y][x], end="")
        print()
    print("A* Search: moves=%s, cost=%s." % (result.depth, result.cost))


if __name__ == "__main__":
    solve()
