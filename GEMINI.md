# GEMINI.md - SIID-2 Project Context

## Project Overview
**SIID-2** (Sistemas de Información e Investigación de Operaciones 2) is a project focused on Operations Research and Optimization techniques, specifically Linear Programming, Integer Programming, and Mixed Integer Programming. It belongs to the DISA-UNAB department.

## Technical Stack
- **Language:** Python >= 3.14
- **Package Manager:** [uv](https://github.com/astral-sh/uv)
- **Core Libraries:**
  - `scipy.optimize`: For linear programming and optimization.
  - `pulp`: For linear and integer programming modeling and solving.
  - `numpy`, `pandas`: Data manipulation and numerical computations.
  - `matplotlib`, `seaborn`: Data visualization.

## Project Structure
- `main.py`: Entry point for the application.
- `notebooks/`: Contains Jupyter notebooks for exploration and exercises.
  - `linear-prog.ipynb`: Implementation of Simplex, Integer Programming, and MIP.
- `src/`: Source code directory.
- `pyproject.toml`: Project configuration and dependencies.

## Key Instructions
- Use `uv` for dependency management.
- Follow PEP 8 and use `ruff` for linting.
- All code changes should be verified with appropriate tests or by running the notebooks/scripts.
