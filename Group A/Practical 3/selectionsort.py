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