# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # TO-DO – put back together here

    a = 0
    b = 0

    for k in range(0, elements):
        # compare a and b
        # if a is bigger, put it in array and iterate both
        if a >= len(arrA):  # we're done with a, push b
            merged_arr[k] = arrB[b]
            b += 1
        # if b is bigger, put it in array and iterate both
        elif b >= len(arrB):
            merged_arr[k] = arrA[a]
            a += 1
        # if a is smaller, push b and iterate both
        elif arrA[a] < arrB[b]:
            merged_arr[k] = arrA[a]
            a += 1
        # if b is smaller, push a and iterate both
        else:
            merged_arr[k] = arrB[b]
            b += 1

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # TO-DO – split here

    # base case: if array length less than 1
    if len(arr) > 1:

        # find the middle of arr
        # sort items in left and put items to the left in left array
        left = merge_sort(arr[0: len(arr) // 2])
        # sort items in the right and put items to the right in right array
        right = merge_sort(arr[len(arr) // 2:])

        # merge left array and right array
        arr = merge(left, right)

    return arr


print(merge_sort([8, 3, 100, 43, 28, 1, 1000, 12, 24]))
# STRETCH: implement an in-place merge sort algorithm


def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
