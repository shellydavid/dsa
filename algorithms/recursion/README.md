# Recursion

Defining/solving a problem with smaller versions of itself

1. **Base case**: a condition where the function stops calling itself and returns a value
    - Necessary to prevent infinite recursion
    - If recursion goes too deep w/out returning, a StackOverflow error occurs
2. **Recursive case**: the function calling itself with a smaller/simpler input


## [`Recursive Call Stack`](./recursive_call_stack_practice.py)
Recursive function calls are managed via **call stacks**

1. For each recursive call, a new frame gets pushed onto the stack
    - Info related to the function is stored (local variables, return address, etc)
2. Once a base case is reached, this starts unwinding
    - The function returns its value to the return address (the function that directly called it) and gets popped


## [`Recursive Backtracking`](./recursive_backtracking.py)
Meant for exhaustive searches/brute-force 
<br>
*Ex: finding all possible solutions of a problem*

1. Make a decision
2. Do recursion
3. Hit base case
4. Undo the decision (backtrack)


## [`Recursive Data Structures`](./recursion_examples.py)
Recursion can be used for many problems on recursive-like data structures:
- Linked lists
- Trees
- Graphs

Leaves or NULL values are the base cases