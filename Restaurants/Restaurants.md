**Task**:
Given a list of restaurants, write a function to filter restaurants by rate, price and distance.

The attributes of a restaurant are given as four integers in this order: `id`, `rate`, `price`, `distance`. We guarantee `id` is unique and `min_price <= max_price`. The `rate` attribute has only five possible values: 1,2,3,4 or 5.

To filter the list, we will give you `min_price`, `max_price`, `min_rate`. Please return the restaurants’ `id` that meets the condition: `min_price <= price <= max_price` and `rate >= min_rate`.

The output is an integer list, which should be in the *increasing* order of `distance`; if there are restaurants whose `distance` equals, order the restaurants' `id` from the *largest to the smallest*.

In case6, we want you to implement two comparators for the class Restaurant. One is the natural order, which should be implemented by the comparable interface (java), the other one is a comparator object/method (called `Comparator1`).

For example, there is a list of restaurants, `r :list[Restaurant]`. `sorted(r)` will sort the array by calling the natural comparator. Similarly, `sorted(r, cmp=Comparator1)` will sort the list by `Comparator1`. See more details in the template block below.

The natural comparator should order the restaurants by the formula `distance * price / rate`, if the value is the same, keep the same order as input.

The `comparator1` should order the restaurants by the rate in *increasing* order, distance in *increasing* order (if tied), and id in *decreasing* order (if tied again).

---

**Template**
```python
import functools
from typing import List


class Restaurant(object):
    def __init__(self, id :int, rate :int, price :int, distance :int):
        pass

    def getID(self) -> int:
        return 0

    def __lt__(self, b) -> bool:
        """
        The natural comparator of Restaurant
        
        The comparator should compare the restaurants by the value calculated from the formula
        `distance * price / rate`
        and return True if the value of `self` is lower than `b`
        If the value is the same, keep the same order as input.
        """
        return True

    @staticmethod
    def comparator1(a, b) -> int:
        """
        Compare two restaurants by restaurant object

        Order the restaurants by the rate in increasing order,
        distance in increasing order (if tied),and 
        id in decreasing order (if tied again).
        
        Parameters:
            a(Restaurant): The restaurant object
            b(Restaurant): The restaurant object

        Return:
            result(int): -1 for restaurant a has smaller order, 1 for restaurant b has smaller order, 0 for equal.
        """
        return 0


class Restaurants(object):
    def __init__(self, restaurants :List[Restaurant]):
        pass

    def filter(self, min_price: int, max_price :int, min_rate: int) -> List[int]:
        """
        Filter the restaurants, output the list of restaurant id that meet the condition.

        Output the list in in the increasing order of distance;
        If the distance is the same, order the restaurant ids from the highest to the lowest.

        Return:
            restaurants (List[int]): The list of restaurant id.
        """
        return []
```

**Example**

```python
if __name__ == "__main__":
    rests = [
        # id, rate, price, distance
        Restaurant(20, 1, 20, 12),
        Restaurant(15, 3, 19, 11),
        Restaurant(19, 4, 19, 12),
        Restaurant(18, 5, 20, 11),
    ]
    r = Restaurants(rests)
    print(r.filter(0, 25, 3)) 
    print(r.filter(0, 25, 4)) 
    print(r.filter(0, 20, 1)) 
    print(r.filter(0, 10, 1))
    print(r.filter(0, 19, 1))
    print(r.filter(19, 19, 3))

    # case6
    rests = [
        # id, rate, price, distance
        Restaurant(3, 2, 3, 8),
        Restaurant(0, 2, 4, 6),
        Restaurant(2, 4, 5, 12),
        Restaurant(1, 5, 6, 11),
    ]
    print([i.getID() for i in sorted(rests)])
    print([i.getID() for i in sorted(rests, key=functools.cmp_to_key(Restaurant.comparator1))])

    """
Output:
[18, 15, 19]
[18, 19]
[18, 15, 20, 19]
[]
[15, 19]
[15, 19]
[3, 0, 1, 2]
[0, 3, 2, 1]
    """
```

---

**Test Case**: Total 100 points. <BR> 
1. `0 <= Distance`, `Price <= 10000`, `0 <= id <= 10000000`
2. The number of times of query(calling filter) will less than 1000
3. `N` refers to the number of restaurants
4. `M` refers to the total length of output for each sample(The total length of filter output for each class after initiation)
<BR>  
- 20 points: `N = 10`, `M < 100`
- 20 points: `N = 100000`, `M < 1000000`. Special Case
- 20 points: `N = 1000`, `M < 100*N`
- 20 points: `N = 9000`, `M < 100*N`
- 10 points: `N = 100000`, `M < 10*N`
- 10 points: Implementation of comparison.


