from DsDictionaryModule import DsDictionary
import sys
import os
import pathlib
from pathlib import Path
import hashlib
import json
import ast
import re

failures = []
success_count = 0


def test_create_empty():
    global success_count
    try:
        d = DsDictionary()
        assert len(d) == 0
        success_count += 1
    except Exception as e:
        failures.append(('test_create_empty', str(e)))

def test_create_non_empty():
    global success_count
    try:
        d = DsDictionary([('a', 1), ('b', 2)])
        assert len(d) == 2
        success_count += 1
    except Exception as e:
        failures.append(('test_create_empty', str(e)))

def test_set():
    global success_count
    try:
        d = DsDictionary()
        d['a'] = 1
        assert len(d) == 1
        success_count += 1
    except Exception as e:
        failures.append(('test_set', str(e)))


def test_get():
    global success_count
    try:
        d = DsDictionary([('a', 1)])
        assert d['a'] == 1
        success_count += 1
    except Exception as e:
        failures.append(('test_get', str(e)))


def test_overwrite_value():
    global success_count
    try:
        d = DsDictionary()
        d['x'] = 5
        d['x'] = 10
        assert d['x'] == 10 and len(d) == 1
        success_count += 1
    except Exception as e:
        failures.append(('test_overwrite_value', str(e)))


def test_delitem():
    global success_count
    try:
        d = DsDictionary()
        d['k'] = 'v'
        del d['k']
        assert len(d) == 0
        success_count += 1
    except Exception as e:
        failures.append(('test_delitem', str(e)))


def test_keyerror():
    global success_count
    try:
        d = DsDictionary()
        try:
            _ = d['missing']
            failures.append(('test_keyerror', 'KeyError not raised for missing key'))
        except KeyError:
            success_count += 1
    except Exception as e:
        failures.append(('test_keyerror', str(e)))


def test_len():
    global success_count
    try:
        items = [('a', 1), ('b', 2), ('c', 3)]
        d = DsDictionary(items)
        assert len(d) == 3
        success_count += 1
    except Exception as e:
        failures.append(('test_len', str(e)))


def test_iter():
    global success_count
    try:
        items = [('a', 1), ('b', 2), ('c', 3)]
        d = DsDictionary(items)
        keys = [k for k in d]
        assert keys == ['a', 'b', 'c']
        success_count += 1
    except Exception as e:
        failures.append(('test_iter', str(e)))

def test_print_dsdictionary():
    global success_count
    try:
        items = [('a', 1), ('b', 2)]
        d = DsDictionary(items)
        normalized = str(d).replace(' ', '')
        assert normalized == "{'a':1,'b':2}"
        success_count += 1
    except Exception as e:
        failures.append(('test_print_dsdictionary', str(e)))

def test_print_keys():
    global success_count
    try:
        items = [('a', 1), ('b', 2)]
        d = DsDictionary(items)
        keys_view = d.keys()
        normalized = str(keys_view).replace(' ', '')
        assert normalized == "DsDictionaryView_Keys(['a','b'])"
        success_count += 1
    except Exception as e:
        failures.append(('test_print_keys', str(e)))

def test_print_values():
    global success_count
    try:
        items = [('a', 1), ('b', 2)]
        d = DsDictionary(items)
        values_view = d.values()
        normalized = str(values_view).replace(' ', '')
        assert normalized == "DsDictionaryView_Values([1,2])"
        success_count += 1
    except Exception as e:
        failures.append(('test_print_values', str(e)))

def test_print_items():
    global success_count
    try:
        items = [('a', 1), ('b', 2)]
        d = DsDictionary(items)
        items_view = d.items()
        normalized = str(items_view).replace(' ', '')
        assert normalized == "DsDictionaryView_Items([('a',1),('b',2)])"
        success_count += 1
    except Exception as e:
        failures.append(('test_print_items', str(e)))


def test_values():
    global success_count
    try:
        items = [('a', 1), ('b', 2)]
        d = DsDictionary(items)
        values_view = d.values()
        assert list(values_view) == [1, 2]
        success_count += 1
    except Exception as e:
        failures.append(('test_values', str(e)))

def test_items():
    global success_count
    try:
        items = [('a', 1), ('b', 2)]
        d = DsDictionary(items)
        items_view = d.items()
        assert list(items_view) == [('a', 1), ('b', 2)]
        success_count += 1
    except Exception as e:
        failures.append(('test_items', str(e)))

def test_view_reflects_changes():
    global success_count
    try:
        d = DsDictionary([('a', 1)])
        keys_view = d.keys()
        assert list(keys_view) == ['a']
        d['b'] = 2
        assert list(keys_view) == ['a', 'b']
        success_count += 1
    except Exception as e:
        failures.append(('test_view_reflects_changes', str(e)))


def _sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


def test_file_hashes():
    global success_count   
    filename = "file_hashes.json"  # Hardcoded filename
    filepath = os.path.join(os.getcwd(), filename)

    if not os.path.exists(filepath):
        print(f"File '{filename}' not found in current directory.")
        return False
 
    hashes_path = Path(filepath)
    try:
        assert hashes_path.exists(), (
            "file_hashes.json not found."
        )

        expected = json.loads(hashes_path.read_text())
        for fname, exp_hash in expected.items():
            p = Path(fname)
            assert p.exists(), f"Expected file {fname} is missing"
            # actual = _sha256_file(p)

            p = pathlib.Path(p)
            text = p.read_text(encoding='utf-8')
            normalized = re.sub(r"\s+", "", text)
            actual = hashlib.sha256(normalized.encode('utf-8')).hexdigest()

            assert (
                exp_hash == actual
            ), f"Hash mismatch for {fname}. Expected {exp_hash}, got {actual}."
        success_count += 1
    except Exception as e:
        failures.append(('test_file_hashes', str(e)))


def test_builtin_dictionary_used():
    global success_count    
    try:
        result = check_file_for_dictionary()
        assert(result == False)
        success_count += 1
    except Exception as e:
        failures.append(('test_builtin_dictionary_used', str(e))) 

def check_file_for_dictionary():
    filename = "DsDictionaryModule.py"  # Hardcoded filename
    filepath = os.path.join(os.getcwd(), filename)

    if not os.path.exists(filepath):
        print(f"File '{filename}' not found in current directory.")
        return False

    with open(filepath, "r") as f:
        tree = ast.parse(f.read(), filename=filename)

    for node in ast.walk(tree):
        # dictionary literal: {...}
        if isinstance(node, ast.Dict):
            return True
        # dict() constructor call
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == "dict":
            return True

    return False


def main():
    test_create_empty()
    test_create_non_empty()
    test_set()
    test_get()
    test_overwrite_value()
    test_delitem()
    test_keyerror()
    test_len()
    test_iter()
    test_print_dsdictionary()
    test_print_keys()
    test_print_values()
    test_print_items()
    test_values()
    test_items()
    test_view_reflects_changes()
    test_file_hashes()
    test_builtin_dictionary_used()


if __name__ == '__main__':
    main()
    print()
    if failures:
        for failure in failures:
            print(f"ERROR: {failure[0]} -> {failure[1]}")
        print(f"\n{len(failures)} tests failed")
        print(f"\n{success_count} tests passed")
        print()
        sys.exit()

    print()
    print(f"All {success_count} tests passed")
    print()
