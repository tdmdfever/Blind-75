# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

Python solutions to the "Blind 75" set of classic coding-interview problems, worked through as 2026 summer homework. There is no package, no build system, no test framework, and no external dependencies (stdlib only: `collections`, `heapq`, `math`, `random`).

## Running a solution

Each file is standalone: it defines one or more solutions to the problem plus inline test calls (`print(...)` statements) at the bottom, and running the file prints its own output for manual verification against the expected outputs documented in the file's header docstring.

```bash
python "1: Sequences/01_twosum.py"
```

There is no test runner — "testing" a change means running the file directly and eyeballing the printed output against the docstring's `Expected Output` values.

## Structure

Problems are grouped into topic units, numbered in solve order (directory names include the number, e.g. `1: Sequences`):

- **1: Sequences** — arrays, strings, and interval problems
- **2: Data Structures** — linked lists, sliding window, and grid/graph basics
- **3: Nonlinear Data Structures** — trees and graphs
- **4: More Data Structures** — tries, heaps, and unions
- **5: Dynamic Programming** — not yet started

Within each unit, files are numbered in solve order: `NN_problemname.py`.

## File conventions

Every problem file follows the same shape — preserve it when adding or editing solutions:

1. A module-level docstring with the full problem statement plus 2-3 worked `Example` blocks (`Input:` / `Expected Output:` / `Justification:`).
2. One or more solution implementations. Files often contain multiple approaches to the same problem (e.g. a brute-force version alongside an optimized one, such as `two_sum` vs. `two_sum_solution` vs. `two_sum_two_pointers` in [1: Sequences/01_twosum.py](1: Sequences/01_twosum.py)) — this is intentional and not dead code to clean up.
3. A `# Test:` section at the bottom with bare `print(...)` calls exercising each implementation against the examples from the docstring.

For problems needing helper classes (tries, linked lists, trees, LRU caches, etc.), the supporting class (e.g. `TrieNode`) is defined above the main solution class in the same file.
