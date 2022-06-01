**Task**: Give a material with NxN grids which are initially blocked. We open the grid one-by-one and ask you to check if the grid is full or the material is percolation.

Definition:
- Open: Turn the blocked grid to open grid
- Full: The grid can connect to top row grid via a chain of neighboring (left, right, up, down) open grid.
- Percolation: There has full grid at the bottom row.

---

**Example**
```python
s = Percolation(3)
s.open(1,1)
print(s.isFull(1, 1)) 
print(s.percolates())
s.open(0,1)
s.open(2,0)
print(s.isFull(1, 1)) 
print(s.isFull(0, 1)) 
print(s.isFull(2, 0)) 
print(s.percolates())
s.open(2,1)
print(s.isFull(1, 1)) 
print(s.isFull(0, 1)) 
print(s.isFull(2, 0)) 
print(s.isFull(2, 1)) 
print(s.percolates())


=>

False
False

True
True
False
False

True
True
True
True
True
```
The final material should be like this
```
XOX
XOX
OOX
```

---

**Template**
```python
class Percolation:
    def __init__(self, N: int):
        """ Create N-by-N grid, with all sites blocked """
        pass

    def open(self, i :int, j :int):
        """ Open site (row i, column j) if it is not open already """
        pass

    def isOpen(self, i :int, j :int) -> bool:
        """ Is site (row i, column j) open? """
        return True

    def isFull(self, i :int, j :int) -> bool:
        """ Is site (row i, column j) full? We guarantee that site(i,j) is open when we call isFull. Note that 0 <= i < N and 0 <= j < N."""
        
        return True
            
    def percolates(self) -> bool:
        """ Does the system percolate? """
        return True
```

---

**Test Case**: Total 100 points. <BR> 
`N` refers to the number of sites on each side of the grid(i.e. N-by-N grid). Total number of times our judge calling your function will be smaller than `3N^2`.

- 20 points: `N < 5` 
- 20 points: `N < 50`. Special Cases
- 20 points: `N < 50`
- 20 points: `N < 100`
- 20 points: `N < 250`

