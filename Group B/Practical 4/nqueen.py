# # Implement a solution for a Constraint Satisfaction Problem using Branch and Bound 
# # and Backtracking for n-queens problem or a graph coloring problem  

# ### **1. Constraint Satisfaction Problem (CSP):**

# A **Constraint Satisfaction Problem (CSP)** is a mathematical problem defined by:

# * **Variables**: The entities you need to find a solution for. Each variable has a **domain** of possible values.
# * **Constraints**: Conditions or rules that restrict the possible assignments of values to variables.

# #### Example of CSP:

# For the **N-Queens problem**, the variables are the rows of the chessboard, the domain is the column positions (for each row), and the constraints are:

# * No two queens should be in the same column.
# * No two queens should be on the same diagonal.

# The task is to find an assignment of values (in this case, positions of queens) that satisfies all constraints.

# ---

# ### **2. Branch and Bound (B\&B):**

# **Branch and Bound (B\&B)** is an algorithm design paradigm for solving optimization problems, particularly **CSPs** and **combinatorial problems**. It systematically explores the solution space while **pruning** parts of the search space that cannot lead to better solutions.

# #### Key Concepts:

# * **Branching**: Split the problem into subproblems (or "branches"). For example, in the N-Queens problem, you can branch by placing a queen in each possible column of the current row.
# * **Bounding**: For each subproblem, compute a bound on the best possible solution within that branch. If the bound suggests that no better solution can be found in that subproblem, **prune** (discard) it.
# * **Pruning**: This process removes subproblems from the search space that cannot lead to an optimal solution.

# Branch and Bound is most useful when you want to minimize or maximize some objective, or when the search space is too large to explore exhaustively.

# #### Example of B\&B:

# In the N-Queens problem, while trying to place queens, we can prune branches where placing a queen violates the "no two queens in the same column" constraint, thereby eliminating unnecessary computations.

# ---

# ### **3. Backtracking:**

# **Backtracking** is another algorithmic approach used to solve CSPs, particularly useful when you need to explore all possible solutions while satisfying certain constraints.

# #### Key Concepts:

# * **Try**: Place a value for a variable (or queen) and continue to the next variable.
# * **Backtrack**: If a constraint is violated, **backtrack** by removing the last assignment and trying another possibility.
# * **Search Space Exploration**: Backtracking explores all possible assignments of variables, ensuring that it finds a solution that satisfies all constraints.

# #### Example of Backtracking:

# For the N-Queens problem, backtracking would involve trying to place queens one by one on the chessboard. If at any point you find that placing a queen violates a constraint, you remove the queen and try placing it in another position.

# ---

# ### **Differences Between Branch and Bound & Backtracking**:

# * **Backtracking**:

#   * Involves trying all possible assignments and backing up when a constraint is violated.
#   * It doesn't require any bounds to prune the search space.
# * **Branch and Bound**:

#   * Involves both branching and bounding. The key difference is the use of a bounding function that helps prune branches early, avoiding unnecessary search.
#   * Backtracking is a form of Branch and Bound but without any bounding or pruning logic.

# ---

# ### **Comparison:**

# * **Backtracking** is simple and intuitive. It explores every possible solution path and can be used when there are few constraints, or the search space is not large.
# * **Branch and Bound** is more efficient because it uses pruning based on bounds to eliminate large portions of the search space early on. It is more effective when the problem has an objective function to maximize or minimize.

# The 4-Queens problem has exactly 2 distinct solutions. (mirror images of each other)
# The 8-Queens problem has 92 total distinct solutions.
# 92 solutions count all distinct arrangements, even if some are symmetrical (rotated or reflected).

# If you only count fundamentally unique solutions (ignoring symmetrical ones), there are 12.

N = int(input("Enter dimension of board N by N: "))
# N = 4

# for i in range(N):
#     temp = []
#     for j in range(N):
#         temp.append(0)
#     board.append(temp)

#do the same thing as above but in a single line
board = [[0] * N for i in range(N)] # This line creates a 2D list (or matrix) of size N x N, initialized with zeroes.
# board = [[0 for i in range(N)] for j in range(N)] 
# [[0 for i in range(N)] for j in range(N)] is a list comprehension that creates a list of lists (i.e., a 2D array). Here's how it works:
# The outer list comprehension [ ... for j in range(N)] creates N rows.
# The inner list comprehension [0 for i in range(N)] creates a list of N zeroes for each row.

# print(board)

def isSafe(i,j):
    for p in range(N):
        if board[i][p] == 1 or board[p][j]== 1: # Check if any queen is in the same row or column. i.e keep row constant and check all columns, then keep column constant and check all rows.
            return False #this is normal hor or ver checker
    for n in range(N):
        for m in range(N):
            if (i+j) == (n+m) or (i-j) == (n-m): # Check if any queen is on the same diagonal. i.e check if the sum of the row and column indices are equal or the difference of the row and column indices are equal.
                if board[n][m] == 1: # Check if queens exist on that digaonal, This checks if the current position (i,j) is on the same diagonal as any other queen.
                    return False
    return True # If no queens are found in the same row, column, or diagonal, return True.

def nqueen(noq):
    if noq == 0: # Base case: If no queens are left to place, return True.
        return True
    
    for i in range(N):
        for j in range(N):
            if board[i][j] != 1 and isSafe(i,j):
                board[i][j] = 1
                if nqueen(noq-1) == True: # This line checks if the recursive call to nqueen with one less queen (noq-1) returns True.
                    return True
                board[i][j] = 0 # backtrack

    return False # If no valid position is found for the current queen, return False.

#Recursion = base condition + function calling itself
#Base condition = if all queens are placed successfully, return True
#Function calling itself = nqueen(noq-1) # This line calls the nqueen function with one less queen to place.


def printBoard(board):
    for row in board: # a simple way to print a 2D list (matrix) like your N x N chessboard in a readable format.
        print(' '.join('Q' if cell == 1 else '-' for cell in row))
# Explanation:
# board is a list of lists, like this for N = 4:

# [
#   [0, 0, 1, 0],
#   [1, 0, 0, 0],
#   [0, 0, 0, 1],
#   [0, 1, 0, 0]
# ]
# for i in board: loops through each row of the board (where i is each list like [0, 0, 1, 0]).

# print(i) prints that row.


if nqueen(N):
    printBoard(board)
else:
    print("No solution exists")