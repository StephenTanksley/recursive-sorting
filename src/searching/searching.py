# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    """
    U - Understand. A binary search performs by cutting the array in half every time
        until it reaches its target. In a recursive binary search, we use recursion
        to determine which half of the array to discard before trying again.
    P - Will require a base case where the length of the array is 0, a case where 
        the mid-point matches the target, a recursive case. If we find the target, we will return the index of the array where we found it. Else, we return -1.
    E - Write base case first
    R
    """

    mid = (start + end) // 2

    # base case 1 - length of array is 0
    if len(arr) == 0:
        return -1

    # base case 2 - we find what we're looking for.
    #   if the array with an index in the middle is equal to the target,
    #   we return 1 to indicate we found what we're looking for.
    if arr[mid] == target:
        return 1

    if arr[mid] > target:

    pass

# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively
# or iteratively


def agnostic_binary_search(arr, target):
    # Your code here
    pass
