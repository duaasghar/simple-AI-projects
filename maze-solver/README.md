# Maze Solver

Navigating an ASCII maze from start to goal using A* search with a
Euclidean-distance heuristic.

## Problem

Given a text-based maze with walls (`#`), a start cell (`o`), and a goal
cell (`x`), find the shortest path between them.

- **State** — `(x, y)` coordinates on the grid.
- **Actions** — move up / down / left / right, provided the destination
  isn't a wall.
- **Path cost** — 1 per move.
- **Heuristic** — straight-line (Euclidean) distance to the goal, used by
  A* search.

## Approach

Implementation: [`maze_solver.py`](./maze_solver.py), using
[`simpleai`](https://github.com/simpleai-team/simpleai)'s A* search.

## Result

```
##############################
#         #              #   #
# ####    ########       #   #
#  o.#    # ........     #   #
#   .### ....####  .######   #
#   ......####     .#        #
#            #  #  .#   #### #
#     ######    #  .....#.x  #
#        #      #      ...   #
##############################
A* Search: moves=33, cost=33.0.
```

The `.` characters mark the discovered path from `o` to `x`.

## Discussion

Because every move costs exactly 1 and the heuristic is admissible, A*
here effectively behaves like an efficiently-guided breadth-first search —
it reaches the optimal 33-move solution while expanding far fewer nodes
than an uninformed search would, since the Euclidean-distance heuristic
consistently steers the search toward the goal.

## Running

```bash
pip install -r requirements.txt
python maze_solver.py
```
