# Potential Evaluation Questions for Practicals

Here are common questions examiners might ask during your practical evaluation, grouped by topic.

## General Algorithm Questions
*   **What is Time Complexity?** (Big O notation, Best/Average/Worst case)
*   **What is Space Complexity?** (Memory usage)
*   **Difference between Greedy and Dynamic Programming?**
    *   *Greedy*: Makes the best local choice at each step. Fast but doesn't always guarantee the global optimum.
    *   *DP*: Solves all subproblems and stores results to avoid re-computation. Guarantees global optimum but uses more memory.
*   **What is Divide and Conquer?** (Break problem into smaller sub-problems, solve them, and combine results).

## Practical Specific Questions

### 1. Sorting (Bubble, Insertion, Selection)
*   **Which sorting algorithm is best for small datasets?** (Insertion Sort is often fastest for very small or nearly sorted arrays).
*   **Why is Bubble Sort considered inefficient?** (It does many unnecessary swaps).
*   **What is the complexity of these sorts?** (O(N²) for all three in average/worst case).
*   **Can you name an O(N log N) sorting algorithm?** (Merge Sort, Quick Sort, Heap Sort).
*   **What is a "Stable" sort?** (Preserves the relative order of equal elements).

### 2. Recursion vs. Iteration (Sum, Fibonacci)
*   **Why is the recursive Fibonacci so slow?** (It recalculates the same values many times - overlapping subproblems).
*   **What is "Stack Overflow"?** (When recursion goes too deep and runs out of memory).
*   **When should you use Recursion?** (When the problem has a recursive structure, like trees or graphs, and code readability is important).

### 3. Greedy Algorithms (Coin Change, Fractional Knapsack)
*   **Does the Greedy Coin Change always work?** (No, it fails for some coin systems, e.g., Coins: [1, 3, 4], Target: 6. Greedy gives 4+1+1 (3 coins), Optimal is 3+3 (2 coins)).
*   **Why can we use Greedy for Fractional Knapsack but not 0/1 Knapsack?** (In Fractional, we can always take the "densest" item. In 0/1, taking the densest item might waste space that could be better filled by other items).
*   **What is the criteria for sorting in Fractional Knapsack?** (Profit/Weight ratio).

### 4. Dynamic Programming (LCS, Matrix Chain Multiplication)
*   **What is "Memoization"?** (Caching results of function calls).
*   **What does `dp[i][j]` represent in LCS?** (Length of LCS between first `i` chars of string A and first `j` chars of string B).
*   **Why do we need DP for Matrix Chain Multiplication?** (To find the optimal parenthesization to minimize scalar multiplications. The number of ways to parenthesize is exponential).

### 5. Huffman Coding
*   **What is a Prefix Code?** (No code is a prefix of another. Ensures no ambiguity in decoding).
*   **Why do frequent characters get shorter codes?** (To minimize total file size).
*   **What data structure is used to build the tree efficiently?** (Min-Heap / Priority Queue).

### 6. Graph Algorithms (Dijkstra, TSP)
*   **What is the difference between Dijkstra and Prim's algorithm?** (Dijkstra finds shortest path from source. Prim's finds Minimum Spanning Tree).
*   **Does Dijkstra work with negative weights?** (No, it can get into infinite loops or give wrong answers. Use Bellman-Ford).
*   **Why is TSP hard?** (It's NP-Hard. The number of routes grows factorially O(N!), so we can't solve it exactly for large N).
*   **What does the adjacency matrix represent?** (Connections and weights between nodes).

## Python Specific Questions
*   **What is the difference between a List and a Tuple?** (Lists are mutable, Tuples are immutable).
*   **What is `float('inf')`?** (Represents infinity, useful for initializing minimum search algorithms).
*   **How does `zip()` work?** (Combines multiple iterables element-wise).
*   **What is `matplotlib` used for?** (Plotting graphs and visualizations).
