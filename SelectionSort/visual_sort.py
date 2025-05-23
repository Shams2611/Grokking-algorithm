"""
Visualize selection sort step by step

Helps understand what's happening at each iteration
"""

def selection_sort_visual(arr):
    arr = list(arr)
    n = len(arr)

    print(f"Start: {arr}\n")

    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        if min_idx != i:
            print(f"Step {i+1}: swap {arr[i]} with {arr[min_idx]}")
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
        else:
            print(f"Step {i+1}: {arr[i]} already in place")

        # show sorted vs unsorted parts
        sorted_part = arr[:i+1]
        unsorted_part = arr[i+1:]
        print(f"  Sorted: {sorted_part} | Unsorted: {unsorted_part}\n")

    return arr


test = [64, 25, 12, 22, 11]
result = selection_sort_visual(test)
print(f"Final: {result}")
