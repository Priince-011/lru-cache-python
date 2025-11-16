# Build and Publish Instructions for in-memory-lru-cache

## 1. Install build tools
```bash
python -m pip install --upgrade build twine
```

## 2. Build the package
```bash
python -m build
```
This will create `dist/` with `.tar.gz` and `.whl` files.

## 3. (Optional) Test the build locally
```bash
pip install dist/in_memory_lru_cache-0.1.0-py3-none-any.whl
```

## 4. Publish to PyPI
```bash
python -m twine upload dist/*
```

## 5. Tag and push to GitHub
```bash
git tag v0.1.0
git push origin v0.1.0
```

---

## Run Tests
```bash
pip install -e .[dev]
pytest
```

---

## PyPI Metadata
- Name: in-memory-lru-cache
- Version: 0.1.0
- Author: Prince Kumar Singh
- License: MIT
- Python: >=3.8

---

## Directory Structure
```
in-memory-lru-cache/
├── src/lru_cache/
├── tests/
├── examples/
├── pyproject.toml
├── README.md
├── LICENSE
├── .gitignore
```
