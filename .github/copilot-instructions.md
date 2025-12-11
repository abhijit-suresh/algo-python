# Copilot Instructions for algo-python Repository

This repository is organized by algorithmic patterns, with each folder containing Python scripts that solve classic coding problems. The main focus is on clarity, modularity, and pattern-based organization for coding and algorithm practice.

## Directory Structure
- `Hash Map and Sets/Hash Maps/`: Contains hash map-based solutions (e.g., `pair_sum_unsorted.py`, `verify_sudoku_board.py`).
- `Two Pointers/Inward Traversal/`: Contains two-pointer pattern solutions (e.g., `3sum.py`, `is_valid_palindrome.py`, `largest_container.py`, `pair_sum_sorted.py`).
- `resources/`: Reference materials (e.g., `CodingPatterns2.pdf`).

## Key Patterns & Conventions
- Each script typically solves a single problem and is self-contained.
- Function names are descriptive and match the problem being solved (e.g., `is_valid_palindrome`, `verify_sudoku_board`).
- No external dependencies are required; all code uses standard Python libraries.
- No test framework or build system is present; scripts are run directly with Python.
- Input/output is usually hardcoded for demonstration purposes.
- No class-based architecture; solutions are procedural and focused on algorithmic clarity.

## Developer Workflow
- **Run a solution:**
  ```zsh
  python <path-to-script>
  # Example:
  python "Hash Map and Sets/Hash Maps/verify_sudoku_board.py"
  ```
- **Code formatting:**
  Use `black .` to auto-format all Python files.
- **Add new solutions:**
  Place new scripts in the appropriate pattern folder. Name files and functions to reflect the problem and pattern.
- **Reference patterns:**
  Use `resources/CodingPatterns2.pdf` for guidance on algorithmic approaches.

## Example Patterns
- **Hash Map:**
  - `pair_sum_unsorted.py`: Finds pairs with a given sum in an unsorted array using a hash map.
- **Two Pointers:**
  - `is_valid_palindrome.py`: Checks if a string is a palindrome using inward traversal.
  - `largest_container.py`: Solves the container-with-most-water problem using two pointers.

## AI Agent Guidance
- When generating new solutions, follow the existing file and function naming conventions.
- Keep code self-contained and focused on clarity.
- Avoid introducing external dependencies or complex architectures.
- Reference the `resources/CodingPatterns2.pdf` for accepted patterns.
- Scripts should be runnable as-is with Python 3.x.

---
If any section is unclear or missing important details, please provide feedback for further refinement.