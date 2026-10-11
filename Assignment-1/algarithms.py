import time

def linear_search(records, target):
    for i in range(len(records)):
        if records[i] == target:
            return i
    return -1

def binary_search(records, target, low, high):
    if low > high:
        return -1

    mid = (low + high) // 2

    if records[mid] == target:
        return mid
    elif records[mid] < target:
        return binary_search(records, target, mid + 1, high)
    else:
        return binary_search(records, target, low, mid - 1)

def hash_search(record_set, target):
    return target in record_set

records = [1001, 1002, 1003, 1004, 1005]
target = 1003

start = time.perf_counter()
print("Linear Search:", linear_search(records, target))
print("Linear Search Time:", time.perf_counter() - start)

sorted_records = sorted(records)
start = time.perf_counter()
print("Binary Search:", binary_search(sorted_records, target, 0, len(sorted_records) - 1))
print("Binary Search Time:", time.perf_counter() - start)

record_set = set(records)
start = time.perf_counter()
print("Hash Search:", hash_search(record_set, target))
print("Hash Search Time:", time.perf_counter() - start)