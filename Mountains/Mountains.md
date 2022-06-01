**Task**: Given a N*M mountains with its height. What is the most energy-saving way when you go from `(0,0)` to `(N-1, M-1)`.

You can go from one mountain($M_{i}$) to another adjacent mountain($M_{j}$) by either up, down, left and right. The energy consumption can be calculated by

$$\left\{
\begin{aligned}
&height_{i} - height_{j},  &\text{if } height_{i} \geq height_{j} \\
&2(height_{j} - height_{i}), &\text{if } height_{i} < height_{j} \\
\end{aligned}
\right.
$$

Climbing up is more harder than going down, of course.

The total energy is the summation of the energy consumption along the path. Try to **find a path with the minimum total energy and output its value**.

---

**Hint**
- Shortest Path
- You can implement one of three algorithms(One of them may cause WA)
---

**Template** and **Example**
```python
from typing import List

class Mountains:
    def mountains(self, mountains_height: List[List[int]]) -> int:
        return 0


if __name__ == "__main__":
    print(Mountains().mountains(
        [[ 0, 1, 2, 3, 4], 
         [24,23,22,21, 5], 
         [12,13,14,15,16],
         [11,17,18,19,20],
         [10, 9, 8, 7, 6]]))
    # ans=42
    print(Mountains().mountains(
        [[3, 4, 5], 
         [9, 3, 5], 
         [7, 4, 3]]))
    # ans=6
```
Case 1
```
Mountains:
[[ 0,  1,  2,  3,  4],
 [24, 23, 22, 21,  5],
 [12, 13, 14, 15, 16],
 [11, 17, 18, 19, 20],
 [10,  9,  8,  7,  6]]
 
42 ->
From (0, 0)(height= 0) to (0, 1)(height= 1) takes  2 ; total:  2
From (0, 1)(height= 1) to (0, 2)(height= 2) takes  2 ; total:  4
From (0, 2)(height= 2) to (0, 3)(height= 3) takes  2 ; total:  6
From (0, 3)(height= 3) to (0, 4)(height= 4) takes  2 ; total:  8
From (0, 4)(height= 4) to (1, 4)(height= 5) takes  2 ; total: 10
From (1, 4)(height= 5) to (2, 4)(height=16) takes 22 ; total: 32
From (2, 4)(height=16) to (2, 3)(height=15) takes  1 ; total: 33
From (2, 3)(height=15) to (2, 2)(height=14) takes  1 ; total: 34
From (2, 2)(height=14) to (2, 1)(height=13) takes  1 ; total: 35
From (2, 1)(height=13) to (2, 0)(height=12) takes  1 ; total: 36
From (2, 0)(height=12) to (3, 0)(height=11) takes  1 ; total: 37
From (3, 0)(height=11) to (4, 0)(height=10) takes  1 ; total: 38
From (4, 0)(height=10) to (4, 1)(height= 9) takes  1 ; total: 39
From (4, 1)(height= 9) to (4, 2)(height= 8) takes  1 ; total: 40
From (4, 2)(height= 8) to (4, 3)(height= 7) takes  1 ; total: 41
From (4, 3)(height= 7) to (4, 4)(height= 6) takes  1 ; total: 42
```

Case 2
```
Mountains:
[[3, 4, 5],
 [9, 3, 5],
 [7, 4, 3]]
 
6 =>
From (0, 0)(height= 3) to (0, 1)(height= 4) takes  2; total:  2
From (0, 1)(height= 4) to (1, 1)(height= 3) takes  1; total:  3
From (1, 1)(height= 3) to (2, 1)(height= 4) takes  2; total:  5
From (2, 1)(height= 4) to (2, 2)(height= 3) takes  1; total:  6

or 
From (0, 0)(height= 3) to (0, 1)(height= 4) takes  2; total:  2
From (0, 1)(height= 4) to (0, 2)(height= 5) takes  2; total:  4
From (0, 2)(height= 5) to (1, 2)(height= 5) takes  0; total:  4
From (1, 2)(height= 5) to (2, 2)(height= 3) takes  2; total:  6
```
---

**Test Case** Total 100 Points. `0 <= height <= 1000` <BR>
- 20 points: N*M <= 30
- 20 points: N*M <= 10000(Special Case)
- 20 points: N*M <= 1000
- 20 points: N*M <= 100000
- 20 points: N*M <= 300000




