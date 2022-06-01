**Task**: Find the only one solution of `nums[a] + nums[b] = target` where a, b is the index of the value from an int array(`nums`) and target is also an integer(`target`)

**Assumption**: the integers in array(`nums`) are distinct

**Output**: an int array with two elements (`[a,b]`) where `a<b`

**Example**
```python
>>> nums = [2,7,11,15]
>>> target = 9
>>> Solution().twoSum(nums, target)
[0, 1]
# 2 + 7 = 9

>>> nums = [3,2,4]
>>> target = 6
>>> Solution().twoSum(nums, target)
[1, 2]
# 2 + 4 = 6

>>> nums = list(range(1000))
>>> target = 1997
>>> Solution().twoSum(nums, target)
[998, 999]
# 998 + 999 = 1997
```

**Template**

```python
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        return [0, 1]
```

**Test Case**: Total 100 points. `N` refers to the size (or length) of `nums`.

- 20 points: `-10 < a, b < 20` and `N < 5` 
- 20 points: `-20 < a, b < 20` and `N <= 10` 
- 20 points: `|a, b| < 100000` and `N <= 1000` 
- 20 points: `|a, b| < 1000000` and `N <= 10000` 
- 20 points: `|a, b| < 100000000` and `N <= 100000`