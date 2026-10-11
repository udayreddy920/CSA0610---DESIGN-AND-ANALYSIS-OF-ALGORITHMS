"""
DAA Assignment 1: Search Strategies for a Student Record System
Python 3.x

This program compares:
1. Linear Search (iterative)
2. Binary Search (iterative, on sorted data)
3. Hash Search (Python dictionary)

It records preprocessing time, search time, and operation counts.
Timings are measured on the computer running this program and will vary.
"""
import csv
import random
import time

SIZES = [1_000, 10_000, 100_000, 1_000_000]
REPEATS = 5
RANDOM_SEED = 42


def linear_search(data, key):
    """Return (index, comparisons)."""
    comparisons = 0
    for i, value in enumerate(data):
        comparisons += 1
        if value == key:
            return i, comparisons
    return -1, comparisons


def binary_search(data, key):
    """Return (index, comparisons); data must be sorted."""
    low, high = 0, len(data) - 1
    comparisons = 0
    while low <= high:
        mid = (low + high) // 2
        comparisons += 1
        if data[mid] == key:
            return mid, comparisons
        if key < data[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1, comparisons


def benchmark(n):
    # Unique IDs representing student records.
    data = list(range(1_000_000, 1_000_000 + n))
    random.Random(RANDOM_SEED + n).shuffle(data)
    missing_key = -1  # Deliberately absent: measures a worst-case unsuccessful search.

    start = time.perf_counter()
    sorted_data = sorted(data)
    sort_seconds = time.perf_counter() - start

    start = time.perf_counter()
    hash_table = {student_id: student_id for student_id in data}
    hash_build_seconds = time.perf_counter() - start

    # Warm up and repeat searches. The reported time is the mean per search.
    linear_times = []
    for _ in range(REPEATS):
        start = time.perf_counter()
        result, linear_comparisons = linear_search(data, missing_key)
        linear_times.append(time.perf_counter() - start)
        assert result == -1

    binary_times = []
    for _ in range(REPEATS):
        start = time.perf_counter()
        result, binary_comparisons = binary_search(sorted_data, missing_key)
        binary_times.append(time.perf_counter() - start)
        assert result == -1

    hash_times = []
    for _ in range(REPEATS):
        start = time.perf_counter()
        result = hash_table.get(missing_key)
        hash_times.append(time.perf_counter() - start)
        assert result is None

    return {
        "n_records": n,
        "test": "unsuccessful search (key absent)",
        "linear_preprocessing_seconds": 0.0,
        "linear_mean_search_seconds": sum(linear_times) / REPEATS,
        "linear_comparisons": linear_comparisons,
        "binary_sort_preprocessing_seconds": sort_seconds,
        "binary_mean_search_seconds": sum(binary_times) / REPEATS,
        "binary_comparisons": binary_comparisons,
        "hash_build_preprocessing_seconds": hash_build_seconds,
        "hash_mean_search_seconds": sum(hash_times) / REPEATS,
        "hash_lookups": 1,
        "repeats": REPEATS,
    }


def main():
    rows = []
    for n in SIZES:
        print(f"Benchmarking n={n:,} ...")
        rows.append(benchmark(n))

    output_file = "Performance_Results.csv"
    with open(output_file, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)

    print("\nRESULTS (times are machine-dependent)")
    print(f"{'Records':>10} | {'Linear ms':>10} | {'Binary ms':>10} | {'Hash ms':>10}")
    print("-" * 53)
    for row in rows:
        print(
            f"{row['n_records']:>10,} | "
            f"{row['linear_mean_search_seconds'] * 1000:>10.4f} | "
            f"{row['binary_mean_search_seconds'] * 1000:>10.4f} | "
            f"{row['hash_mean_search_seconds'] * 1000:>10.4f}"
        )
    print(f"\nSaved measurements to {output_file}")


if __name__ == "__main__":
    main()
