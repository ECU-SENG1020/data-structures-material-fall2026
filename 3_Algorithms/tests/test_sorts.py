import pytest
import importlib.util
import os


# helper to import module from path (works for filenames starting with digits)
def load_module_from_path(name, path):
	spec = importlib.util.spec_from_file_location(name, path)
	module = importlib.util.module_from_spec(spec)
	spec.loader.exec_module(module)
	return module


ROOT = os.path.dirname(os.path.dirname(__file__))

selection = load_module_from_path("selection_sort", os.path.join(ROOT, "6_selection_sort.py"))
insertion = load_module_from_path("insertion_sort", os.path.join(ROOT, "7_insertion_sort.py"))
merge = load_module_from_path("merge_sort", os.path.join(ROOT, "8_merge_sort.py"))


def test_selection_sort_basic():
	arr = [5, 3, 1, 4, 2]
	expected = sorted(arr)
	selection.selection_sort(arr)
	assert arr == expected


def test_selection_sort_counts():
	arr = [5, 3, 1, 4, 2]
	sorted_arr, comps, swaps = selection.selection_sort_with_counts(arr)
	assert sorted_arr == sorted(arr)
	assert isinstance(comps, int) and comps >= 0
	assert isinstance(swaps, int) and swaps >= 0


def test_insertion_sort_basic():
	arr = [9, 7, 8, 1, 2]
	expected = sorted(arr)
	insertion.insertion_sort(arr, len(arr))
	assert arr == expected


def test_insertion_sort_counts():
	arr = [9, 7, 8, 1, 2]
	sorted_arr, comps, shifts = insertion.insertion_sort_with_counts(arr)
	assert sorted_arr == sorted(arr)
	assert isinstance(comps, int) and comps >= 0
	assert isinstance(shifts, int) and shifts >= 0


def test_merge_sort_basic():
	arr = [3, 6, 1, 8, 2]
	expected = sorted(arr)
	merge.merge_sort(arr, 0, len(arr) - 1)
	assert arr == expected


def test_merge_sort_counts():
	arr = [3, 6, 1, 8, 2]
	sorted_arr, comps, copies = merge.merge_sort_with_counts(arr, 0, len(arr) - 1)
	assert sorted_arr == sorted(arr)
	assert isinstance(comps, int) and comps >= 0
	assert isinstance(copies, int) and copies >= 0
