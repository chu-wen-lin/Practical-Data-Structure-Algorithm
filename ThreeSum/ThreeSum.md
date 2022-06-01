**Task**: Find all the solutions of `a + b + c = 0` where `a`, `b`, `c` is from a int array(`nums`)

**Assumption**: the integers in array(`nums`) are distinct

**Output**: all possible solutions in a list. Solution should be a form of a three element int array `[a,b,c]`

Make sure

- There is no duplicated solution in the solution list
- The solution item is `[a,b,c]` where `a<b<c`
- (optional) The items in solution list should be in ascending order; items should be sorted by the first number in the item; if ties happen, use the next number to sort the item

**Example**

```python
>>> nums = [-1, 0, 1, 2, -2, -4]
>>> Solution().threeSum(nums)
[[-2, 0, 2], [-1, 0, 1]]

>>> nums = [0]
>>> Solution().threeSum(nums)
[]

>>> nums = list(range(-3, 10000))
>>> Solution().threeSum(nums)
[[-3, -2, 5], [-3, -1, 4], [-3, 0, 3], [-3, 1, 2], [-2, -1, 3], [-2, 0, 2], [-1, 0, 1]]
```

**Template**

```python
from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        return [[0, 1, 2]]
```

**Test Case**: Total 100 points. `N` refers to the size (or length) of `nums`.
- 20 points: `-5 < a, b < 5` and `N < 7`
- 20 points: `-20 < a, b < 20` and `N <= 100`. Special Cases
- 20 points: `|a, b, c| < 10` and `N <= 10`
- 20 points: `|a, b, c| < 100000` and `N <= 1000`
- 20 points: `|a, b, c| < 100000000` and `N <= 1000`

