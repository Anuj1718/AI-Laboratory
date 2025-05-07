# Selection Sort in Python
# This program sorts a list of numbers entered by the user using the Selection Sort algorithm.

def selection_sort(arr):
    # Traverse through all array elements
    for i in range(len(arr)-1):
        # Find the minimum element in the remaining unsorted array
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        # Swap the found minimum element with the first element of the unsorted part
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Input: Get a list of numbers from the user
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
#numbers = [ 64, 25, 12, 22, 11 ] # Example list

#OR
# Taking user input
# x = int(input("Enter the number of elements in the array: "))
# num = []

# for i in range(x):
#     val = int(input(f"Enter number {i + 1}: "))
#     num.append(val)

# Sort the list using Selection Sort
selection_sort(numbers)

# Output: Display the sorted list
print("Sorted list:", numbers)

#1st pass : first smallest element  is found and swapped with the first element of the list.
# 2nd pass : second smallest element is found and swapped with the second element of the list.
# 3rd pass : third smallest element is found and swapped with the third element of the list. 
#etc

# Summary:
# Case	Time Complexity	Space Complexity
# Best	O(n²)	O(1)
# Average	O(n²)	O(1)
# Worst	O(n²)	O(1)

# The outer loop runs n - 1 times because by the time the loop reaches the second-last element, the last one is already in its correct position.

# Let's break it down:
# If the list has n elements:

# 1st pass: places the smallest at index 0.

# 2nd pass: places the second smallest at index 1.

# ...

# (n-1)th pass: places the (n-1)th smallest at index n-2.

# At this point, only one element remains at the last index n-1, and since all smaller elements have already been placed before it, it's already in the right place.

# So:

# Looping one more time (i.e., to i = n-1) is unnecessary.

# There’s no next element to compare with, so the inner loop would not run at all for that iteration.


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:  # swap if out of order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Example
arr = [5, 2, 9, 1, 5, 6]
bubble_sort(arr)
print(arr)


# Bubble Sort compares adjacent elements and swaps them if they are in the wrong order. This process is repeated until the list is sorted.

# It "bubbles up" the largest unsorted element to its correct position in each pass.

# ime Complexity:
# Worst Case: O(n²) (when reversed)

# Average Case: O(n²)

# Best Case: O(n) (already sorted)

# 🔸 Space Complexity:
# O(1) (in-place sorting, no extra space)

# Input:
# arr = [5, 1, 4, 2]

# Pass 1:

# Compare 5 and 1 → swap → [1, 5, 4, 2]

# Compare 5 and 4 → swap → [1, 4, 5, 2]

# Compare 5 and 2 → swap → [1, 4, 2, 5]

# Pass 2:

# Compare 1 and 4 → OK

# Compare 4 and 2 → swap → [1, 2, 4, 5]

# Compare 4 and 5 → OK

# Pass 3:

# Compare 1 and 2 → OK

# Compare 2 and 4 → OK

# Sorted: [1, 2, 4, 5]

# 🔸 Explanation:
# Selection Sort finds the minimum element in the unsorted part and swaps it with the first element of the unsorted part. Repeats for the rest of the array.

# 🔸 Example:
# Input:
# arr = [5, 1, 4, 2]

# Step 1:

# Find min in [5, 1, 4, 2] → 1

# Swap 1 with 5 → [1, 5, 4, 2]

# Step 2:

# Find min in [5, 4, 2] → 2

# Swap 2 with 5 → [1, 2, 4, 5]

# Step 3:

# Find min in [4, 5] → 4

# Already in place

# Sorted: [1, 2, 4, 5]

# 🔸 Time Complexity:
# Worst Case: O(n²)

# Average Case: O(n²)

# Best Case: O(n²) (still checks all elements)

# 🔸 Space Complexity:
# O(1) (in-place)

# ✅ Summary:
# Algorithm	Best TC	Worst TC	SC	Stable?
# Bubble Sort	O(n)	O(n²)	O(1)	Yes
# Selection Sort	O(n²)	O(n²)	O(1)	No

#  What is a "Stable" Sorting Algorithm?
# A stable sorting algorithm preserves the relative order of elements with equal keys (values).

# 🔸 In simple terms:
# If two elements are equal, and one comes before the other in the original array, they will remain in the same order after sorting.

# Stability of Common Sorts:
# Algorithm	Stable?
# Bubble Sort	✅ Yes
# Selection Sort	❌ No
# Insertion Sort	✅ Yes
# Merge Sort	✅ Yes
# Quick Sort	❌ No
# Python’s sort()	✅ Yes (Timsort)