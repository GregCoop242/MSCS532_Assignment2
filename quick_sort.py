import random
import time

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)
    low = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    high = [x for x in arr if x > pivot]
    return quick_sort(low) + equal + quick_sort(high)



if __name__ == "__main__":
    
    print("Quick Sort Examples:")
    print("---------------------")
    print("Sorted Quick Sort Begin :")
    start = time.time()
    sorted_array = quick_sort([1, 2, 3, 4, 5, 6,7,8,9,10])
    end = time.time()
    print(f"Execution time: {end - start:.10f} seconds")
    print("Sorted Quick Sort End :")
    print("---------------------")
    print("Reverse Sorted Quick Sort Begin :")
    start = time.time()
    reverse_sorted = quick_sort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
    end = time.time()
    print(f"Execution time: {end - start:.10f} seconds")
    print("Reverse Sorted Quick Sort End :")
    print("---------------------")
    print("Random Quick Sort Begin :")
    start = time.time()
    random_sort = quick_sort([1, 4, 3, 7, 2, 5,9,6,10,8])
    end = time.time()
    print(f"Execution time: {end - start:.10f} seconds")
    print("Random Quick Sort End :")
    print("---------------------")    
    print("Quick Sort Completed.")