# zhimingzeng_laurasanchezfernandez

import math

TRIED = '.'
OBSTACLE = '#'
DEAD_END = 'X'
START = 'D'
END = 'F'

# class Empty(Exception):
#     """Error attempting to access an element from an empty container."""
#     pass

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

    # def top(self):
    #     """Return (but do not remove) the element at the top of the stack
    #     Raise Empty Exception if the stack is empty
    #     """
    #     # if self.is_empty():
    #     #     raise Empty('Stack is empty')
    #     return self._data[-1]       # the last item in the list

    def pop(self):
        """Remove and return the element from the top of the stack (i.e., LIFO).
        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            # raise Empty('Stack is empty')
            return None
        return self._data.pop()     # remove last item from list


class Laby(object):
    """Solve a maze using the solve() method."""
    def __init__(self, LABYRINTHE, DIMENSION):
        """Initialize the labyrinth object."""
        # if len(LABYRINTHE) != DIMENSION * DIMENSION:
        #     raise ValueError("lab's length doesn't equal dim^2 !")
        self.strLaby = LABYRINTHE
        self.dim = DIMENSION
        self.laby = []
        self.start = ()
        self.end = ()
        self.path = Stack() # A stack to remember the path
        self.isFound = False # if the path is found

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

        # """Check if the starting point exists"""
        # if self.start == ():
        #     raise Empty("There is no starting point")
        # """Check if the finishing point exists"""
        # if self.end == ():
        #     raise Empty("There is no finishing point")

    def show_laby(self):
        for list in self.laby:
            for item in list:
                print(item, end=" ")
            print()
        print("Starting point: {0}, finishing point: {1}".format(self.start, self.end))

    """Search in the labyrinth recursively to find if the possible path to the end exists"""
    def searchFrom(self, row, column):
        """If run into an obstacle, return False"""
        if self.laby[row][column] == OBSTACLE: # obstacle
            return False
        """If the point has been visited, return False"""
        if self.laby[row][column] == TRIED or self.laby[row][column] == DEAD_END:
            return False
        """If the finishing point is found, get the Path and return True"""
        if self.laby[row][column] == END:
            self.path.push((row, column))
            self.isFound = True
            return True

        """Set the point to be visited"""
        self.laby[row][column] = TRIED

        """Try each direction in turn from the current point recursively"""
        isFound = self.searchFrom(row-1, column) or \
                  self.searchFrom(row+1, column) or \
                  self.searchFrom(row, column-1) or \
                  self.searchFrom(row, column+1)
        """If found or not"""
        if isFound:
            """Push the current point to the path stack if found"""
            self.path.push((row, column))
        else:
            """If not found, set the point to DEAD_END"""
            self.laby[row][column] = DEAD_END
        return isFound

    def solve(self):
        # pass
        """Search from the starting point"""
        self.searchFrom(self.start[0], self.start[1])

        if self.isFound:
            """Transform the path from stack to a traversed list"""
            list = self.stackToList()
            return self.isFound, list
        else:
            return self.isFound, None

    """Transform the path stack to a list"""
    def stackToList(self):
        list = []
        """Pop every item in the stack to a list"""
        e = self.path.pop()
        while e is not None:
            list.append(e)
            e = self.path.pop()
        # """Flip the list"""
        # l = len(list)
        # for i in range(l//2):
        #     list[i], list[l-i-1] = list[l-i-1], list[i]
        return list



def test(labyStr, dim):
    laby = Laby(labyStr, dim)
    laby.show_laby()
    iFound, list = laby.solve()
    print(iFound)
    print(list)

# labyStr = "#####D####F#####"
# dim = 4 # Fail
# test(labyStr, dim)
#
# labyStr = "#####D###0F#####"
# dim = 4 # Success
# test(labyStr, dim)
#
#
labyStr = "######D00##00####0F######"
# dim = 5 # True, Dead_End
test(labyStr, int(math.sqrt(len(labyStr))))
# labyStr = "######D#0##000###0F######"
# # dim = 5 # Ture, Straightforward
# test(labyStr, int(math.sqrt(len(labyStr))))
#
# labyStr = "#######D#00##000####0#F###000#######"
# dim = 6
# test(labyStr, dim)
# #
# labyStr = "########D#000##000#0###0##F###000################"
# dim = 7
# test(labyStr, dim)
#
#
# labyStr = "###########D#000#F0##000#0#00###0#0##00###000000####0#########0#00#00###000##00#####0000############"
# dim = 10
# test(labyStr, dim)
# #
# labyStr = "###########D#000#00##000#0#00###0#0##0F###000000####0#########0#00#00###000##00#####0000############"
# dim = 10
# test(labyStr, dim)
# #
# labyStr = "###########D#000##F##000#0#0####0#0##00###000000####0#########0#00#00###000##00#####0000############"
# dim = 10
# test(labyStr, dim)
#
# labyStr = "#####################D#000#00##0#000#00##000#0#00##000#0#00###0#0##00###0#0##00###000000####000000####0#########0#########0#00#000000#00#00###000##00###000##00#####0000######0000#######0###################0###############0#000#00##0#000#00##000#0#00#0000#0#00###0#0##0000#0#0##0F###000000####000000####0#########0#########0#00#00###0#00#00###000##00###000##00#####0000######0000######################"
# dim = 20 # Success
# test(labyStr, dim)
#
# labyStr = "#####################D#000#00##0#000#00##000#0#00##000#0#00###0#0##00###0#0##00###000000####000000####0#########0#########0#00#000000#00#00###000##00###000##00#####0000######0000#######0###################0###############0#000#00##0#000#00##000#0#00#0000#0#00###0#0##0000#0#0##00###000000####000000####0######F##0#########0#00#00###0#00#00###000##00###000##00#####0000######0000######################"
# dim = 20 # Fail
# test(labyStr, dim)

# laby.path.push((1,2))
# laby.path.push((3,4))
# laby.path.push((5,6))
# laby.path.push((7,8))
# list=laby.stackToTList()
# print(list)

# import datetime
# a = datetime.datetime.now()
# b = datetime.datetime.now()
# delta = b - a
# print(delta)
