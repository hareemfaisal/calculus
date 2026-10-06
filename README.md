# Calculus Solver

A Python command-line calculus solver that differentiates and integrates functions using SymPy, with support for higher-order derivatives, definite integrals, and LaTeX output.

## Features
- First and higher-order derivatives
- Evaluate a derivative at a specific point
- Indefinite and definite integrals (supports `pi` and `oo` as limits)
- Natural input such as `x^2` and `2x`
- LaTeX output for every result

## Installation
```bash
pip install sympy
```

## Usage
```bash
python calculus_solver.py
```
Choose 1 to differentiate or 2 to integrate, then type your function.

## Examples
| Task | Input | Result |
|------|-------|--------|
| Differentiate | `x^3`, order 1 | `3*x**2` |
| Differentiate | `x^3`, order 2 | `6*x` |
| Integrate | `x^2` | `x**3/3 + C` |
| Definite integral | `sin(x)`, 0 to `pi` | `2` |

## License
MIT
