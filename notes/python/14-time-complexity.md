## Time Complexity & Big O Notation: Comprehensive Guide
Time complexity quantifies the amount of time an algorithm takes to run as a function of the length of the input. It focuses on the growth rate rather than the specific number of milliseconds.
------------------------------
## 1. Big O Notation Basics

* Definition: Describes the upper bound of an algorithm's execution time (worst-case scenario).
* Rule 1: Drop Constants. $O(2n)$ becomes $O(n)$.
* Rule 2: Drop Less Significant Terms. $O(n^2 + n)$ becomes $O(n^2)$.
* Rule 3: Worst Case Matters. We usually care about the maximum possible time an algorithm could take.

------------------------------
## 2. Complexity Classes & Examples## O(1) — Constant Time
The execution time does not change regardless of the input size.

* Example: Accessing an array index or checking if a number is even/odd.

def get_first_element(arr):
    return arr[0] # Always 1 step

## O(log n) — Logarithmic Time
The input size is halved in every step. Very efficient for large datasets.

* Example: Binary Search.

def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target: return mid
        elif arr[mid] < target: low = mid + 1
        else: high = mid - 1
    return -1

## O(n) — Linear Time
The time grows proportionally with the input size.

* Example: A single loop through an array.

def find_max(arr):
    max_val = arr[0]
    for num in arr:
        if num > max_val:
            max_val = num
    return max_val

## O(n log n) — Linearithmic Time
Common in efficient sorting algorithms. It performs a logarithmic operation $n$ times.

* Example: Merge Sort, Quick Sort, Heap Sort.

## O(n²) — Quadratic Time
Performance is directly proportional to the square of the input size. Often involves nested loops.

* Example: Bubble Sort or comparing every element to every other element.

def print_pairs(arr):
    for i in arr:          # Runs n times
        for j in arr:      # Runs n times
            print(i, j)    # Total = n * n

------------------------------
## 3. Quick Reference Table

| Notation | Name | Growth Rate | Common Algorithm |
|---|---|---|---|
| O(1) | Constant | Flat | Array lookup |
| O(log n) | Logarithmic | Very Slow | Binary Search |
| O(n) | Linear | Steady | Single Loop |
| O(n log n) | Linearithmic | Moderate | Merge Sort |
| O(n²) | Quadratic | Fast | Nested Loops |
| O(2ⁿ) | Exponential | Explosive | Recursive Fibonacci |

------------------------------
## 4. How to Calculate (Steps)

   1. Count the steps: Identify loops and recursive calls.
   2. Identify the input ($n$): What is the size of the data?
   3. Simplify: Ignore constants (e.g., $5n \rightarrow n$).
   4. Pick the winner: Keep only the highest order term.

💡 Key Tip: If you see a nested loop, it's usually O(n²). If you see a loop that divides the data in half, it's usually O(log n).
------------------------------
I can provide more detail if you tell me:

* Do you need Space Complexity (memory usage) explained too?
* Are you preparing for a coding interview or a school exam?
* Would you like examples in a specific language like Java or C++?


