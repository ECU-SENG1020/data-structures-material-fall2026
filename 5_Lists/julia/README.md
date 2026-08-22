# Custom Linked List (Julia)

This folder mirrors the Python/JavaScript versions, but in **Julia** and kept simple for new programmers.

## Files
- `NodeModule.jl` — defines a `Node`
- `ListModule.jl` — defines `DsList` (singly linked list)
- `app.jl` — small usage demo
- `demo_node.jl` — shows how nodes link together
- `unit_tests.jl` — tiny test runner

## Notes (Julia differences)
- Julia uses **1-based indexing**.
  - First element is `list[1]`, second is `list[2]`, etc.

## Run
From this folder:
- `julia app.jl`
- `julia unit_tests.jl`
