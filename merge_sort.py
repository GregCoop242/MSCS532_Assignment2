import random
import time


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i]); i += 1
        else:
            result.append(right[j]); j += 1
    return result + left[i:] + right[j:]

if __name__ == "__main__":
    
    print("Merge Sort Examples:")
    print("---------------------")
    print("Sorted Merge Sort Begin :")
    start = time.time()
    sorted_array = merge_sort([1, 2, 3, 4, 5, 6,7,8,9,10])
    end = time.time()
    print(f"Execution time: {end - start:.10f} seconds")
    print("Sorted Merge Sort End :")
    print("---------------------")
    print("Reverse Sorted Merge Sort Begin :")
    start = time.time()
    reverse_sorted = merge_sort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
    end = time.time()
    print(f"Execution time: {end - start:.10f} seconds")
    print("Reverse Sorted Merge Sort End :")
    print("---------------------")
    print("Random Merge Sort Begin :")
    start = time.time()
    random_sort = merge_sort([1, 4, 3, 7, 2, 5,9,6,10,8])
    end = time.time()
    print(f"Execution time: {end - start:.10f} seconds")
    print("Random Merge Sort End :")
    print("---------------------")    
    print("Merge Sort Completed.")