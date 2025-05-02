"""
Quicksort with step-by-step output

See what happens at each recursion level
"""

def quicksort(arr, depth=0):
    indent = "  " * depth

    if len(arr) < 2:
        print(f"{indent}base case: {arr}")
        return arr

    pivot = arr[0]
    less = [x for x in arr[1:] if x <= pivot]
    greater = [x for x in arr[1:] if x > pivot]

    print(f"{indent}arr={arr}, pivot={pivot}")
    print(f"{indent}less={less}, greater={greater}")

    sorted_less = quicksort(less, depth + 1)
    sorted_greater = quicksort(greater, depth + 1)

    result = sorted_less + [pivot] + sorted_greater
    print(f"{indent}-> {result}")
    return result


test = [3, 1, 4, 1, 5]
print("Sorting:", test)
print()
quicksort(test)
