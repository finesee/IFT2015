# zhimingzeng_laurasanchezfernandez

class Empty(Exception):
    """Error attempting to access an element from an empty container."""
    pass

class Stack:
    """LIFO Stack implementation using a Python list as underlying storage."""
    def __init__(self):
        """Create an empty stack"""
        self._data = []         # nonpublic list instance

    def __len__(self):
        """Return the number of elements in the stack"""
        return len(self._data)

    def is_empty(self):
        """Return True if the stack is empty"""
        return len(self._data) == 0

    def push(self, e):
        """Add element e to the top of the stack"""
        self._data.append(e)            # new item stored at the end of list

    def top(self):
        """Return (but do not remove) the element at the top of the stack

        Raise Empty Exception if the stack is empty
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[-1]       # the last item in the list

    def pop(self):
        """Remove and return the element from the top of the stack (i.e., LIFO).

        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data.pop()     # remove last item from list

class Laby(object):
    """Solve a maze using the solve() method."""
    def __init__(self, LABYRINTHE, DIMENSION):
        """Initialize the labyrinth object."""
        if len(LABYRINTHE) != DIMENSION * DIMENSION:
            raise ValueError("lab's length doesn't equal dim^2 !")
        self.strLaby = LABYRINTHE
        self.dim = DIMENSION
        self.laby = []
        self.start = ()
        self.end = ()

        """Transform the labyrinth string to a 2-dimensional list,
        and confirm the starting point and finishing point if possible.
        """
        for j in range(self.dim):
            """Separate for dim lists"""
            list = []
            for i in range(self.dim):
                """Separate each item in the current list."""
                c = self.strLaby[j * self.dim + i]  # Get the current item
                if c == 'D':  # Check if it's the starting point
                    self.start = (j, i)
                elif c == 'F':  # Check if it's the finishing point
                    self.end = (j, i)
                list.append(c)  # Get the current list and append it to the final 2-dimensional list
            self.laby.append(list)  # Get the whole two dimensional list

        """Check if the starting point exists"""
        if self.start == ():
            raise Empty("There is no starting point")

        """Check if the finishing point exists"""
        if self.end == ():
            raise Empty("There is no finishing point")

    def show_laby(self):
        for list in self.laby:
            for item in list:
                print(item, end=" ")
            print()
        print("Starting point: {0}, finishing point: {1}".format(self.start, self.end))

    def solve(self):
        pass

labyStr = "########D#000##000#0###0##F###000################"
dim = 7
laby = Laby(labyStr, dim)
laby.show_laby()

# labyStr = "########0#000##000#0###0##F###000################"
# dim = 7
# laby = Laby(labyStr, dim)
# laby.show_laby()

# labyStr = "########D#000##000#0###0##0###000################"
# dim = 7
# laby = Laby(labyStr, dim)
# laby.show_laby()

# import datetime
# a = datetime.datetime.now()
# b = datetime.datetime.now()
# delta = b - a
# print(delta)

