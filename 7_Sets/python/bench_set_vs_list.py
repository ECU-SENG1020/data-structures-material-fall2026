"""
Benchmark: compare building a set vs searching a list.
Saves timings for:
 - building a set from a list
 - performing m membership checks against the list (``x in lst``)
 - performing m membership checks against the set (``x in s``)

Run this script and inspect the printed results. Results depend on CPU, Python version and memory.
"""
import random
import time
import sys

PARAMS = [10_000, 100_000, 500_000]
M = 10_000  # number of membership queries

print(f"Python: {sys.executable} {sys.version.replace(chr(10),' ')}")
print(f"Membership queries per test: {M}\n")

for n in PARAMS:
    # prepare data
    data = list(range(n))
    random.seed(0)
    queries = [random.randint(0, n - 1) for _ in range(M)]

    # time building a set from list
    t0 = time.perf_counter()
    s = set(data)
    t1 = time.perf_counter()
    set_build = t1 - t0

    # time membership checks on list
    t0 = time.perf_counter()
    hits_list = 0
    for q in queries:
        if q in data:
            hits_list += 1
    t1 = time.perf_counter()
    list_membership = t1 - t0

    # time membership checks on set
    t0 = time.perf_counter()
    hits_set = 0
    for q in queries:
        if q in s:
            hits_set += 1
    t1 = time.perf_counter()
    set_membership = t1 - t0

    # sanity
    assert hits_list == hits_set == M

    print(f"n={n:,}")
    print(f"  set build time:      {set_build:.6f} s")
    print(f"  list membership (m={M}): {list_membership:.6f} s")
    print(f"  set membership  (m={M}): {set_membership:.6f} s")
    if set_membership > 0:
        print(f"  membership speedup (list / set): {list_membership / set_membership:.1f}x")
    print()

print("Note: actual speedups vary by CPU, cache, Python version, and data sizes.")
print("Interpretation: building the set is O(n) but gives O(1) membership; repeated list membership is O(n) per query.")
