Demo: Running and comparing sorting algorithms

This demo shows how to run the provided sorting scripts and the tests.

Run a script directly (examples are interactive prints):

```powershell
# Run selection sort demo
python 6_selection_sort.py

# Run insertion sort demo
python 7_insertion_sort.py

# Run merge sort demo
python 8_merge_sort.py
```

Run the tests (requires `pytest`):

```powershell
pip install pytest
pytest -q
```

What you should see
- Each script prints an "UNSORTED" and "SORTED" list.
- Each script prints a small "(demo) comparisons=..., swaps=..." line showing instrumented counts.

Use these counts in class to compare how many comparisons or copies each algorithm did on the same input.
