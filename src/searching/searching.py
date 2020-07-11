# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    """
    U - Understand. A binary search performs by cutting the array in half every time
        until it reaches its target. In a recursive binary search, we use recursion
        to determine which half of the array to discard before trying again.

    P - Will require a base case where the length of the array is 0, a case where 
        the mid-point matches the target, a recursive case. If we find the target, we will return the index of the array where we found it. Else, we return -1.

    E - Write base case first, then consider recursive cases.

    R - Get it working first, then look for ways to optimize.
    """

    # define mid point at the start of the algorithm.
    mid = (start + end) // 2

    if start <= end:

        # base case 1 - length of array is 0
        if len(arr) == 0:
            return -1

        # base case 2 - we find what we're looking for.
        #   if the array with an index in the middle is equal to the target,
        #   return index of the item to show its location.
        if arr[mid] == target:
            # print(mid)
            # print(arr.index(arr[mid]))
            return arr.index(arr[mid])

        # recursive cases
        # target is less than the midpoint.
        if arr[mid] > target:
            return binary_search(arr, target, start, mid - 1)

        # target is greater than the midpoint.
        if arr[mid] < target:
            return binary_search(arr, target, mid + 1, end)
    else:
        return -1


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively
# or iteratively


def agnostic_binary_search(arr, target):
    # Your code here
    pass


"""
    To implement an order agnostic search, the same principles apply with some variations.
    
    1) We need to detect if the list is in ascending or descending order.
    2) We need to implement search cases for both of them.
    3) We need to have those cases trigger by the correctly detected list order.

"""
