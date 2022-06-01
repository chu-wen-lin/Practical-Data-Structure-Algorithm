**Scenario**: Let's play the board game. The height and width of the board are given as h and w. The playing pieces in our board game are called stones. There are two types of stones: 'O' and 'X'. A set of stones can be flipped if their connected stones are surrounded by another type of stones (not including border, the stone at the corner will never be surrounded).

Explanation:
```
# Both O are not surrounded by X
.X.
XOOX
.XX.

# Both O are surrounded by X
.XX
XOOX
.XX.

# Neither O or X is surrounded
OXO
XOX

```
---
**Task**: 
1. `putStone(x :List[int], y :List[int], stoneType :str)`: Put specific type of stones at (x[i],y[j]) on the board. We guarantee that there is not stone at (x[i],y[j]) on the board initially.
2. `surrounded(x :int, y :int) -> bool`: Return if the stone and its connected stones are surrounded by another type of stones, which means they are qualified to be flipped.
Connected is defined as two stones are next to each other in vertically or horizontally. We guarantee that there must have stone at (x[i],y[j]) when we call surrounded(x[i],y[j]).

**Output**: After we put the stones on the board, return if the stone at (x[i], y[j]) is surrounded or not. We may call both functions multiple times.

---

**Example**

Given a board
```
...    ...    .X.    .X.    .X.
... -> .O. -> XOX -> XOX -> XOX
...    ...    ...    .X.    OX.
```

```python
>>> g = BoardGame(3, 3)
>>> g.putStone([1], [1], 'O')
>>> print(g.surrounded(1, 1))
False

>>> g.putStone([0, 1, 1], [1, 0, 2], 'X')
>>> print(g.surrounded(1, 1))
False

>>> g.putStone([2], [1], 'X')
>>> print(g.surrounded(1, 1))
True
>>> print(g.surrounded(2, 1))
False

>>> g.putStone([2], [0], 'O')
>>> print(g.surrounded(2, 0))
False
```

---

**Template**

```python
from typing import List


class BoardGame:
    def __init__(self, h :int, w :int):
        """
        Set the width and height of the board.
        
        Parameters:
            h (int): The height of the board
            w (int): The width of the board
        """
        pass

    def putStone(self, x :List[int], y :List[int], stoneType :str):
        """
        Put the stone at (x[i],y[j]) on the board.
        
        We grantee that there are not stones at (x[i],y[j]) on the board initially.
        
        Parameters:
            x (int): The vertical position of the stone, 0 <= x < h
            y (int): The horizontal position of the stone, 0 <= y < w
            stoneType (string): The type of the stone to be put on the board, which has only two options {'O', 'X'}
        """
        pass

    def surrounded(self, x :int, y :int) -> bool:
        """
        Answer if the stone and its connected stones are surrounded by another type of stones, which means they are qualified to be flipped if we want.
        
        Parameters:
            x (int): The vertical position of the stone, 0 <= x < h
            y (int): The horizontal position of the stone, 0 <= y < w
        Returns:
            surrounded (bool): can be flipped or not.
        """
        return True
    
    def getStoneType(self, x :int, y :int) -> str:
        """
        Get the type of the stone at (x,y)
            
        We grantee that there must have stone at (x,y)
        
        Parameters:
            x (int): The vertical position of the stone, 0 <= x < h
            y (int): The horizontal position of the stone, 0 <= y < w
        Returns:
            stoneType (string): The type of the stones, which has only two value {'O', 'X'}
        """
        stoneType = 'X'
        return stoneType
```
We guarantee there is stone at (x,y) when we call surrounded(x,y)
And there is no stone at (x,y) when we call putStone(x,y).

---

**Test Case**: Total 100 points. <BR> 
`N`: the number of stones on the board.
`M`: the total number of times we call `putStone` or `surrounded`

- 20 points: `w,h < 3` and `M < 100`
- 20 points: `w,h <= 1001` and `M < 7000`. Special Case
- 20 points: `w,h <= 101` and `M < 1000`
- 20 points: `w,h <= 101` and `M < 4000`
- 20 points: `w,h <= 10001`and  `M < 4000`