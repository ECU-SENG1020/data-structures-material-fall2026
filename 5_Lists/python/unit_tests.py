from email.mime import text
import pathlib
from ListModule import DsList
import sys
import hashlib
import json
from pathlib import Path
import ast
import os
import re

failures = []
success_count = 0


def test_append():
    global success_count

    try:
        ds_list = DsList()
        ds_list.append('a')
        ds_list.append('b')
        ds_list.append('c')        
        assert(len(ds_list) == 3)
        success_count += 1
    except Exception as e:
        failures.append(('test_append', str(e)))
    
def test_get_item():
    global success_count
    
    try:
        ds_list_get_item = DsList()
        ds_list_get_item.append('a')
        ds_list_get_item.append('b')
        ds_list_get_item.append('c')        
        assert(ds_list_get_item[1] == 'b')
        success_count += 1
    except Exception as e:
        failures.append(('test_get_item', str(e)))

def test_set_item():
    global success_count
    
    try:
        ds_list_set_item = DsList()
        ds_list_set_item.append('a')
        ds_list_set_item.append('b')
        ds_list_set_item.append('c') 
        ds_list_set_item[1] = 'd'       
        assert(ds_list_set_item[1] == 'd')
        success_count += 1
    except Exception as e:
        failures.append(('test_set_item', str(e)))

def test_iter():
    global success_count
    count = 0
    try:
        ds_list = DsList()
        ds_list.append('a')
        ds_list.append('b')
        for item in ds_list:
            count += 1
        assert(count == 2)
        success_count += 1
    except Exception as e:
        failures.append(('test_iter', str(e)))  
    
def test_add():
    global success_count

    try:
        ds_list = DsList()
        ds_list.append('e')
        ds_list.append('b')

        new_ds_list = DsList()   

        ds_list2 = DsList()
        ds_list2.append('f')
        ds_list2.append('f')
        new_ds_list = ds_list + ds_list2        
        assert(str(new_ds_list) in ["['e','b','f','f']", "['e', 'b', 'f', 'f']", "[ 'e','b','f','f' ]", "[ 'e', 'b', 'f', 'f' ]"])
        success_count += 1
    except Exception as e:
        failures.append(('test_add', str(e)))      

def test_in_true():
    global success_count
    try:
        new_ds_list = DsList()   
        new_ds_list.append('e')
        new_ds_list.append('b')
        new_ds_list.append('f')
        new_ds_list.append('f')

        result = 'b' in new_ds_list

        assert(result == True)
        success_count += 1
    except Exception as e:
        failures.append(('test_in_true', str(e)))   

def test_in_false():
    global success_count
    try:    
        new_ds_list = DsList()   
        new_ds_list.append('e')
        new_ds_list.append('b')
        new_ds_list.append('f')
        new_ds_list.append('f')

        result = 'z' in new_ds_list

        assert(len(new_ds_list) == 4 and result == False)
        success_count += 1
    except Exception as e:
        failures.append(('test_in_false', str(e)))   

def test_clear():
    global success_count
    try:    
        new_ds_list = DsList()   
        new_ds_list.append('e')
        new_ds_list.append('b')
        new_ds_list.append('f')
        new_ds_list.append('f')

        new_ds_list.clear()

        assert(len(new_ds_list) == 0)
        success_count += 1
    except Exception as e:
        failures.append(('test_clear', str(e)))  

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
        result = check_file_for_list()
        assert(result == False)
        success_count += 1
    except Exception as e:
        failures.append(('test_builtin_list_used', str(e))) 

def check_file_for_list():
    filename = "ListModule.py"  # Hardcoded filename
    filepath = os.path.join(os.getcwd(), filename)

    if not os.path.exists(filepath):
        print(f"File '{filename}' not found in current directory.")
        return False

    with open(filepath, "r") as f:
        tree = ast.parse(f.read(), filename=filename)

    for node in ast.walk(tree):
        if isinstance(node, ast.List):  # List literal: [...]
            return True
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == "list":  # list()
            return True

    return False

def main():
    test_append()
    test_get_item()
    test_set_item()
    test_iter()
    test_add()
    test_in_true()
    test_in_false()
    test_clear()
    # test_file_hashes()
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

