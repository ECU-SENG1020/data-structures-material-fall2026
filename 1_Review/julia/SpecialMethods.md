# Common "Special Methods" in Julia (Python dunder equivalents)

In Python, you customize behavior using *dunder methods* like `__len__`, `__getitem__`, and `__str__`.

In Julia, you customize behavior by adding methods to existing functions in `Base`.

## Examples

### Length
- Python: `__len__` → `len(x)`
- Julia: define `Base.length(x::YourType)` → `length(x)`

### Indexing
- Python: `__getitem__` → `x[i]`
- Julia: define `Base.getindex(x::YourType, i)` → `x[i]`

### Setting an index
- Python: `__setitem__` → `x[i] = v`
- Julia: define `Base.setindex!(x::YourType, v, i)` → `x[i] = v`

### Printing
- Python: `__str__` / `__repr__`
- Julia: define `Base.show(io::IO, x::YourType)`

### Iteration
- Python: `__iter__`
- Julia: define `Base.iterate(x::YourType, state=...)`

### Membership
- Python: `__contains__` → `v in x`
- Julia: define `Base.in(v, x::YourType)` → `v in x`

### Operator overloading
- Python: `__add__` → `a + b`
- Julia: define `Base.:+(a::YourType, b::YourType)`

## Key idea
Julia focuses on *functions + types* (multiple dispatch), rather than methods living inside a class.
