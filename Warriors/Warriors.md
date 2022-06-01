**Task**:
There are warriors standing in a line. Each warrior has two important properties: **STH** and **RNG**. **STH** stands for “strength”, the power of each warrior. **RNG** stands for Range, the effective radius that the warrior can attack.
Suppose that there are *N* warriors in this contest. An index i indicates one’s position (an integer coordinate). An attack will be blocked if there is a warrior with a higher or equal **STH** within the **RNG** distance. 
Formally speaking, let $\{s_0, s_1, ..., s_{N-1}\}$ be the sequence of **STH** for the *N* warriors, and $\{r_0, r_1, ..., r_{N-1}\}$ be the sequence of **RNG** for them, then the *i*-th warrior can attack the *j*-th warrior if and only if the following conditions are satisfied:
- $|j-i|\leq r_{i}$
- $s_{j} < s_{i}$
- $\{s_{k}\} < s_{i}, \forall k $ between $i$ and $j$
- $a_{i} =$ the index of the leftmost standing warrior that the *i*-th warrior can attack
- $b_{i} =$ the index of the rightmost standing warrior that the *i*-th warrior can attack

Please determine the sequence of pairs $\{(a_{0}, b_{0}), ..., (a_{N-1}, b_{N-1})\}$.
To simplify the edge case, a warrior can attach itself.

---

**Hint**:
- Stack
- Use two for-loops from left to right and then from right to left
- Firstly compare the strength without limiting the range(regardless of the range)

---
**Template**
```python
from typing import List

class Warriors: 
    def warriors(self, strength :List[int], attack_range :List[int]):
        """
        Given the attributes of each warriors and output the minimal and maximum
        index of warrior can be attacked by each warrior.

        Parameters:
          strength (List[int]): The strength value of N warriors
          attack_range (List[int]): The range value of N warriors

        Returns:
          attack_interval (List[int]):
              The min and the max index that the warrior can attack.
              The format of output is 2N int array `[a0, b0, a1, b1, ...]`
        """
        return []
```
---
**Example**
```python
if __name__ == "__main__":
    sol = Warriors()
    print(sol.warriors([11, 13, 11, 7, 15],
                       [ 1,  8,  1, 7,  2]))
    """
    # Output
    [0, 0, 0, 3, 2, 3, 3, 3, 2, 4]
    """
```
---

**Test Case**: Total 100 points. `N` is the number of warriors.
1. `0 <= strength <= 1000000000`
2. `0 <= attack_range <= M`
3. `1 <= N`
<BR>
- 20 points: `N <= 10`, `M < 10`
- 20 points: `N <= 200000`, `M <= 200000`. Special case
- 20 points: `N <= 10000`, `M <= 5000`
- 20 points: `N <= 400000`, `M <= 200000`
- 20 points: `N <= 1000000`, `M <= 500000`