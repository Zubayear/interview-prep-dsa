# Interview Prep DSA

Python practice repo for common interview problems and data structures.

## Canonical Layout

Use these as the main entry points for new work:

```text
src/
  data_structures/
    linear/
    trees/
    graphs/
  algorithms/
    searching/
    dynamic_programming/
  design_patterns/
problems/
  arrays/
  graphs/
  recursion/
  sliding_window/
tests/
  data_structures/
  algorithms/
  problems/
```

Suggested rules:

- Put each new reusable class in `src/data_structures/`.
- Put each reusable algorithm in `src/algorithms/`.
- Put each problem solution in `problems/`.
- Mirror the package structure in `tests/` so each module has a nearby test file.
- Prefer one solution module per problem, not large mixed grab-bags.

## Notes

- Use `src.*` and `problems.*` for new imports.
- Keep package-specific tests under `tests/data_structures/`, `tests/algorithms/`, and `tests/problems/`.
- The old top-level source packages were removed; add new work only in the canonical layout.

## Working In This Repo

- Run tests with `python3 -m pytest` from the repo root.
- Use a focused test path first, for example `python3 -m pytest tests/test_stack.py`.
- Import paths are the source of truth, even when they look unusual, but prefer the canonical `src.*` and `problems.*` paths for new code.

## Adding A New Problem

1. Pick the pattern folder that matches the solution technique.
2. Add the implementation module.
3. Add or update the matching test file under `tests/`.
4. Keep helper names and imports consistent with the existing module style.

## Notes

- This repo does not use a project manifest or package manager lockfile.
- Some older files still use legacy names and casing; keep them stable unless you are doing a deliberate cleanup.
