import timeit
import random
from tabulate import tabulate


def measure_time(sort_func, data):
    start_time = timeit.default_timer()
    sorted_data = sort_func(data[:])
    execution_time = timeit.default_timer() - start_time
    return sorted_data, execution_time


def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
    return lst


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))


def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged


def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    return arr

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


# Генеруємо випадкові дані для тестування
data_smallest = [random.randint(0, 1_000) for _ in range(10)]
data_small = [random.randint(0, 1_000) for _ in range(100)]
data_big = [random.randint(0, 1_000) for _ in range(1_000)]
data_largest = [random.randint(0, 10_000) for _ in range(10_000)]

# Генерація частково відсортованих даних
data_almost_sorted = sorted(data_largest)
data_almost_sorted[int(len(data_almost_sorted) * 0.9):] = reversed(data_almost_sorted[int(len(data_almost_sorted) * 0.9):])

# Генерація реверсивно відсортованих даних
data_reversed = list(reversed(data_largest))

test_data = [
    ("Random Smallest", data_smallest),
    ("Random Small", data_small),
    ("Random Big", data_big),
    ("Random Largest", data_largest),
    ("Almost Sorted", data_almost_sorted),
    ("Reversed", data_reversed)
]

sorting_functions = [
    ("Insertion Sort", insertion_sort),
    ("Merge Sort", merge_sort),
    ("Timsort (built-in sorted)", sorted),
    ("Bubble Sort", bubble_sort),
    ("Shell Sort", shell_sort),
    ("Selection Sort", selection_sort)
]

# Проведення тестування та виведення результатів
table = []
headers = ["Sorting Algorithm"] + [name for name, _ in test_data]

for sort_name, sort_func in sorting_functions:
    row = [sort_name]
    for _, data in test_data:
        _, exec_time = measure_time(sort_func, data)
        row.append(f"{exec_time:.6f}")
    table.append(row)

print(tabulate(table, headers=headers, tablefmt="github"))