**Task**:
Implement a calendar that allows adding events on it.

Events will occupy the time interval `[start, end)` in the calendar, i.e. the time step x is unavailable in `start <= x < end`.

Make sure there are no overlapping events on the calendar. If the event request is violating the rule, please output `False` to reject the request, otherwise return `True` and then book the event in the time interval.

Initially, there is no event in the calendar, i.e. It is free for any event.

---
**Hint**
- Segment Tree(Tree interval as node)  OR
- Balanced Binary Search Tree(Allow Finding the min or max index)  OR
- Interval Search Tree
---
Words from teaching assistant:

For java user, TreeMap is a powerful data structure
For pythoner, sortedcontainers is allowed for this homework

This problem is easy though, you can try implement your own RBTree or any methods instead of using sortedcontainers packages. You will get more confidence on tree structure if you writen by your own.

Red-Black Tree implementation exmaples:

Java implemenatation https://algs4.cs.princeton.edu/33balanced/RedBlackBST.java.html

My implementation https://gist.github.com/linnil1/7db27e38fffa8f95c5443ce2ef608c6f

The performance of python-based RBTree written by yourself is always worse than the packages(Written in C++). I extend the TLE limit because I don’t want to punish you when you work hard to implement one.
(My RBTree takes 4s in case2)

---

**Template** and **Example**
```python
class Calendar:
    def __init__(self):
        ...

    def book(self, start: int, end: int) -> bool:
        """
        Book the event where interval started from start(included) to end(excluded)

        If availble: book it and return True
        else: return False
        """
        return True


if __name__ == "__main__":
    a = Calendar()
    print(a.book(10, 20))
    print(a.book(15, 25))
    print(a.book(20, 25))
    print(a.book(17, 21))
    print(a.book(0, 3)) 
    print(a.book(2, 6)) 
    print(a.book(3, 6)) 
    """ 
    True
    False  #[15, 20) is unavailable
    True
    False  #[17, 21] is unavailable
    True
    False  #[2, 3) is unavailable
    True
    """

    a = Calendar()
    print(a.book(5, 15))
    print(a.book(0, 18))
    print(a.book(24, 29))
    print(a.book(13, 25))
    print(a.book(18, 22))
    print(a.book(15, 18))
    """ 
    True
    False  #[5, 15) is unavailable
    True
    False  #[24, 25] is unavailable
    True
    True
    """
```
---
**Test Case**
1. `0 <= start, end <= M`, start and end are integer.
2. N is the number of booking events

- 20 points: N <= 10, M <= 50
- 20 points: N <= 10001, M < 200000 Special Case(Three samples)
- 20 points: N <= 1000, M <= 1000
- 20 points: N <= 20000, M <= 200000
- 20 points: N <= 120000, M <= 1000000




