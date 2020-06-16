def linear_search(arr, target):
    for index, i in enumerate(arr):
        if i == target:
            return index
    return - 1 # not found

# Test

# arr = [-2, 7, 3, -9, 5, 1, 0, 4, -6]

# target = 0

# print(linear_search(arr, target))

# arr1 = [-9, -8, -6, -4, -3, -2, 0, 1, 2, 3, 5, 7, 8, 9]

# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    low_index = 0
    high_index = len(arr) - 1
    found = False
    while low_index <= high_index and not found:
    # compare the item in the middle of arr to the target
        middle_index = (low_index + high_index) // 2
        # if the item is the same return the index of the item
        if arr[middle_index] == target:
            found = True
            return middle_index
        # else if the item is less than the item in the middle
        elif arr[middle_index] < target:
            # set low index to 1 above the middle index
            low_index = middle_index + 1
        # else the item is greater than the item in the middle
        else:
            # set high index to 1 below the middle index
            high_index = middle_index -1
    return -1  # not found

# Test

# print(binary_search(arr1, target))
