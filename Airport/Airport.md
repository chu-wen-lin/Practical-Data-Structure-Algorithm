**Scenario**: There is a small town with *n* houses. The town needs an airport. An airport is basically a very long, very straight road. Think of it as an infinite line. We need to build the airport such that the **average distance from each house to the airport is as small as possible**. However, no one wants to walkacross the runway, so all of the houses must be on the same side of the airport. (Some houses may be a distance of zero away from the runway, but that’s ok. We’ll give them some free ear plugs.) 

**Question**: Where should we build the airport, and what will be the average distance?

**Hint**: 
- Convex Hull
- Formula for the distance between a point and a line
---

**Template** and **Example**

```python
from typing import List
import math


class Airport:
    def airport(self, houses: List[List[int]]) -> float:
        """
        Find the best place to build airport and
        calculate the average distance from all the house to airport

        Parameters:
            houses(list[list[int]]): List of houses.
                Each house contains [x,y] coordination.

        Returns:
            distance(float)
        """
        return 0

    
if __name__ == "__main__":
    print(Airport().airport([[0,0],[1,0]]))
    """
    0.0
    """
    print(Airport().airport([[0,0],[1,0],[0,1]]))
    """
    *.
    **
    # Convex: [[0, 0], [1, 0], [0, 1]]
    0.2357022603955159
    """
    print(Airport().airport([[0,0],[2,0],[0,2],[1,1],[2,2]]))
    """
    *.*
    .*.
    *.*
    # Convex: [[0, 0], [2, 0], [2, 2], [0, 2]]
    1.0
    """
    print(Airport().airport([[1,1],[2,2],[0,2],[2,0],[2,4],[3,3],[4,2],[4,1],[4,0]]))
    """
    ..*..
    ...*.
    *.*.*
    .*..*
    ..*.*
    # Convex: [[0, 2], [2, 0], [4, 0], [4, 2], [2, 4]]
    1.3356461422412562
    """
```

---

**Test Case**: Total 100 points. <BR> 
1. `0 <= x, y <= M`, `x` and `y` are integer. We guarantee the coordinates are unique.
2. `N` is the number of houses
3. We will check your answer by `abs(output - answer) <= 1e-4`.

- 20 points: `N = 10`, `M <= 100`
- 20 points: `N = 60000`, `M < 1000000`. Special Case(Four samples)
- 20 points: `N = 100`, `M <= 10`
- 20 points: `N = 1000`, `M <= 1000`
- 20 points: `N = 100000`, `M <= 100000`