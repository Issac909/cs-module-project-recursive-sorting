# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    A_index = 0
    B_index = 0
    x = 0
    # Your code here
    while A_index < len(arrA) and B_index < len(arrB):
        if arrA[A_index] <= arrB[B_index]:
            merged_arr[x] = arrA[A_index]
            x = x + 1
            A_index = A_index + 1

        else:
            merged_arr[x] = arrB[B_index]  
            x = x + 1
            B_index = B_index + 1

    while A_index < len(arrA):
        merged_arr[x] = arrA[A_index]    
        x = x + 1
        A_index = A_index + 1

    while B_index < len(arrB):
        merged_arr[x] = arrB[B_index] 
        x = x + 1
        B_index = B_index + 1 

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    if len(arr) < 2:
        return arr

    else:
        pivot_point = arr[0]
        lesser = [i for i in arr[1:] if i <= pivot_point]
        greater = [i for i in arr[1:] if i > pivot_point]
        return merge_sort(lesser) + [pivot_point] + merge_sort(greater)

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any eA_indextra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass

def merge_sort_in_place(arr, l, r):
    # Your code here
    pass
