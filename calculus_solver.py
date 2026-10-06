"""Calculus solver: differentiation and integration using SymPy.

Install:  pip install sympy
Run:      python calculus_solver.py
"""
from sympy import symbols, diff, integrate, simplify, sympify, latex, Integral, SympifyError
from sympy.parsing.sympy_parser import (
    parse_expr, standard_transformations,
    implicit_multiplication_application, convert_xor,
)

TRANSFORMS = standard_transformations + (implicit_multiplication_application, convert_xor)


def parse(expr_str, var_str):
    var = symbols(var_str)
    expr = parse_expr(expr_str, local_dict={var_str: var}, transformations=TRANSFORMS)
    return var, expr


def differentiate_expr(expr_str, var_str="x", order=1, point=None):
    var, expr = parse(expr_str, var_str)
    result = simplify(diff(expr, var, order))
    value = result.subs(var, point) if point is not None else None
    return expr, result, value


def integrate_expr(expr_str, var_str="x", lower=None, upper=None):
    var, expr = parse(expr_str, var_str)
    if lower is None or upper is None:
        result = integrate(expr, var)
        definite = False
    else:
        result = integrate(expr, (var, lower, upper))
        definite = True
    if isinstance(result, Integral):
        return expr, None, definite  # no closed form found
    return expr, simplify(result), definite


def do_differentiation():
    print("\n--- Differentiation ---")
    print("Examples: x^3 + 2x, sin(x)*exp(x), ln(x)/x")
    expr_str = input("f(x) = ").strip()
    if not expr_str:
        return
    var_str = input("Variable [x]: ").strip() or "x"
    order_str = input("Order of derivative [1]: ").strip() or "1"
    point_str = input("Evaluate at point (optional): ").strip()

    try:
        order = int(order_str)
        point = sympify(point_str) if point_str else None
        expr, result, value = differentiate_expr(expr_str, var_str, order, point)
    except (SympifyError, SyntaxError, ValueError, TypeError) as e:
        print(f"Could not process that input: {e}")
        return

    print(f"\nf({var_str}) = {expr}")
    print(f"Derivative (order {order}) = {result}")
    print(f"LaTeX: {latex(result)}")
    if value is not None:
        print(f"At {var_str} = {point}: {value}  (~ {value.evalf()})")


def do_integration():
    print("\n--- Integration ---")
    print("Examples: x^2, sin(x)*cos(x), 1/(x**2+1)")
    print("Limits may be numbers or symbols like pi, oo (infinity).")
    expr_str = input("f(x) = ").strip()
    if not expr_str:
        return
    var_str = input("Variable [x]: ").strip() or "x"
    lo_str = input("Lower limit (blank for indefinite): ").strip()
    hi_str = input("Upper limit: ").strip() if lo_str else ""

    try:
        lower = sympify(lo_str) if lo_str else None
        upper = sympify(hi_str) if hi_str else None
        expr, result, definite = integrate_expr(expr_str, var_str, lower, upper)
    except (SympifyError, SyntaxError, ValueError, TypeError) as e:
        print(f"Could not process that input: {e}")
        return

    if result is None:
        print("\nNo closed-form antiderivative found.")
        return

    if definite:
        print(f"\nIntegral from {lower} to {upper} of {expr} d{var_str}")
        print(f"  = {result}  (~ {result.evalf()})")
    else:
        print(f"\nIntegral of {expr} d{var_str}")
        print(f"  = {result} + C")
    print(f"LaTeX: {latex(result)}")


def main():
    print("=== Calculus Solver ===")
    while True:
        print("\nWhat would you like to do?")
        print("  1. Differentiate a function")
        print("  2. Integrate a function")
        print("  q. Quit")
        choice = input("Choose 1, 2 or q: ").strip().lower()

        if choice in ("1", "d", "differentiate"):
            do_differentiation()
        elif choice in ("2", "i", "integrate"):
            do_integration()
        elif choice in ("q", "quit", "exit"):
            print("Goodbye!")
            break
        else:
            print("Please enter 1, 2 or q.")


if __name__ == "__main__":
    main()
