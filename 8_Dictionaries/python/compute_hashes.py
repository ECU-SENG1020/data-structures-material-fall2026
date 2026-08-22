import hashlib
import json
from pathlib import Path
import re

FILES = ["test.py"]


def sha256_file(path: Path) -> str:
    """Compute SHA-256 of the file after removing ALL whitespace (spaces, tabs, newlines).

    This normalizes line endings and other whitespace differences across OSes by
    stripping any \s characters before hashing. The file is read as UTF-8.
    """
    # Ensure we have a Path
    p = Path(path)
    text = p.read_text(encoding="utf-8")
    # Remove all whitespace (spaces, tabs, newlines, etc.)
    normalized = re.sub(r"\s+", "", text)
    return hashlib.sha256(normalized.encode("utf-8")).hexdigest()


def build_hashes(root: Path = Path(".")) -> dict:
    out = {}
    for fname in FILES:
        p = root / fname
        if p.exists():
            out[fname] = sha256_file(p)
        else:
            out[fname] = None
    return out


def write_hashes(path: Path = Path("file_hashes.json")) -> None:
    data = build_hashes(path.parent)
    path.write_text(json.dumps(data, indent=2))


if __name__ == "__main__":
    write_hashes()
    print("Wrote file_hashes.json")
