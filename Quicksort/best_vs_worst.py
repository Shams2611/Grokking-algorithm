"""
Best case vs worst case for quicksort

Best: O(n log n) - balanced partitions
Worst: O(n^2) - one side always empty
"""

call_count = 0


def quicksort_counted(arr):
    global call_count
    call_count += 1

    if len(arr) < 2:
        return arr

    pivot = arr[0]
    less = [x for x in arr[1:] if x <= pivot]
    greater = [x for x in arr[1:] if x > pivot]

    return quicksort_counted(less) + [pivot] + quicksort_counted(greater)


# worst case - already sorted
call_count = 0
sorted_arr = list(range(1, 11))
quicksort_counted(sorted_arr)
print(f"Sorted input [1-10]: {call_count} calls")

# better case - shuffled
import random
call_count = 0
shuffled = list(range(1, 11))
random.shuffle(shuffled)
quicksort_counted(shuffled)
print(f"Shuffled input: {call_count} calls")
