"""
Task 2.1 - Route Planning
=========================
Six cities are connected by roads of varying cost. We compare three
uninformed search strategies (breadth-first, depth-first, and uniform-cost
search) for finding a route between city 1 and city 5, and show that only
uniform-cost search is guaranteed to find the optimal (cheapest) route.

Requires: pip install simpleai
"""

from simpleai.search import SearchProblem, breadth_first, depth_first, uniform_cost

# Distance matrix between the 6 cities. 'inf' means no direct connection,
# 0 means "self" (diagonal).
COSTS = [
    [0, 7, 9, 'inf', 'inf', 14],
    [7, 0, 10, 15, 'inf', 'inf'],
    [9, 10, 0, 11, 'inf', 2],
    ['inf', 15, 11, 0, 6, 'inf'],
    ['inf', 'inf', 'inf', 6, 0, 9],
    [14, 'inf', 2, 'inf', 9, 0],
]


class Route(SearchProblem):
    """Search problem representing travel between numbered cities."""

    def __init__(self, initial, goal):
        # "-1" because the cities are numbered from 1, but the cost
        # matrix is zero-indexed.
        self.initial = initial - 1
        self.goal = goal - 1
        super(Route, self).__init__(initial_state=self.initial)

    def actions(self, state):
        """Return all directly connected cities (cost not 0 or 'inf')."""
        return [
            action
            for action in range(len(COSTS[state]))
            if COSTS[state][action] not in ('inf', 0)
        ]

    def result(self, state, action):
        return action

    def is_goal(self, state):
        return state == self.goal

    def cost(self, state, action, state2):
        return COSTS[state][action]


def solve(initial: int = 1, goal: int = 5) -> None:
    problem = Route(initial, goal)

    result_bfs = breadth_first(problem, graph_search=True)
    result_dfs = depth_first(problem, graph_search=True)
    result_ucs = uniform_cost(problem)

    path_bfs = [x[1] + 1 for x in result_bfs.path()]
    print("The BFS route is %s, and total cost is %s" % (path_bfs, result_bfs.cost))

    path_dfs = [x[1] + 1 for x in result_dfs.path()]
    print("The DFS route is %s, and total cost is %s" % (path_dfs, result_dfs.cost))

    path_ucs = [x[1] + 1 for x in result_ucs.path()]
    print("The UCS route is %s, and total cost is %s" % (path_ucs, result_ucs.cost))


if __name__ == "__main__":
    solve()
