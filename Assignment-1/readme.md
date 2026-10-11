# Design and Analysis of Algorithms — Assignment 1

## Student Record Retrieval: Design, Analysis, and Validation

## Task 1 — Design Three Searching Algorithms

**Approach A: Iterative Linear Search**
- Checks each student registration number one by one.
- Works with unsorted data.
- Time complexity: O(n).

**Approach B: Recursive Binary Search**
- Sorts the records and repeatedly divides the search range into halves.
- Time complexity: O(log n) after sorting.
- Sorting complexity: O(n log n).

**Approach C: Hash Table Search**
- Uses a hash table to find registration numbers.
- Expected search complexity: O(1).
- Requires additional memory for the hash table.

## Task 2 — Identify the Basic Operation

- Linear Search: Compare the target with each registration number.
- Binary Search: Compare the target with the middle element.
- Hash Search: Look up the registration number in the hash table.

## Task 3 — Derive Time Complexity Mathematically

**Linear Search**

Best case: Θ(1)

Average case: Θ(n)

Worst case: Θ(n)

**Binary Search**

Recurrence:

T(n) = T(n/2) + c

Solution: Θ(log n)

Sorting preprocessing: Θ(n log n)

**Hash Search**

Expected lookup: Θ(1)

Expected index construction: Θ(n)

Worst-case lookup: Θ(n)

## Task 4 — Best, Average, and Worst Cases

| Algorithm | Best Case | Average Case | Worst Case |
|---|---|---|---|
| Linear Search | Θ(1) | Θ(n) | Θ(n) |
| Binary Search | Θ(1) | Θ(log n) | Θ(log n) |
| Hash Search | Expected Θ(1) | Expected Θ(1) | Θ(n) |

## Task 5 — Asymptotic Analysis

- Linear Search: O(n)
- Binary Search: O(log n) after sorting.
- Hash Search: Expected O(1) lookup.

O represents an upper bound, Ω represents a lower bound, and Θ represents a tight asymptotic bound.

## Task 6 — Formulate the Recurrence Relation

For recursive binary search:

T(n) = T(n/2) + c, for n > 1

T(1) = c₀

Here, c represents the constant work performed in each recursive call.

## Task 7 — Solve the Recurrence Relation

T(n) = T(n/2) + c

T(n) = T(n/4) + 2c

T(n) = T(n/8) + 3c

After k steps:

T(n) = T(n/2ᵏ) + kc

When n/2ᵏ = 1:

k = log₂ n

Therefore:

**T(n) = Θ(log n)**

## Task 8 — Implement and Test the Algorithms

Implement the following algorithms using Python:

1. Iterative Linear Search
2. Recursive Binary Search
3. Hash Table Search

Test the algorithms with datasets containing:

- 1,000 records
- 10,000 records
- 100,000 records
- 1,000,000 records

Verify that each algorithm correctly handles both present and absent registration numbers.

## Task 9 — Measure Experimental Performance

Record the following for each dataset:

- Number of records
- Preprocessing time
- Search execution time
- Number of comparisons, where applicable

Save the measured results in `benchmark_results.csv`.

Run the program on your computer to obtain actual timings.

## Task 10 — Compare Theory with Experimental Results

- Linear Search is expected to become slower as the dataset grows.
- Binary Search is expected to grow logarithmically after sorting.
- Hash Search is expected to provide approximately constant-time lookup.

Compare the actual measurements with the theoretical complexity. Explain differences caused by computer performance, memory, and system load.

## Task 11 — Recommend and Justify the Best Algorithm

Hash Table Search is recommended for frequent exact registration-number searches because its expected lookup complexity is Θ(1).

Binary Search is a suitable alternative when records are maintained in sorted order.

Linear Search is less suitable for very large datasets because its worst-case complexity is Θ(n).

The final recommendation should also consider the measured results, memory usage, and update requirements.

## Task 12 — Day-4 Design Challenge

**Given requirements:**
- 1,000,000 student records
- 50,000 searches per hour
- New records added once per day

**A. Impact Analysis**

50,000 searches per hour is approximately 13.9 searches per second.

**B. Evaluate the Existing Design**

- Linear Search can require up to 1,000,000 comparisons per unsuccessful search.
- Binary Search requires approximately 20 comparison levels after sorting.
- Hash Search provides expected Θ(1) lookup.

**C. Adapt or Redesign**

Use a hash table as the primary lookup index. Build or update the index after the daily batch of new records arrives.

Maintain a sorted index if sorted reports or range searches are also required.

**D. Justification**

Hash Search is suitable because the system performs many searches between daily updates. Its index construction cost can be shared across many searches. Use experimental results to support the final decision.

## Conclusion

The assignment compares Linear Search, Binary Search, and Hash Search through algorithm design, mathematical analysis, implementation, and experimentation. For frequent exact registration-number searches across one million records, a hash-table index is a strong choice because its expected lookup time is constant.

## Repository Files

- `README.md` — Explanation of all 12 tasks
- `algorithms.py` — Algorithm implementations
- `benchmark.py` — Experimental testing program
- `benchmark_results.csv` — Measured experimental results
- `performance_plot.png` — Performance comparison graph
