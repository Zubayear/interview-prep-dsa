# Interview Prep DSA

Python practice repo for common interview problems and data structures.

## Canonical Layout

Use these as the main entry points for new work:

```text
patterns/
  arrays_hashing/
  binary_search/
  binary_tree/
  dp/
  graph/
  recursion/
  sliding_window/
  stack_queue/
  trie/
structures/
  stack/
  tree/
  graph/
tests/
  patterns/
  structures/
```

Suggested rules:

- Put each new problem in the pattern folder that matches the technique used to solve it.
- Keep reusable classes in `structures/`.
- Mirror the package structure in `tests/` so each module has a nearby test file.
- Prefer one solution module per problem, not large mixed grab-bags.

## Notes

- Use `patterns.*` for problem patterns and `structures.*` for reusable data structures.
- Keep package-specific tests under `tests/patterns/` and `tests/structures/`.
- The old top-level source packages were removed; add new work only in the canonical layout.

## Working In This Repo

- Run tests with `python3 -m pytest` from the repo root.
- Use a focused test path first, for example `python3 -m pytest tests/test_stack.py`.
- Import paths are the source of truth, even when they look unusual, but prefer the canonical `patterns.*` and `structures.*` paths for new code.

## Adding A New Problem

1. Pick the pattern folder that matches the solution technique.
2. Add the implementation module.
3. Add or update the matching test file under `tests/`.
4. Keep helper names and imports consistent with the existing module style.

## Notes

- This repo does not use a project manifest or package manager lockfile.
- Some older files still use legacy names and casing; keep them stable unless you are doing a deliberate cleanup.
