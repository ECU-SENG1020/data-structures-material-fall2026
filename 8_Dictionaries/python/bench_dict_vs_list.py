"""
Benchmark: dictionary key lookups vs scanning a list of key/value pairs.
Saves timings for:
 - building a dict from pairs
 - performing m key lookups by scanning a list of pairs
 - performing m key lookups using dict membership/get
"""
import random
import time
import sys

PARAMS = [10_000, 100_000, 500_000]
M = 10_000

print(f"Python: {sys.executable} {sys.version.replace(chr(10), ' ')}")
print(f"Key lookup queries per test: {M}\n")

for n in PARAMS:
    entries = [(f"k_{i}", i) for i in range(n)]
    random.seed(0)
    queries = [f"k_{random.randint(0, n - 1)}" for _ in range(M)]

    t0 = time.perf_counter()
    d = dict(entries)
    t1 = time.perf_counter()
    dict_build = t1 - t0

    t0 = time.perf_counter()
    hits_scan = 0
    for q in queries:
        found = False
        for k, _ in entries:
            if k == q:
                found = True
                break
        if found:
            hits_scan += 1
    t1 = time.perf_counter()
    pair_scan_lookup = t1 - t0

    t0 = time.perf_counter()
    hits_dict = 0
    for q in queries:
        if q in d:
            hits_dict += 1
    t1 = time.perf_counter()
    dict_lookup = t1 - t0

    assert hits_scan == hits_dict == M

    print(f"n={n:,}")
    print(f"  dict build time:             {dict_build:.6f} s")
    print(f"  pair-scan lookup (m={M}):    {pair_scan_lookup:.6f} s")
    print(f"  dict key lookup (m={M}):     {dict_lookup:.6f} s")
    if dict_lookup > 0:
        print(f"  lookup speedup (scan / dict): {pair_scan_lookup / dict_lookup:.1f}x")
    print()

print("Note: actual speedups vary by CPU, cache behavior, and Python version.")
print("Interpretation: building a dict is O(n), then repeated key lookup is typically O(1).")
