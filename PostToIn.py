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

def postfixToInfix(exp):
    """Receives a String composed of operators and operands in postfixed order,

    and returns the equivalent expression in infixed order.
    """
    operatorList1 = ['+', '-', '*', '/', '<', '>'] # Operator Type 1: pop() twice plus '(' + ')'
    operatorList2 = ['=']                          # Operator Type 1: pop() twice without parentheses
    operatorList3 = ['\u221A', '!']                # Operator Type 2: pop() once
    stack = Stack()
    str = exp.split()
    # print(str)

    for c in str:
        if c not in operatorList1 and c not in operatorList2 and c not in operatorList3:
            """if not operator, push to stack"""
            stack.push(c)
        elif c in operatorList1:
            """if Operator Type 1: pop() twice for two oprands, 
            append with this operator, plus '(' + ')'
            """
            operator1 = stack.pop()
            operator2 = stack.pop()
            stack.push("(" + operator2 + c + operator1 + ")")
        elif c in operatorList2:
            """if Operator Type 2: pop() twice for two oprands, append with this operator"""
            operator1 = stack.pop()
            operator2 = stack.pop()
            stack.push(operator2 + c + operator1)
        elif c in operatorList3:
            """if Operator Type 3: pop() once for one oprand, append with this operator"""
            operator = stack.pop()
            stack.push(c + operator)
    return stack.pop()

exp = "9 √ 3 ="
print(postfixToInfix(exp))
exp = "15 7 1 1 + - / 3 * 2 1 1 + + -"
print(postfixToInfix(exp))
exp = "n ! n 1 + ! <"
print(postfixToInfix(exp))



