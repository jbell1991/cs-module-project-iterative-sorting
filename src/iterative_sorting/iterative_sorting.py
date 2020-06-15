# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # loop through unsorted elements
        for j in range(cur_index + 1, len(arr)):
            # if the element is < the current smallest
            if arr[j] < arr[smallest_index]:
                # set that element as the new current smallest
                smallest_index = j
                # print(arr) # uncomment to show how iterations of array changing
        # swap the minimum with the first unsorted position
        arr[smallest_index], arr[cur_index] = arr[cur_index], arr[smallest_index]
    return arr

# Test

# arr = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]

# print(selection_sort(arr))


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here
    # set swapped = True to enter while loop
    swapped = True
    while swapped:
        # are the elements swapped?
        swapped = False
        # loop through n-1 elements because the last element has nothing to its right
        for i in range(0, len(arr) - 1):
            left_element = i
            right_element = i + 1
            # if left element > right element
            if arr[left_element] > arr[right_element]: 
                # swap(left element, right element)
                arr[left_element], arr[right_element] = arr[right_element], arr[left_element]
                # set swapped to True to continue while loop until no swaps left
                swapped = True
                # print(arr) # uncomment to show iterations of array changing
    return arr

# Test

# print(bubble_sort(arr))

'''
STRETCH: implement the Count Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    # Your code here


    return arr
