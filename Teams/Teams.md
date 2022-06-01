**Task**: You are the manager that runs an idol group similar to AKB48. One day, you want to hold a sport competition.

The competition separates idols into two groups, the red team and the white team. The only constraint is that there is no tee-tee (てぇてぇ) pair in the same team.

Tee-tee means two idols have better relationship and always cooperate with each other.

To make this question easier, each idol has her ID and
we will give you a list of tee-tees pair and ask you if you can separate the idols into two groups or not.

---

**Hint**
- Bipartite Graph
- BFS and DFS both works, but dfs has recursion overhead(Especially for Python user).
- Create your graph with Adjacency List
- For java users, Linked-list is the best suitable structure for graph
- To avoid stackoverflow in Java, we can specific your stack memory when execution https://docs.oracle.com/cd/E13150_01/jrockit_jvm/jrockit/jrdocs/refman/optionX.html e.g. `java -Xss10M -cp algs4.jar:. Teams`

---

**Template** and **Example**
```python
from typing import List

class Teams:
    def teams(self, idols: int, teetee: List[List[int]]) -> bool:
        return False


if __name__ == "__main__":
    # example 1: True
    print(Teams().teams(4, [[0,1],[0,3],[2,1],[3,2]]))
    # example 2: False
    print(Teams().teams(4, [[0,1],[0,3],[0,2],[2,1],[3,2]]))
```

Example 1 <BR>
<BR>
![Example 1](Example%201.jpeg)

Red teams: 0, 2 <BR>
White teams: 1, 3

Example 2 <BR>
<BR>
![Example 2](Example%202.jpeg)

Red teams: 0, 2 -> violate the rule, (0,2) are tee-tee pair.
White teams: 1, 3
Actually no combination can be found, so return False.

---

**Test Case**
- `N` is number of idols
- Idol’s ID is bounded by `0 <= id < N`
- `M` is the number of tee-tee pair
- We guarantee tee-tee pair are not duplicated, and cannot tee-tee herself.

Total 100 points.

- 20 points: N <= 4, M <= N*N
- 20 points: N <= 10000, M <= 15000. Special case
- 20 points: N <= 1000, M <= 1000
- 20 points: N <= 10000, M <= 10000
- 20 points: N <= 100000, M <= 400000


