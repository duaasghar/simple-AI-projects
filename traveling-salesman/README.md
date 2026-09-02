# Traveling Salesman Problem (Genetic Algorithm)

Solving a 17-city instance of the classic Travelling Salesman Problem
using an evolutionary algorithm built with
[DEAP](https://deap.readthedocs.io/).

## Problem

Given 17 cities and the distances between every pair, find the shortest
possible round-trip route that visits every city exactly once and returns
to the start.

## Approach

- **Representation** — a tour is a permutation of the 17 city indices.
- **Fitness function** — total round-trip distance (to minimise), summing
  consecutive city-to-city distances from a pre-computed distance matrix.
- **Genetic operators**:
  - *Selection* — tournament selection (`tournsize=3`)
  - *Crossover* — partially matched crossover (`cxPartialyMatched`), which
    preserves permutation validity
  - *Mutation* — shuffle indexes with `indpb=0.05`
- **Parameters** — population of 500 individuals, evolved for 50
  generations, with crossover probability 0.7 and mutation probability 0.2.

Implementation: [`traveling_salesman_ga.py`](./traveling_salesman_ga.py)

## Result

The GA's minimum tour distance converges to **2085**, matching the known
optimal distance for this 17-city instance:

```
gen  min
0    3369
...
35   2085   (converged)
50   2085
```

## Discussion

The population's best fitness improves steadily across generations and
converges to the global optimum by generation 35, remaining stable for the
rest of the run — a good sign that the selection/crossover/mutation
combination is exploring the search space effectively without premature
convergence.

## Running

```bash
pip install -r requirements.txt
python traveling_salesman_ga.py
```
