from email.mime import text
import pathlib
from TupleModule import DsTuple
import sys
import hashlib
import json
from pathlib import Path
import ast
import os
import re

failures = []
success_count = 0


def test_create():
    global success_count

    try:
        ds_tuple = DsTuple('a', 'b', 'c')
        assert(len(ds_tuple) == 3)
        success_count += 1
    except Exception as e:
        failures.append(('test_create', str(e)))

def test_get_item():
    global success_count
    
    try:
        ds_tuple = DsTuple('a', 'b', 'c')       
        assert(ds_tuple[1] == 'b')
        success_count += 1
    except Exception as e:
        failures.append(('test_get_item', str(e)))


def test_iter():
    global success_count
    count = 0
    try:
        ds_tuple = DsTuple('a', 'b', 'c')
        for item in ds_tuple:
            count += 1
        assert(count == 3)
        success_count += 1
    except Exception as e:
        failures.append(('test_iter', str(e)))  
    
def test_add():
    global success_count

    try:
        ds_tuple = DsTuple('a', 'b', 'c')

        ds_tuple2 = DsTuple('e', 'f', 'g')

        new_ds_tuple = ds_tuple + ds_tuple2

        normalized_str = str(new_ds_tuple).replace(" ", "")
        assert(normalized_str == "(a,b,c,e,f,g)")
        success_count += 1
    except Exception as e:
        failures.append(('test_add', str(e)))      

def test_in_true():
    global success_count
    try:
        ds_tuple = DsTuple('a', 'b', 'c')  
        result = 'b' in ds_tuple
        assert(len(ds_tuple) == 3 and result == True)
        success_count += 1
    except Exception as e:
        failures.append(('test_in_true', str(e)))   

def test_in_false():
    global success_count
    try:
        ds_tuple = DsTuple('a', 'b', 'c')
        result = 'z' in ds_tuple
        assert(result == False)

        assert(len(ds_tuple) == 3 and result == False)
        success_count += 1
    except Exception as e:
        failures.append(('test_in_false', str(e)))   

def test_index():
    global success_count
    try:
        ds_tuple = DsTuple('a', 'b', 'c')
        assert(ds_tuple.index('b') == 1)
        success_count += 1
    except Exception as e:
        failures.append(('test_index', str(e)))

def test_count():
    global success_count
    count = 0
    try:
        ds_tuple = DsTuple('a', 'b', 'c', 'b')
        assert(ds_tuple.count('b') == 2)
        success_count += 1
    except Exception as e:
        failures.append(('test_count', str(e)))


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

def test_builtin_list_used():
    global success_count    
    try:
        result = check_file_for_tuple()
        assert(result == False)
        success_count += 1
    except Exception as e:
        failures.append(('test_builtin_list_used', str(e))) 

def check_file_for_tuple():
    filename = "TupleModule.py"  # Hardcoded filename
    filepath = os.path.join(os.getcwd(), filename)

    if not os.path.exists(filepath):
        print(f"File '{filename}' not found in current directory.")
        return False

    with open(filepath, "r") as f:
        tree = ast.parse(f.read(), filename=filename)

    for node in ast.walk(tree):
        if isinstance(node, ast.Tuple):  # Tuple literal: (...)
            return True
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == "tuple":  # tuple()
            return True

    return False

def main():
    test_create()
    test_get_item()
    test_iter()
    test_add()
    test_in_true()
    test_in_false()
    test_index()
    test_count()
    test_file_hashes()
    test_builtin_list_used()

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

