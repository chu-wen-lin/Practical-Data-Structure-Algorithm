**Task**: Watson Industry(W.I.) has built lots of landmark buildings, such as tennis-racket home, welcome statue, PPP farm and Atlantis.

One day, the president, Watson, wants to give a tour for very important person came from Australia. The guest would like to visit all the landmarks on the minecart rather than walking. What is the minimum railway does Watson must to build?(Minecart can run on the railway in both direction)

To simplify the question, we have N landmarks with ID from `0` to `N-1`, and M distances with the form `[a, b, distance]` which indicates the distance from a to b in both direction.

You should return the minimum total distance of railway that connected all the landmarks.

---
**Hint**
- Minimum spanning tree
    1. Kruskal’s Algorithm
    2. Prim’s Algorithm
- Disjoint Set, priority-queue

Change the recursion limit in Python.
```python
import sys 
sys.setrecursionlimit(100001)
```
---

**Template** and **Example**
```python
from typing import List


class Railway():
    def __init__(self):
        pass
    
    def railway(self, landmarks:int, distance: List[List[int]]) -> int:
        return 0


if __name__ == "__main__":
    print(
    Railway().railway(4,[[0,1,2],
                         [0,2,4], 
                         [1,3,5], 
                         [2,1,1]])
    )
    # Minimum path: (0,1,2) (1,2,1) (1,3,5) -> 2 + 1 + 5 = 8
    # Answer: 8 

    print(
    Railway().railway(4,[[0,1,0],
                         [0,2,4], 
                         [0,3,4], 
                         [1,2,1], 
                         [1,3,4], 
                         [2,3,2]])
    )
    # Minimum path: (0,1,0) (1,2,1) (2,3,2) -> 0 + 1 + 2 = 3
    # Answer: 3
```
---
**Test Case**
- `N` is number of landmarks
- Landmark’s ID is bounded by `0 <= id < N`
- `M` is the number of path
- 0 <= distance <= 10000
- We do not guarantee there is only path from a to b.
- There may be a path from a to a (self-loop).
- We guarantee you can go to all the landmarks if you connect all the paths.

Total 100 points.

- 20 points: N <= 4, M <= 10
- 20 points: N <= 10001, M <= 20000. Special case
- 20 points: N <= 10, M <= 100
- 20 points: N <= 1000, M <= 100000
- 20 points: N <= 10000, M <= 1000000 

